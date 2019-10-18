#!/usr/local/bin/python3

from config_parser import config


def get_filename():
    try:
        filename = config["filename"]
    except KeyError:
        filename = 'inf'
    return filename


if __name__ == '__main__':
    print(get_filename(), end='')
