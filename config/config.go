package config

import (
	"path/filepath"
	"strings"
)

//Config defines the config attributes
type Config struct {
	Root string
}

var DataPath string
var RootPath string

//Conf returns the config
func Conf() Config {
	config := Config{Root: "a"}
	DataPath = "/run/media/karmanyaahm/scioly/oldstff/tests/code/data/event_list.yml"
	RootPath = "/run/media/karmanyaahm/scioly/oldstff/tests"
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
