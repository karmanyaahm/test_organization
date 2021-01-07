package db

import (
	"errors"
	"io/ioutil"
	"log"

	"github.com/karmanyaahm/test_organization/config"

	"github.com/karmanyaahm/test_organization/models"
	"github.com/karmanyaahm/test_organization/utils"

	"gopkg.in/yaml.v2"
)

var EventList []models.Event
var InviList []models.Invi

type event struct {
	FancyName string `yaml:"fancy_name"`
	Ids       []string
	Rotations map[string][]int
	First     bool
}

type t struct {
	A map[string]map[string]map[string]event `yaml:"categories"`
}

type invis map[string]struct {
	Name string
}

//Reload reloads info
func Reload() {
	ans := make([]models.Event, 0, 100)
	invisList := make([]models.Invi, 0, 100)

	dataStruct := t{}
	readFileToStructs(config.DataPath, &dataStruct)

	inviStruct := invis{}
	readFileToStructs(config.InviPath, &inviStruct)

	for i, j := range dataStruct.A { //category 1
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

	for i, j := range inviStruct {
		fancyName := j.Name
		if len(fancyName) == 0 {
			fancyName = utils.MakeFancyName(i)
		}
		invisList = append(invisList, models.Invi{Name: i, FancyName: fancyName})
	}

	EventList = ans
	InviList = invisList

	if len(EventList) < 1 {
		panic(errors.New("List Reload Failed"))
	}
}

func parseEvent(i, k, m string, n event) models.Event {

	rotations := map[int]string{}
	for o, p := range n.Rotations { //rotation parsing
		for _, q := range p {
			rotations[q] = o
		}
	}
	if len(n.FancyName) == 0 {
		n.FancyName = utils.MakeFancyName(m)
	}
	e := models.MakeEvent(m, n.FancyName, []string{i, k})
	e.Rotations = rotations
	e.AddIds(n.Ids)
	return e
}

func readFileToStructs(location string, struc interface{}) {
	data, err := ioutil.ReadFile(location)
	if err != nil {
		panic(errors.New("Wrong Event File Path Configured"))
	}

	err = yaml.Unmarshal(data, struc)
	if err != nil {
		log.Fatalf("cannot unmarshal data: %v", err)
	}

}

func insert(arr []models.Event, val models.Event, location int) []models.Event {
	arr = append(arr, models.Event{})      // Step 1
	copy(arr[location+1:], arr[location:]) // Step 2
	arr[location] = val
	return arr
}
