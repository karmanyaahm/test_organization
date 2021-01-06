package main

import (
	"fmt"
	"log"
	"path/filepath"
	"strings"

	"github.com/karmanyaahm/test_organization/commands"

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
	randomToZip.AddPositionalValue(&div, "Division", 2, true, "b or c")

	jsonifyEvents = flaggy.NewSubcommand("jsonify")
	jsonifyEvents.Description = "Sort tests into per event folders"
	jsonifyEvents.Bool(&disableRotations, "", "norotation", "*Disable* rotation sorting (default enabled)")

	flaggy.AttachSubcommand(randomToZip, 1)
	flaggy.AttachSubcommand(jsonifyEvents, 1)

	flaggy.SetVersion(version)
	flaggy.Parse()
}

func main() {

	_ = config.Conf()

	if dataPath != "" {
		config.DataPath, _ = filepath.Abs(dataPath)
	}
	if rootDir != "" {
		config.RootPath, _ = filepath.Abs(rootDir)
	}

	println("Event List dir: ", config.DataPath)

	if randomToZip.Used {

		if div == "c" || div == "C" {
			div = "c"
		} else if div == "b" || div == "B" {
			div = "b"
		} else {
			flaggy.ShowHelpAndExit("Wrong Division")
		}

		randomToZipSortDir, err := filepath.Abs(randomToZipSortDir)
		if err != nil {
			fmt.Println(err)
			flaggy.ShowHelpAndExit("Incorrect Directory to sort")
		}

		fmt.Println("Sort")
		fmt.Println("Directory", randomToZipSortDir)
		fmt.Println("Division", div)
		if askForConfirmation() {
			commands.RandomToZip(randomToZipSortDir, div)
		}

	} else if jsonifyEvents.Used {
		commands.JsonifyEvents()
		//	if !disableRotations {
		//			commands.Rotations(div)
		//		}
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
