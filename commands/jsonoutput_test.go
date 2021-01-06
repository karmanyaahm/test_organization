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

	inpSrc = strings.NewReader(`[
 {
    "Path": "bearso-2021-anatomy_and_physiology-c.test",
    "URL": "https://drive.google.com/drive/folders/1Dw4ahXRdDrMtmEY4QsKD2K61wERXphXO"
  },
  {
    "Path": "bearso-2021-astronomy-c.test",
    "URL": "https://drive.google.com/drive/folders/19NUYVtwnzAHe7VU1izmzik6OpgSAUZ68"
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
