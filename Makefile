testClean:
	git restore tests/
	git reset tests/
	git clean tests/ -f
