package main

import (
	"config"
	"db"
	"fmt"
)

func main() {

	myConfig := config.Conf()
	fmt.Println(myConfig.Root)
	db.Load('a', 'b')
}
