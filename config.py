#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8019668327:AAFfvVgnHJq1nC38WgDh604Wk7B3Mr7x8TE")
    API_ID = int(os.environ.get("API_ID", "22080412"))
    API_HASH = os.environ.get("API_HASH", "17a5b12bb9261b0250d31bbef9c5227f")
    AUTH_USERS = "7587316405"

