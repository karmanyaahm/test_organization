# Scioly test scripts

1. Basic user interface is ready

To get started with this:

* run main.py
* follow instructions

2. Platforms:
   * Tested on Arch Linux with Python 3.8
   * Will probably work on any Linux
   * I'm 99% sure this should work on any POSIX OS (mac, bsd, etc)








### Note
**credentials.json contains secrets that can access my account and I'm trusting everyone who has access to this repo to not misuse it also token.pickle contains secrets that can access the account that the is signed in when running listinvis but that should automatically just stay on your computer and should not be uploaded**
* run command like `find ./byevent-c/ -type l -printf "%f\n" |sort` to get list of all tests and then diff by bylocation to find missing 
```
find ./byevent-c/  -maxdepth 2 -type l   -printf "%f\n" |sort > s 
find ./bylocation/good-c/  -maxdepth 2 -type f   -printf "%f\n" |sort > t
diff t s -y |grep '<'
diff t s -y |grep '<' | grep zip |wc -l

rm s t
```
`find ./bylocation/good-c/  -maxdepth 2 -type f   -printf "%f\n" |sort > t ; find ./byevent-c/  -maxdepth 2 -type l   -printf "%f\n" |sort > s ; diff t s -y |grep '<' | grep zip `