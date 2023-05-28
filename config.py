#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("8595805"))
    API_HASH = os.environ.get("ca430a2687f7fc25c60e8c83854d29ba")
    BOT_TOKEN = os.environ.get("5157509263:AAHL3qOkw0CS_rEnPvnIFA4hu1_Jikw8ELA") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("1145137954")
    SESSION = os.environ.get("BQCDKV0AVdo4s_A1vrPTk1BXCOKfMoKJYVLkhvhAbhClmlV3o0y_kQqipotUNeh8g_gUr4zfuJhu4ohM9tnSO-1XRftZUpYqiGGGCy1U5ovmTUJrjA6dqziLwk85FJSozA65Voso0_eva-7JJv0tZpaM-ENH4n1yfMRsOhpUOXtAtU56J5LhvM6CuHRxEAMJDC-BeV5XkwgsPt1ihooZJnznfO63c9NuOA7c_hozigtrpSusWKTKBxWHAULta-kYeIhv5b6o46Z9aUZeB-A5zmMXbrxsVUu25FWE_5o_7bitsJ0LcwHtl8WSo4boqLMzncXCBOAZqyQJDvAq3ahggb-SXZP0QAAAAABEQWsiAA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
