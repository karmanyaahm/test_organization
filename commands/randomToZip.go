package commands

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/karmanyaahm/test_organization/db"

	"github.com/karmanyaahm/test_organization/utils"

	"github.com/bmatcuk/doublestar/v2"

	"github.com/karmanyaahm/test_organization/models"
)

//RandomToZip random to zip
func RandomToZip(wd string, div string) error {
	cwd, _ := os.Getwd()

	defer os.Chdir(cwd)
	err := os.Chdir(wd)
	if err != nil {
		log.Fatal(err)
	}

	for {
		db.Reload()
		notFound := 0
		//identify events
		basename := filepath.Base(wd)

		rfiles, rdirs := getRootFiles()

		events, notFound1 := identifyFromBases(rdirs)
		notFound += notFound1
		for file, event := range events {
			notFound += renameRootFolder(file, getFolderName(basename, event.Name, div))
		}

		events, notFound1 = identifyFromBases(rfiles)
		notFound += notFound1
		for file, event := range events {
			notFound += moveRootFile(file, getFolderName(basename, event.Name, div))
		}
		//delete empty dirs
		if notFound < 1 {
			break
		}
		pause()
	}
	return nil
}

func pause() {
	fmt.Print("Fix files and press enter to continue: ")
	fmt.Scanln()
}

func renameRootFolder(folder, fname string) int {
	err := os.Rename(folder, fname)
	if err != nil {
		if os.IsExist(err) {
			fmt.Println("target path " + fname + " already exists. Please solve merge conflicts manually.")
			return 1
		}
		panic(err)
	}
	return 0
}
func moveRootFile(file, fname string) int {
	err := os.Rename(file, filepath.Join(fname, file))

	if err != nil {
		if os.IsExist(err) {
			fmt.Println("target file " + filepath.Join(fname, file) + " already exists. Please solve merge conflicts manually.")
			return 1
		} else if os.IsNotExist(err) {
			os.Mkdir(fname, 0755)
			err = os.Rename(file, filepath.Join(fname, file))
			if err != nil {
				fmt.Println(err)
				panic(err)
			}

		} else {
			fmt.Println(err)
			panic(err)
		}
	}
	return 0
}
func getFolderName(basename, eventname string, div string) string {
	return fmt.Sprintf("%s-%s-%s.test", basename, eventname, div)
}

func identifyFromBases(s []string) (ls map[string]models.Event, notFound int) {
	ls = map[string]models.Event{}

	for _, j := range s {
		j = filepath.Base(j)
		e, err := utils.FindEventByFuzzyName(db.EventList, j)
		if err != nil {
			if err.Error() == "Not Found" {
				notFound++
			}
			fmt.Print(j + ": ")
			fmt.Println(err)
		} else {
			ls[j] = e
		}

	}
	return
}

func getRootFiles() ([]string, []string) {
	ans, err := doublestar.Glob("./*") //base directory only - don't go into subdirs
	if err != nil {
		fmt.Println(err)
	}
	return sortFilesAndDirs(ans)
}

func sortFilesAndDirs(f []string) (files, dirs []string) {
	for _, i := range f {
		stat, err := os.Stat(i)
		if err != nil {
			panic(err)
		}
		i, _ = filepath.Abs(i)
		if stat.Mode().IsRegular() { //is regular file - no directory symlink etc
			files = append(files, i)
		} else if stat.Mode().IsDir() {
			extension := strings.Split(i, ".")
			ext := extension[len(extension)-1]
			if ext == "test" {
				//just ignore if the directory ends with .test
			} else {
				dirs = append(dirs, i)

			}
		} else {
			fmt.Printf("Weird file: %s\n", i)
		}
	}
	return
}
