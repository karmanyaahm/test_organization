package commands

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strconv"
	"strings"

	"github.com/karmanyaahm/test_organization/db"
	"github.com/karmanyaahm/test_organization/utils"

	"github.com/karmanyaahm/test_organization/config"
)

func Rotations(div string) {
	path := config.ByEventPath(div)

	db.Reload()

	cwd, _ := os.Getwd()
	defer os.Chdir(cwd)
	err := os.Chdir(path)
	if err != nil {
		log.Fatal(err)
	}

	//events, err := filepath.Glob(path + "/*/*")
	if err != nil {
		log.Fatal(err)
	}

	//	fmt.Println(events)

	r := utils.GetEventRotationInfo(db.EventList)
	//	fmt.Println(r)
	for i, j := range r {
		//fmt.Println(i)
		events, _ := filepath.Glob(fmt.Sprintf("%s/%s/*.test", path, i)) //TODO: add isdir check
		//	fmt.Println(j)
		//	fmt.Println(events)
		mapping := getRequiredDirs(events, j)
		//		fmt.Println(mapping)

		makeRotationDirs(filepath.Join(path, i), mapping)
	}

}

//TODO: for testing make this return mappings and do the actual symlink somewhere else
func makeRotationDirs(eventPath string, mapping map[string][]string) {

	//fmt.Println(eventPath)

	for category, files := range mapping {
		err := os.MkdirAll(filepath.Join(eventPath, category), 0755)
		if err != nil {
			if os.IsExist(err) {
				//do nothing
			} else {
				log.Fatal(err)
			}

		}

		for _, file := range files {
			fname := filepath.Base(file)
			target := filepath.Join(eventPath, category, fname)
			//fmt.Println(target)
			err := os.Symlink(file, target)
			if err != nil {
				if os.IsExist(err) {
					//do nothing
				} else {
					log.Panic(err)
				}
			}
		} //file in category

	} //category

}

func getRequiredDirs(files []string, ref map[int]string) (ans map[string][]string) {
	ans = map[string][]string{}

	for _, i := range files {
		yr := strings.Split(filepath.Base(i), "-")[1]
		yrnum, err := strconv.Atoi(yr)
		if err != nil {
			fmt.Println(err)
		}

		rot := ref[yrnum]
		if rot == "" {
			fmt.Println(i, yr, "rotation not found")
		}
		ans[rot] = append(ans[rot], i)
	}
	return
}

//FolderStructureByEvent frickin comments
func FolderStructureByEvent(div string) {
	scanpath := config.ByInvitationalPath(div)
	targetpath := config.ByEventPath(div)

	db.Reload()

	cwd, _ := os.Getwd()
	defer os.Chdir(cwd)
	err := os.Chdir(scanpath + "/..")
	if err != nil {
		log.Fatal(err)
	}

	events, err := filepath.Glob(scanpath + "/*/*")
	if err != nil {
		log.Fatal(err)
	}

	events = filterEventPaths(events)

	pathMap := parsePaths(events)

	makeEventPaths(targetpath, pathMap)

	symlinkThings(targetpath, pathMap)

	l1, err := filepath.Rel(config.CallPath, scanpath)
	if err != nil {
		fmt.Println(err)
	}
	l2, err := filepath.Rel(config.CallPath, targetpath)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("%s mapped to %s\n", l1, l2)

}

func symlinkThings(targetpath string, pathMap map[string]string) {
	for path, event := range pathMap {
		fname := filepath.Base(path)
		target := filepath.Join(targetpath, event, fname)
		err := os.Symlink(path, target)
		if err != nil {
			if os.IsExist(err) {
				//do nothing
			} else {
				log.Panic(err)
			}
		}
	}
}

func makeEventPaths(targ string, events map[string]string) {
	trueEvents := map[string]bool{}
	for _, k := range events {
		trueEvents[k] = true
	}

	for event := range trueEvents {
		err := os.MkdirAll(filepath.Join(targ, event), 0755)
		if err != nil {
			if os.IsExist(err) {
				//do nothing
			} else {
				log.Fatal(err)
			}
		}
	}
}

func filterEventPaths(v []string) (a []string) {
	for _, i := range v {
		if filepath.Ext(i) == ".test" {
			a = append(a, i)
		}
	}
	return
}
func parsePaths(v []string) (a map[string]string) {
	a = map[string]string{}

	for _, i := range v {
		f := strings.Split(filepath.Base(i), "-")
		a[i] = f[len(f)-2]
	}
	return
}
