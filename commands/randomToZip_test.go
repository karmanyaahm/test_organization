package commands

import (
	"path/filepath"
	//"os"
	"testing"

	"github.com/karmanyaahm/test_organization/config"
)

// func TestFileGlobs(t *testing.T) {

// 	os.Chdir("../tests/randomToZip/tests")
// 	a, b := getRootFiles()
// 	c, d := getNonRootFiles()
// 	t.Log("root files\n\n")
// 	for _, i := range a {
// 		t.Log(i)
// 	}
// 	t.Log("root dirs\n\n")
// 	for _, i := range b {
// 		t.Log(i)
// 	}

// 	t.Log("\n\nnon root files\n\n")
// 	for _, i := range c {
// 		t.Log(i)
// 	}

// 	t.Log("\n\nnon root dirs\n\n")
// 	for _, i := range d {
// 		t.Log(i)
// 	}
// }
func TestRandomToZip(t *testing.T) {
	config.DefaultConfig()
	a, _ := filepath.Abs("../tests/randomToZip/tests-1999")
	RandomToZip(
		a,
		"c",
	)

	//undo these changes with `rm -rf tests; git restore tests`
}
