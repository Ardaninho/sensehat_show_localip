#!/usr/bin/env python
# Copyright (C) 2026 Ardaninho
from sense_hat import SenseHat
sense = SenseHat()
import netifaces
idevice = "eth0"

local_ip = netifaces.ifaddresses(idevice)[netifaces.AF_INET][0]["addr"]
sense.show_message("IP: " + local_ip)   

while True:
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        sense.show_message("IP: " + local_ip)