#! /usr/bin/env python

import os
import sys


mail_location = os.path.expanduser("~/Mail/")
types = {
    # dictionary: "mail -> list of directories"
    # relative paths from mail_location
}
filters = [
    # mailboxes to hide, relative paths from mail_location
]


def get_addresses(instance):
    if not instance:
        return sorted(os.listdir(mail_location))
    return sorted(list(set(os.listdir(mail_location)) & set(types[instance])))


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
    inst = None
    if len(sys.argv) > 1:
        inst = sys.argv[1]
    print format(get_maildirs(get_addresses(inst)))
