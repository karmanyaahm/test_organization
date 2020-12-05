package models

//Event an event
type Event struct {
	Name     string
	Category []string
	ids      []string
	Rotations map[int]string
}

//AddIds to the struct
func (e Event) AddIds(ids []string) {
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
func (e Event) GetIds() []string {
	return e.ids
}

