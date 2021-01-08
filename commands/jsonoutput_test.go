package commands

import (
	"path/filepath"
	"strings"
	"testing"

	"github.com/karmanyaahm/test_organization/config"
)

func TestByEvent2(t *testing.T) {
	config.DefaultConfig()
	config.RootPath, _ = filepath.Abs("../tests/folderStructure/")

	inpSrc = strings.NewReader(`[ {
    "Path": "c/2021/bearso/anatomy_and_physiology.test",
    "ID": "1Dw4ahXRdDrMtmEY4QsKD2K61wERXphXO"
  },  {
    "Path": "c/2021/bearso/astronomy.test",
    "ID": "19NUYVtwnzAHe7VU1izmzik6OpgSAUZ68"
  }
]`)
	JsonifyEvents()
}

//func TestRotation(t *testing.T) {
//
//	TestByEvent(t)
//	Rotations("c")
//
//}
