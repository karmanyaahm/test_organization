package main

import (
	"github.com/karmanyaahm/test_organization/config"
	"github.com/karmanyaahm/test_organization/db"  
	"fmt"
)
 
func main() {

	myConfig := config.Conf()
	fmt.Println(myConfig.Root)
	db.Load('a', 'b')
}
 