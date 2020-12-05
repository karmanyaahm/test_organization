# Scioly test scripts



### Note

To get started with this:

* Edit the following variables in main.py - maindir, spreadsheetid
* Follow getting started and set up directory structure and spreadsheet
* follow instructions

1. Platforms:
   * Tested on Arch Linux with Python 3.8
   * Will probably work on any Linux
   * I'm 99% sure this should work on any POSIX OS (mac, bsd, etc)



## Getting Started

### Example directory structure


* random  
  * yet_to_be_sorted_invi-2012
    * absolutely a file from an actual invi  
    * anatomy/  
    * codebusters/  
    * scores.pdf  
* tests  
    * bylocation  
      * good-b  
        * invitational-1985  
          * harvard-1985-forensics-b.zip  
          * harvard-1985-fossils-b.zip  
      * good-c  
        * invitational-1985  
          * harvard-2020-forensics-c.zip  
          * harvard-2020-fossils-c.zip  
    * scripts  
        * File_Organizer.elf.Organizer  
        * credentials.json  
        * config.yml
        * data
          * testtrade.yml
          * event_list.yml  
  
  
### Super Basic Workflow

1. Move invi to random and rename it to `name-year`
2. Run option one in the code(running ./main.py)
3. Move the `name-year` after running option one to bylocation/good-`division`
4. Run option 2 in the code
5. Run option 3 in the code
6. Nice done

### Spreadsheet

To use the spreadsheet feature, you should have a spreadsheet with two sheets 'invis_list-c' and 'invis_list-b'  
You can get the spreadsheet id from the `https://docs.google.com/spreadsheets/d/1EI_McY52x9RBUgShYJZFVzeEW4KCsFKS5ByjgUCFkgM/edit?usp=sharing`
middle part of the spreadsheet url
  
    
      
        

#### Note
* run command like `find ./byevent-c/ -type l -printf "%f\n" |sort` to get list of all tests and then diff by bylocation to find missing 
```
find ./byevent-c/  -maxdepth 2 -type l   -printf "%f\n" |sort > s 
find ./bylocation/good-c/  -maxdepth 2 -type f   -printf "%f\n" |sort > t
diff t s -y |grep '<'
diff t s -y |grep '<' | grep zip |wc -l

rm s t
```
`find ./bylocation/good-c/  -maxdepth 2 -type f   -printf "%f\n" |sort > t ; find ./byevent-c/  -maxdepth 2 -type l   -printf "%f\n" |sort > s ; diff t s -y |grep '<' | grep zip `
