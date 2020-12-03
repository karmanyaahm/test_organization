from __future__ import print_function

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os
import shutil
import difflib
from .functions import getdirs


def sheets_stuff(spreadsheet_id, root):
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    ############### CREDENTIALS ####################
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(root + "/token.pickle"):
        with open(root + "/token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                root + "/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(root + "/token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("sheets", "v4", credentials=creds)
    return service.spreadsheets().values()


def getinvis(div):
    a = os.getcwd()
    os.chdir(f"../organized_by_invitational-{div}")
    dirs = [ddir[2:] for ddir in getdirs()]
    os.chdir(a)
    # got list of invis

    dirs = [this.split("-") for this in dirs]
    oldest = 210000000
    for d, f in dirs:
        oldest = min(int(f), int(oldest))
    # found the oldest test, dirs are now split by '-'

    invis = sorted(list(set([d[0] for d in dirs])))
    # get list of unique invis by name only
    return invis, oldest, dirs


def diff(og, write):
    for line in difflib.unified_diff(
        [",".join(line) for line in og],
        [",".join(line) for line in write],
        fromfile="old",
        tofile="new",
        lineterm="",
        n=0,
    ):
        for prefix in ("---", "+++", "@@"):
            if line.startswith(prefix):
                break
        else:
            print(line,)


class NotBlockedException(Exception):
    pass


def getNumber(blocklist, yr, line):
    # for event, years in blocked[div].items():
    #     if event in invis:
    #         for k in write:
    #             if k[0] == event:
    #                 k[1] = k[1] - years

    # for i in write.copy():
    #     if len(i[1]) == 0:
    #         write.remove(i)
    block = blocklist.blocked[div]
    public = blocklist.public[div]
    event = line[0]

    if event in block.keys():
        if yr in block[event]:
            return "b"
    if event in public.keys():
        if yr in public[event]:
            return "p"
    if yr in line[1]:
        return 1
    return 0


def main( main_info, blocked):
    cwd = os.getcwd()
    spreadsheet_id = main_info.spreadsheet_id
    next_year = main_info.next_year
    root = main_info.root

    spreadsheetValuesObject = sheets_stuff(spreadsheet_id, root)
    global div
    for div in ["b", "c"]:
        #########################################################
        invis, oldest, dirs = getinvis(div)
        write = []

        for i in invis:
            arr = []
            for d in dirs:
                if d[0] == i:
                    arr.append(int(d[1]))
            write.append([i, set(arr)])
        # getting list of years for each invi

        for n, w in enumerate(write):
            arr = []
            for i in range(oldest, next_year):
                arr.append(getNumber(blocked, i, w,))
            write[n] = [w[0]] + list(arr)
        # get list of years in order

        write.insert(0, ["invi"] + list(range(oldest, next_year)))

        write = [[str(ww) for ww in w] for w in write]

        #########################################################
        print(div)

        range_name = f"'invis_list-{div}'!A1:Z100"

        result = spreadsheetValuesObject.get(
            spreadsheetId=spreadsheet_id, range=range_name
        ).execute()
        og = result.get("values", [])
        print("get")

        new = write.copy()
        new.extend([[""] * 26] * (100 - len(new)))
        new = [line + [""] * (26 - len(line)) for line in new]

        og.extend([[""] * 26] * (100 - len(og)))
        og = [line + [""] * (26 - len(line)) for line in og]

        key = {
            "1": "exists in my collection",
            "0": "does not exist in my collection",
            "p": "public afaik (please contact me if you know otherwise)",
            "b": "blocked and cannot post afaik (please contact me if you know otherwise), maybe have",
        }
        for n, hhh in enumerate(key.items()):
            new[2 + n][len(write[0]) + 2] = hhh[0]
            new[2 + n][len(write[0]) + 3] = hhh[1]

        if new != og:
            result = spreadsheetValuesObject.update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption="RAW",
                body={"values": new},
            ).execute()
            print("write")

        print(",".join([str(i)[2:] for i in write[0][1:]]))

        diff(og, new)
    os.chdir(cwd)


# if __name__ == "__main__":
#     from event_list import get_blocked
#     from ..main import next_year, spreadsheet_id,start,blocklistfile
#     blocked = get_blocked(blocklistfile)
#     start = start + 'bylocation/'
#     main(start,spreadsheet_id,next_year,blocked)
