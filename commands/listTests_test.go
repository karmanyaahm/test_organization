package commands

import (
	"path/filepath"
	"testing"

	"github.com/karmanyaahm/test_organization/config"
	"github.com/karmanyaahm/test_organization/db"
	"github.com/karmanyaahm/test_organization/models"
)

func TestListing(t *testing.T) {
	config.DefaultConfig()
	db.Reload()
	path, _ := filepath.Abs("../tests/listing/c/")
	db.InviList = []models.Invi{
		models.Invi{Name: "invi3", FancyName: "INVI3", Public: []int{0}},
		models.Invi{Name: "invi2", Public: []int{0}, Blocked: []int{0}},
		models.Invi{Name: "invi1", Blocked: []int{2020}},
	}
	val := [][]string{
		{"invis", "2020", "2021"},
		{"Invi1", "2b", "2"},
		{"Invi2", "0", "3pb"},
		{"INVI3", "0", "3p"},
	}
	out := getValues(path)
	for a, b := range val {
		for c, d := range b {
			if d != out[a][c] {
				t.Log(d, out[a][c])
				t.Log(out)
				t.FailNow()
			}
		}
	}

}
