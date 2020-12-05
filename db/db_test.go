package db

import (
	"testing"
)

func TestStruct(t *testing.T) {

	//t.Logf("%#v\n", t{})
	t.Log("hello")
}

func TestReload(t *testing.T) {
	a := Reload()

	for _,i := range a{
		t.Log(i.Name)
	}
}
