package sheets

import (
	"bytes"
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"

	"github.com/markbates/pkger"
	"github.com/sergi/go-diff/diffmatchpatch"
	"golang.org/x/net/context"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/google"
	"google.golang.org/api/sheets/v4"
)

// Retrieve a token, saves the token, then returns the generated client.
func getClient(config *oauth2.Config) *http.Client {
	// The file token.json stores the user's access and refresh tokens, and is
	// created automatically when the authorization flow completes for the first
	// time.
	tokFile := "token.json"
	tok, err := tokenFromFile(tokFile)
	if err != nil {
		tok = getTokenFromWeb(config)
		saveToken(tokFile, tok)
	}
	return config.Client(context.Background(), tok)
}

// Request a token from the web, then returns the retrieved token.
func getTokenFromWeb(config *oauth2.Config) *oauth2.Token {
	authURL := config.AuthCodeURL("state-token", oauth2.AccessTypeOffline)
	fmt.Printf("Go to the following link in your browser then type the "+
		"authorization code: \n%v\n", authURL)

	var authCode string
	if _, err := fmt.Scan(&authCode); err != nil {
		log.Fatalf("Unable to read authorization code: %v", err)
	}

	tok, err := config.Exchange(context.TODO(), authCode)
	if err != nil {
		log.Println(authCode)
		log.Fatalf("Unable to retrieve token from web: %v", err)
	}
	return tok
}

// Retrieves a token from a local file.
func tokenFromFile(file string) (*oauth2.Token, error) {
	f, err := os.Open(file)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	tok := &oauth2.Token{}
	err = json.NewDecoder(f).Decode(tok)
	return tok, err
}

// Saves a token to a file path.
func saveToken(path string, token *oauth2.Token) {
	fmt.Printf("Saving credential file to: %s\n", path)
	f, err := os.OpenFile(path, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0600)
	if err != nil {
		log.Fatalf("Unable to cache oauth token: %v", err)
	}
	defer f.Close()
	json.NewEncoder(f).Encode(token)
}

var srv *sheets.Service

func Initialize() {
	file, err := pkger.Open("github.com/karmanyaahm/test_organization:/files/credentials.json")
	if err != nil {
		log.Fatalf("Unable to read client secret file: %v", err)
	}
	b, err := ioutil.ReadAll(file)
	if err != nil {
		log.Fatalf("Unable to read client secret file: %v", err)
	}

	// If modifying these scopes, delete your previously saved token.json.
	config, err := google.ConfigFromJSON(b, "https://www.googleapis.com/auth/spreadsheets")
	if err != nil {
		log.Fatalf("Unable to parse client secret file to config: %v", err)
	}
	client := getClient(config)

	srv, err = sheets.New(client)
	if err != nil {
		log.Fatalf("Unable to retrieve Sheets client: %v", err)
	}
}
func get(spreadsheetId, readRange string) [][]interface{} {
	resp, err := srv.Spreadsheets.Values.Get(spreadsheetId, readRange).Do()
	if err != nil {
		log.Fatalf("Unable to retrieve data from sheet: %v", err)
	}
	return resp.Values

}
func write(spreadsheetId string, inp [][]string) {
	var vr sheets.ValueRange

	vr.Values = make([][]interface{}, len(inp))
	for n, in := range inp {
		vr.Values[n] = make([]interface{}, len(in))
		for n2, i := range in {
			vr.Values[n][n2] = i
		}
	}

	_, err := srv.Spreadsheets.Values.Update(spreadsheetId, "Copy of invis_list-c!1:200", &vr).ValueInputOption("USER_ENTERED").Do()
	if err != nil {
		log.Fatal(err)
	}
}

func myDiff(old [][]interface{}, newstr [][]string) bool {
	oldStr := make([][]string, len(old))
	for n, in := range old {
		oldStr[n] = make([]string, len(in))
		for n2, i := range in {
			oldStr[n][n2] = fmt.Sprint(i)
		}
	}

	oldBuf := bytes.NewBuffer([]byte(""))
	newBuf := bytes.NewBuffer([]byte(""))
	newWrite := csv.NewWriter(newBuf)
	oldWrite := csv.NewWriter(oldBuf)
	newWrite.WriteAll(newstr)
	oldWrite.WriteAll(oldStr)
	newWrite.Flush()
	oldWrite.Flush()

	newStrCsv := newBuf.String()
	oldStrCsv := oldBuf.String()

	if newStrCsv != oldStrCsv {
		dmp := diffmatchpatch.New()
		diffs := dmp.DiffMain(oldStrCsv, newStrCsv, false)
		fmt.Println(dmp.DiffPrettyText(diffs))
		return true
	} else {
		fmt.Println("Spreadsheet is up to date")
		return false
	}

}

func DiffAndSend(spreadsheetId, sheetName string, inp [][]string) {

	og := get(spreadsheetId, "Copy of invis_list-c!1:100")
	if myDiff(og, inp) {
		write(spreadsheetId, inp)
	}
}
