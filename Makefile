flags = CGO_ENABLED=0 
targ = builds/test_organization_
ldflags = -ldflags="-s" 
#ldflag -w ?
upx_command = echo 
#MAKEFLAGS += -Otarget

all: linux_amd64 linux_arm64 linux_i386 mac_arm64 mac_amd64

release:
	$(MAKE) test
	$(MAKE) clean
	pkger 
	$(MAKE) upx all -Otarget
	$(MAKE) checksum
testClean:
	git restore tests/
	git reset tests/
	git clean tests/ -f

test:
	go test ./... -coverprofile=c.out
	@$(MAKE) testClean

amd64:
	$(flags) GOARCH=amd64 go build -o $(targ)amd64 .
upx:
	$(eval upx_command=upx $(targ))
checksum:
	cd builds; \
	  sha256sum * > sha256.txt

linux_amd64:
	$(flags) GOARCH=amd64 GOOS=linux go build $(ldflags) -o $(targ)$@ .
	$(upx_command)$@
linux_arm64:
	$(flags) GOARCH=arm64 GOOS=linux go build $(ldflags) -o $(targ)$@      .
	$(upx_command)$@
linux_i386:
	$(flags) GOARCH=386 GOOS=linux go build $(ldflags) -o $(targ)$@      .
	$(upx_command)$@
mac_arm64:
	#$(flags) GOARCH=arm64 GOOS=darwin go build $(ldflags) -o $(targ)$@ .
	#$(upx_command)$@
mac_amd64:
	$(flags) GOARCH=amd64 GOOS=darwin go build $(ldflags) -o $(targ)$@ .
	$(upx_command)$@
clean:
	rm -rf builds/
	go clean


