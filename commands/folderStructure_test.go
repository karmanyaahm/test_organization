package commands

import (
	"path/filepath"
	"testing"

	"github.com/karmanyaahm/test_organization/config"
)

func TestByEvent(t *testing.T) {
	config.DefaultConfig()
	config.RootPath, _ = filepath.Abs("../tests/folderStructure/")

	FolderStructureByEvent("c")
}

func TestRotation(t *testing.T) {

	TestByEvent(t)
	Rotations("c")

}
