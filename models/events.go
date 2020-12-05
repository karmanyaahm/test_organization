package models

import "strings"

//Event an event
type Event struct {
	Name      string
	Category  []string
	ids       []string
	Rotations map[int]string
}

//AddIds to the struct
func (e *Event) AddIds(ids []string) {
	a := map[string]bool{}

	for _, k := range e.ids {
		a[k] = true
	}
	for _, k := range ids {
		a[k] = true
	}
	ans := []string{}
	for k := range a {
		ans = append(ans, k)
	}
	e.ids = ans
}

//GetIds getids
func (e *Event) GetIds() []string {
	return e.ids
}

//MakeEvent returns event with the following parameters
func MakeEvent(name string, category []string) Event {
	a := Event{Name: name, Category: category}
	a.AddIds([]string{
		name,
		strings.Replace(name, "_", " ", -1),
		strings.Replace(name, "_", "", -1),
		strings.Replace(name, " ", "", -1),
	})
	return a
}
