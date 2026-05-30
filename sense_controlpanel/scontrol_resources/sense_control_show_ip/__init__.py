#!/usr/bin/env python
# Copyright (C) 2026 Ardaninho

import netifaces
import requests

def getlocalip():
    idevice = "eth0"
    local_ip = netifaces.ifaddresses(idevice)[netifaces.AF_INET][0]["addr"]
    return local_ip

def getpublicip():
    public_ip = requests.get("https://checkip.amazonaws.com")
    return public_ip.text.replace("\n","")