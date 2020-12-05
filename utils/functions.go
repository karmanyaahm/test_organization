package utils

import (
	"regexp"
	"errors"

	"github.com/karmanyaahm/test_organization/models"
)

//FindEventByName finds event by exact name
func FindEventByName(eventlist []models.Event, name string) (models.Event, error) {
	for _, i := range eventlist {
		if i.Name == name {
			return i, nil
		}
	}
	return models.Event{}, errors.New("Not Found")

}

//FindEventByFuzzyName finds events by approx name or id
func FindEventByFuzzyName(eventlist []models.Event, val string) (models.Event, error) {
	ans := make([]models.Event, 0, 2)

	for _, event := range eventlist {
		for _, id := range event.GetIds() {
			regex := "(?:[0-9]|\\b|_)(" + id + ")(?:[0-9]|\\b|_)"

			re := regexp.MustCompile(regex)
			 if len(re.FindStringSubmatch(val))>0{
				 ans = append(ans, event)
				 break
			 }
		}
	}

	if len(ans) == 0 {
		return models.Event{}, errors.New("Not Found")
	} else if len(ans) <= 2 {
		return ans[0], nil
	} else {
		return ans[0], errors.New("Too Many")
	}
}
