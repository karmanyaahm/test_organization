#! /usr/bin/env python3.8

from __future__ import unicode_literals
import os

if os.name == "nt":
    print("use a real posix OS like mac or linux or bsd or something")
    exit(69)

from yaml import load, FullLoader
from datetime import date
from realcode.mvc import mvc


class mainInfo:
    root = os.path.dirname(os.path.realpath(__file__))
    next_year = date.today().year + 2
    config = load(open(root + "/config.yml", "r"), Loader=FullLoader)
    blocklistfile = root + "/data/testtrade.yml"
    eventlistfile = root + "/data/event_list.yml"
    pat1 = "(?:[0-9]|\\b|_)("
    pat2 = ")(?:[0-9]|\\b|_)"
    similarity_conf = config["similarity_conf"]
    spreadsheet_id = config["spreadsheet_id"]
    maindir = config["maindir"]
    start = maindir + "/tests/"
    wd = maindir + "/random/"
    locations = []


main_info = mainInfo()


def main():
    thismvc = mvc(main_info, main_info.config["ui"])
    thismvc.start()


if __name__ == "__main__":
    main()


