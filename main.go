package main

import (
	"fmt"
	"log"
	"path/filepath"
	"strings"

	"github.com/karmanyaahm/test_organization/commands"
	"github.com/karmanyaahm/test_organization/db"

	"github.com/integrii/flaggy"
	"github.com/karmanyaahm/test_organization/config"
)

var version = "unknown"

var dataPath string
var rootDir string

var randomToZip *flaggy.Subcommand
var randomToZipSortDir string
var div string

var jsonifyEvents *flaggy.Subcommand
var disableRotations bool

var sheetsUpload *flaggy.Subcommand
var scanPath string

func init() {
	flaggy.SetName("Scioly Test Organizer")
	flaggy.SetDescription("example program")

	flaggy.ShowHelpOnUnexpectedEnable()

	//global flags
	flaggy.String(&dataPath, "c", "datapath", "path to data file")
	flaggy.String(&rootDir, "r", "rootdir", "path to organization root")

	randomToZip = flaggy.NewSubcommand("randToZip")
	randomToZip.Description = "Random Files to Zip"
	randomToZip.AddPositionalValue(&randomToZipSortDir, "SortDir", 1, true, "The Directory to Sort")

	jsonifyEvents = flaggy.NewSubcommand("jsonify")
	jsonifyEvents.Description = "Sort tests into per event folders"
	jsonifyEvents.Bool(&disableRotations, "", "norotation", "*Disable* rotation sorting (default enabled)")

	sheetsUpload = flaggy.NewSubcommand("spreadsheet")
	sheetsUpload.Description = "Upload tests to spreadsheet"
	sheetsUpload.AddPositionalValue(&scanPath, "ScanPath", 1, true, "The Directory to scan for tests. This should be at the division level.")

	flaggy.AttachSubcommand(randomToZip, 1)
	flaggy.AttachSubcommand(jsonifyEvents, 1)
	flaggy.AttachSubcommand(sheetsUpload, 1)

	flaggy.SetVersion(version)
	flaggy.Parse()
}

func main() {

	_ = config.Conf()
	db.Reload()

	if dataPath != "" {
		config.DataPath, _ = filepath.Abs(dataPath)
	}
	if rootDir != "" {
		config.RootPath, _ = filepath.Abs(rootDir)
	}

	println("Event List dir: ", config.DataPath)

	if randomToZip.Used {

		randomToZipSortDir, err := filepath.Abs(randomToZipSortDir)
		if err != nil {
			fmt.Println(err)
			flaggy.ShowHelpAndExit("Incorrect Directory to sort")
		}

		fmt.Println("Sort")
		fmt.Println("Directory", randomToZipSortDir)
		if askForConfirmation() {
			commands.RandomToZip(randomToZipSortDir)
		}

	} else if jsonifyEvents.Used {
		commands.JsonifyEvents()
		//	if !disableRotations {
		//			commands.Rotations(div)
		//		}
	} else if sheetsUpload.Used {
		f, e := filepath.Abs(scanPath)
		if e != nil {
			log.Fatalf("Could not properly read path; %s", e)
		}
		commands.ListTests(f)
	} else {
		flaggy.ShowHelpAndExit("Unexpected Command")
	}

}
func askForConfirmation() bool {
	var response string
	fmt.Print("Confirm? [y/n] ")

	_, err := fmt.Scanln(&response)
	if err != nil {
		log.Fatal(err)
	}

	switch strings.ToLower(response) {
	case "y", "yes":
		return true
	case "n", "no":
		return false
	default:
		fmt.Println("I'm sorry but I didn't get what you meant, please type (y)es or (n)o and then press enter:")
		return askForConfirmation()
	}
}
