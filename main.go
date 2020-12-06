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

var randomToZip *flaggy.Subcommand
var randomToZipSortDir string
var randomToZipDiv string

func init() {
	flaggy.SetName("Scioly Test Organizer")
	flaggy.SetDescription("example program")

	flaggy.ShowHelpOnUnexpectedEnable()

	//global flags
	flaggy.String(&dataPath, "d", "datapath", "path to data file")

	randomToZip = flaggy.NewSubcommand("randToZip")
	randomToZip.Description = "Random Files to Zip"
	randomToZip.AddPositionalValue(&randomToZipSortDir, "SortDir", 1, true, "The Directory to Sort")
	randomToZip.AddPositionalValue(&randomToZipDiv, "Division", 2, true, "b or c")

	flaggy.AttachSubcommand(randomToZip, 1)

	flaggy.SetVersion(version)
	flaggy.Parse()
}

func main() {

	_ = config.Conf()

	if dataPath != "" {
		config.DataPath, _ = filepath.Abs(dataPath)
	}
	fmt.Println("Even List dir: ", config.DataPath)

	if randomToZip.Used {
		randomToZipSortDir, err := filepath.Abs(randomToZipSortDir)
		if err != nil {
			fmt.Println(err)
			flaggy.ShowHelpAndExit("Incorrect Directory to sort")
		}
		if randomToZipDiv == "c" || randomToZipDiv == "C" {
			randomToZipDiv = "c"
		} else if randomToZipDiv == "b" || randomToZipDiv == "B" {
			randomToZipDiv = "b"
		} else {
			flaggy.ShowHelpAndExit("Wrong Division")
		}

		fmt.Println("Sort")
		fmt.Println("Directory", randomToZipSortDir)
		fmt.Println("Division", randomToZipDiv)
		if askForConfirmation() {
			commands.RandomToZip(randomToZipSortDir, randomToZipDiv)
		}

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
