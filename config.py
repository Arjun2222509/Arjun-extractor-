#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", ")
    API_ID = int(os.environ.get("API_ID", "20054245"))
    API_HASH = os.environ.get("API_HASH", "431f22f320ed5d69225d3b3fc253fc0d")
    AUTH_USERS = "5034929962"

