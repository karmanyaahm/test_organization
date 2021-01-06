package utils

import (
	"testing"
)

func TestStruct(t *testing.T) {

	//t.Logf("%#v\n", t{})
	t.Log("hello")
}

// func TestReload(t *testing.T) {
// 	eventlist := db.Reload()

// 	a, err := FindEventByFuzzyName(eventlist, "geomap")
// 	t.Log(a.Name)
// 	t.Log(err)

// }

//func TestRotationInfo(t *testing.T) {
//	config.DefaultConfig()
//	db.Reload()
//
//	r := GetEventRotationInfo(db.EventList)
//
//	for i, j := range r {
//		t.Log(i)
//		for k, l := range j {
//			t.Log(k, l)
//		}
//	}
//}
