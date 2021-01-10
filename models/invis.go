package models

import "strings"

//Event an event
type Invi struct {
	Name      string
	FancyName string
	Public    []int
	Blocked   []int
}

//MakeEvent returns event with the following parameters
func MakeInvi(name, fancyName string) Invi {
	a := Invi{Name: name, FancyName: fancyName}
	return a
}

func (invi *Invi) GetFlags(year int) string {
	ans := ""

	for _, i := range invi.Public {
		if year == i || 0 == i {
			ans += "p"
		}
	}

	for _, i := range invi.Blocked {
		if year == i || 0 == i {
			ans += "b"
		}
	}

	return ans
}

func (invi *Invi) GetFancyName() string {
	if len(invi.FancyName) > 0 {
		return invi.FancyName
	} else {
		return strings.Title(strings.ReplaceAll(invi.Name, "_", " "))
	}
}
