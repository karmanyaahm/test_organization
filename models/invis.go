package models

//Event an event
type Invi struct {
	Name      string
	FancyName string
}

//MakeEvent returns event with the following parameters
func MakeInvi(name, fancyName string) Invi {
	a := Invi{Name: name, FancyName: fancyName}
	return a
}
