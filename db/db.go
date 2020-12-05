package db

import (
	"io/ioutil"
	"log"
	"github.com/karmanyaahm/test_organization/models"

	"gopkg.in/yaml.v2"
)

var eventListFile, blockListFile string

//Load loads filenames and tries to parse them with Reload
func Load(eventlistfile, blocklistfile string) []models.Event {
	eventListFile = eventlistfile
	blockListFile = blocklistfile
	return Reload()
}

type event struct {
	Ids       []string
	Rotations map[string][]int
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

				rotations := map[int]string{}
				for o, p := range n.Rotations { //rotation parsing
					for q := range p {
						rotations[q] = o
					}
				}

				e := models.MakeEvent(name: m, category: []string{i, k})
				e.Rotations = rotations
				e.AddIds(n.Ids)

				ans = append(ans, e)
			}
		}
	}
	return ans
}

func readFileToStructs() t {
	data, _ := ioutil.ReadFile("../../data/event_list.yml")
	out := t{}

	err := yaml.Unmarshal(data, &out)
	if err != nil {
		log.Fatalf("cannot unmarshal data: %v", err)
	}

	return out
}
