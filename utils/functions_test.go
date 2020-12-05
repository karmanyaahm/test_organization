package utils

import (
	"testing"

	"github.com/karmanyaahm/test_organization/db"
)

func TestStruct(t *testing.T) {

	//t.Logf("%#v\n", t{})
	t.Log("hello")
}

func TestReload(t *testing.T) {
	eventlist := db.Reload()

	a, err := FindEventByFuzzyName(eventlist, "geomap")
	t.Log(a.Name)
	t.Log(err)

}
