package commands

import (
	"os"

	"github.com/karmanyaahm/test_organization/models"
)

func RandomToZip(wd string, div byte, eventlist []models.Event) error {
	cwd, _ := os.Getwd()
	defer os.Chdir(cwd)
	os.Chdir(wd)

	//glob all files depth 1 or files and dirs depth 2
	//identify events
	//create event folders
	//move files to directories
	
	return nil
}
