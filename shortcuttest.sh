#!/bin/bash
for filename in ../organized_by_event-b/*; do
rclone backend shortcut schoolDrive: scioly/scioly_tests/tests/${filename:3} scioly/testing/$(basename $filename)
	echo scioly/scioly_tests/tests/${filename:3}
done

