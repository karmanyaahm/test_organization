package commands

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/karmanyaahm/test_organization/db"

	"github.com/karmanyaahm/test_organization/config"
)

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
