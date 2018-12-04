#!/usr/bin/env python
import argparse
import datetime
import os
import shlex
import subprocess


GIT_CMD = "git -C {path} log --all --no-merges --after '{after}' --before '{before}' --pretty=%s {extra}"


def main(path=None, date=None, author=None):

    if date is None:
        date = datetime.datetime.now().date()

    before = after = date

    if path is None:
        path = os.getcwd()

    extra = ""
    if author is not None:
        extra = "--author={}".format(author)

    subprocess.call(shlex.split(GIT_CMD.format(
        path=path,
        after=after.strftime("%Y-%m-%d 00:00"),
        before=before.strftime("%Y-%m-%d 23:59"),
        extra=extra
    )))


def date_type_validate(value):
    return datetime.datetime.strptime(value, "%Y-%m-%d").date()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path")
    parser.add_argument("-d", "--date", type=date_type_validate)
    parser.add_argument("-a", "--author")
    args = parser.parse_args()

    main(args.path, args.date, args.author)
