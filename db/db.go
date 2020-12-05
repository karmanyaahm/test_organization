package db

import (
	"fmt"
	"io/ioutil"
	"log"

	"github.com/karmanyaahm/test_organization/models"

	"gopkg.in/yaml.v2"
)

var eventListFile, blockListFile string

//Load loads filenames and tries to parse them with Reload
func Load(eventlistfile, blocklistfile string) []models.Event {
	eventListFile = eventlistfile
	fmt.Println(eventlistfile)
	blockListFile = blocklistfile
	return Reload()
}

type event struct {
	Ids       []string
	Rotations map[string][]int
	First     bool
}

type t struct {
	A map[string]map[string]map[string]event `yaml:"categories"`
}

//Reload reloads info
func Reload() []models.Event {
	ans := make([]models.Event, 0, 100)

	t := readFileToStructs()

	for i, j := range t.A { //category 1
		for k, l := range j { //category 2
			for m, n := range l { // events in that category

				e := parseEvent(i, k, m, n)

				if n.First {
					ans = insert(ans, e, 0)
				} else {
					ans = append(ans, e)
				}
			}
		}
	}
	return ans
}

func parseEvent(i, k, m string, n event) models.Event {

	rotations := map[int]string{}
	for o, p := range n.Rotations { //rotation parsing
		for q := range p {
			rotations[q] = o
		}
	}

	e := models.MakeEvent(m, []string{i, k})
	e.Rotations = rotations
	e.AddIds(n.Ids)
	return e
}

func readFileToStructs() t {
	data, _ := ioutil.ReadFile("../data/event_list.yml")
	out := t{}

	err := yaml.Unmarshal(data, &out)
	if err != nil {
		log.Fatalf("cannot unmarshal data: %v", err)
	}

	return out
}

func insert(arr []models.Event, val models.Event, location int) []models.Event {
	arr = append(arr, models.Event{})      // Step 1
	copy(arr[location+1:], arr[location:]) // Step 2
	arr[location] = val
	return arr
}
