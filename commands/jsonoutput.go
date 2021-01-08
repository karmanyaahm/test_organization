package commands

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/karmanyaahm/test_organization/config"
	"github.com/karmanyaahm/test_organization/db"
	"github.com/karmanyaahm/test_organization/utils"
)

//func Rotations(div string) {
//	path := config.ByEventPath(div)
//
//	db.Reload()
//
//	cwd, _ := os.Getwd()
//	defer os.Chdir(cwd)
//	err := os.Chdir(path)
//	if err != nil {
//		log.Fatal(err)
//	}
//
//	//events, err := filepath.Glob(path + "/*/*")
//	if err != nil {
//		log.Fatal(err)
//	}
//
//	//	fmt.Println(events)
//
//	r := utils.GetEventRotationInfo(db.EventList)
//	//	fmt.Println(r)
//	for i, j := range r {
//		//fmt.Println(i)
//		events, _ := filepath.Glob(fmt.Sprintf("%s/%s/*.test", path, i)) //TODO: add isdir check
//		//	fmt.Println(j)
//		//	fmt.Println(events)
//		mapping := getRequiredDirs(events, j)
//		//		fmt.Println(mapping)
//
//		makeRotationDirs(filepath.Join(path, i), mapping)
//	}
//
//}
//
////TODO: for testing make this return mappings and do the actual symlink somewhere else
//func makeRotationDirs(eventPath string, mapping map[string][]string) {
//
//	//fmt.Println(eventPath)
//
//	for category, files := range mapping {
//		err := os.MkdirAll(filepath.Join(eventPath, category), 0755)
//		if err != nil {
//			if os.IsExist(err) {
//				//do nothing
//			} else {
//				log.Fatal(err)
//			}
//
//		}
//
//		for _, file := range files {
//			fname := filepath.Base(file)
//			target := filepath.Join(eventPath, category, fname)
//			//fmt.Println(target)
//			err := os.Symlink(file, target)
//			if err != nil {
//				if os.IsExist(err) {
//					//do nothing
//				} else {
//					log.Panic(err)
//				}
//			}
//		} //file in category
//
//	} //category
//
//}
//
//func getRequiredDirs(files []string, ref map[int]string) (ans map[string][]string) {
//	ans = map[string][]string{}
//
//	for _, i := range files {
//		yr := strings.Split(filepath.Base(i), "-")[1]
//		yrnum, err := strconv.Atoi(yr)
//		if err != nil {
//			fmt.Println(err)
//		}
//
//		rot := ref[yrnum]
//		if rot == "" {
//			fmt.Println(i, yr, "rotation not found")
//		}
//		ans[rot] = append(ans[rot], i)
//	}
//	return
//}
//
//FolderStructureByEvent frickin comments
type OneVal struct {
	Year     int    `json:"year"`
	Event    string `json:"event"`
	Location string `json:"location"`
	URL      string `json:"URL"`
	Div      string `json:"div"`
}
type Output = []OneVal

type Inp struct {
	Path, ID string
}
type Input = []Inp

var inpSrc io.Reader = os.Stdin
var outSrc io.Writer = os.Stdout

func JsonifyEvents() {
	db.Reload()
	dec := json.NewDecoder(inpSrc)
	enc := json.NewEncoder(outSrc)

	// read open bracket
	tok, err := dec.Token()
	if err != nil {
		log.Fatal(err)
	}
	outSrc.Write([]byte(fmt.Sprintf("%v\n", tok)))

	for dec.More() {
		i := Inp{}
		dec.Decode(&i)
		if !strings.HasSuffix(i.Path, ".test") {
			continue
		}
		split := strings.Split(i.Path, "/")
		split[len(split)-1] = strings.Split(split[len(split)-1], ".")[0]

		locationName := split[2]
		location, e := utils.FindInviByName(db.InviList, locationName)
		if e != nil {
			if e.Error() == "Not Found" {
			} else {
				log.Fatal(e)
			}
		}
		if len(location.FancyName) > 0 {
			locationName = location.FancyName
		} else {
			locationName = utils.MakeFancyName(locationName)
		}
		year, e := strconv.Atoi(split[1])
		check(e)
		event, e := utils.FindEventByFuzzyName(db.EventList, split[len(split)-1])
		check(e)

		name := event.Name
		if len(event.FancyName) > 0 {
			name = event.FancyName
		}

		div := strings.ToUpper(split[0])
		enc.Encode(OneVal{URL: config.URLPrefix + i.ID, Location: locationName, Year: year, Event: name, Div: div})
		if dec.More() {
			outSrc.Write([]byte(",\n"))
		}
	}
	// read closing bracket
	tok, err = dec.Token()
	if err != nil {
		log.Fatal(err)
	}

	outSrc.Write([]byte(fmt.Sprintf("%v\n", tok)))
}
func check(e error) {
	if e != nil {
		log.Fatal(e)
	}
}
