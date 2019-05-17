#!/usr/local/bin/python3

"""
This module parses config file
"""

import json

with open("/app/config.json") as fp:
    config = json.load(fp)