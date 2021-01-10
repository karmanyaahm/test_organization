package commands

import (
	"fmt"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"time"

	"github.com/karmanyaahm/test_organization/config"
	"github.com/karmanyaahm/test_organization/db"
	"github.com/karmanyaahm/test_organization/models"
	"github.com/karmanyaahm/test_organization/sheets"
	"github.com/karmanyaahm/test_organization/utils"
)

var maxYr int = time.Now().AddDate(0, 6, 0).Year()

func ListTests(path string) {
	outputArr := getValues(path)

	sheets.Initialize()
	sheets.DiffAndSend(config.SpreadsheetID, "Copy of invis_list-c", outputArr)
}

func getValues(path string) (outputArr [][]string) {
	valMap := make(map[string]map[int]int, 0)
	glob, err := filepath.Glob(path + "/*/*/*.test")
	check(err)

	for _, i := range glob {
		split := strings.Split(i, "/")
		yr, err := strconv.Atoi(split[len(split)-3])
		check(err)
		loc := split[len(split)-2]
		if len(valMap[loc]) > 0 {
			valMap[loc][yr] += 1
		} else {
			valMap[loc] = map[int]int{}
			valMap[loc][yr] = 1
		}
	}
	minYr := maxYr
	for _, i := range valMap {
		for j := range i {
			if minYr > j {
				minYr = j
			}
		}
	}

	outputArr = outputBuilder(minYr, len(valMap))

	outputInviVals(outputArr, valMap, minYr) //slice outputArr passed by ref
	return
}

func sortedKeys(m map[string]map[int]int) []string {
	keys := make([]string, len(m))
	i := 0
	for k := range m {
		keys[i] = k
		i++
	}
	sort.Strings(keys)
	return keys
}

func outputInviVals(val [][]string, valMap map[string]map[int]int, minYr int) {

	for c, name := range sortedKeys(valMap) {
		yrs := valMap[name]
		event, err := utils.FindInviByName(db.InviList, name)
		if err != nil {
			if err.Error() == "Not Found" {
				event = models.Invi{Name: name}
			}
		}

		row := val[c+1]
		row[0] = event.GetFancyName()

		for i := maxYr; i >= minYr; i-- {
			row[i-minYr+1] = "0"
		}
		for yr, ct := range yrs {
			row[yr-minYr+1] = strconv.Itoa(ct) + event.GetFlags(yr)
		}

	}
}

func outputBuilder(minYr, invis int) [][]string {
	val := make([][]string, invis+1)
	for n := range val {
		val[n] = make([]string, maxYr-minYr+2) //dont run this exactly at new years the two things might mess up lol
	}
	//fmt.Println(len(val))
	//init
	val[0][0] = "invis"
	for i := minYr; i <= maxYr; i++ {
		val[0][i-minYr+1] = strconv.Itoa(i)
	}
	rules := []string{
		">1 exists in my collection",
		"0 does not exist in my collection",
		"p - public afaik (please contact me if you know otherwise)",
		"b - blocked and cannot post afaik (please contact me if you know otherwise), maybe have",
	}
	for n, i := range rules {
		if len(val) >= (5 + n) {
			val[5+n] = append(val[5+n], i)
		} else {
			fmt.Println("too few tests to add instructions")
			break
		}
	}

	return val
}

//func check(err error) {
//	if err != nil {
//		log.Fatal(err)
//	}
//}
