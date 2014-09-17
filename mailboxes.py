#! /usr/bin/env python

import os


mail_location = os.path.expanduser("~/Mail/")
filters = [
    # Directory not list in mutt
    # relative paths from 'mail_location'
    ]


def get_addresses():
    return sorted(os.listdir(mail_location))


def get_maildirs(addresses):
    l = []
    for i in addresses:
        if os.path.isdir(mail_location + i + "/cur"):
            l.append("+" + i)
        else:
            for j in sorted(os.listdir(mail_location + i)):
                if "+" + i + "/" + j not in filters:
                    l.append("+" + i + "/" + j)
    return l


def format(maildirs):
    return " ".join(['"' + x + '"' for x in maildirs])


if __name__ == "__main__":
    print format(get_maildirs(get_addresses()))
