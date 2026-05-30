#!/usr/bin/env python
# Copyright (C) 2026 Ardaninho

from scontrol_resources import sense_control_icons
from sense_hat import SenseHat
import time
sense=SenseHat()

for i in sense_control_icons.iconset.values():
    sense.set_pixels(i)
    time.sleep(1)
sense.clear()