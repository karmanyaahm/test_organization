package config


//Config defines the config attributes
type Config struct {
	Root string
}

var DataPath string

//Conf returns the config
func Conf() Config {
	config := Config{Root: "a"}
	DataPath = "/run/media/karmanyaahm/scioly/oldstff/tests/code/data/event_list.yml"
	return config

	// var configPath string
	// flag.StringVar(&configPath, "config.yml path", "./config.yml", "path to configuration file")

	// flag.Parse()

	// fmt.Println("word:", configPath)

}
