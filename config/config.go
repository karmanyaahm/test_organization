package config

import (
	"os"
	"path/filepath"
	"strings"
)

//Config defines the config attributes
type Config struct {
	Root string
}

var DataPath string
var RootPath string
var CallPath string
var InviPath string
var URLPrefix string

//Conf returns the config
func Conf() Config {
	config := Config{Root: "a"}
	DataPath = "/run/media/karmanyaahm/scioly/oldstff/tests/code/data/event_list.yml"
	RootPath = "/run/media/karmanyaahm/scioly/oldstff/tests"
	InviPath = "/run/media/karmanyaahm/scioly/oldstff/tests/code/data/invitationals.yml"
	URLPrefix = "https://drive.google.com/drive/folders/"
	CallPath, _ = os.Getwd()
	return config

	// var configPath string
	// flag.StringVar(&configPath, "config.yml path", "./config.yml", "path to configuration file")

	// flag.Parse()

	// fmt.Println("word:", configPath)

}
func ByInvitationalPath(div string) string {
	div = strings.ToLower(div)
	return filepath.Join(RootPath, "organized_by_invitational-"+div)
}
func ByEventPath(div string) string {
	div = strings.ToLower(div)
	return filepath.Join(RootPath, "organized_by_event-"+div)
}
