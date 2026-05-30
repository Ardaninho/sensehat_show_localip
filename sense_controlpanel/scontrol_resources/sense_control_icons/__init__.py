#!/usr/bin/env python
# Copyright (C) 2026 Ardaninho

b = [0,0,0]
w = [255,255,255]
r = [255,0,0]
g = [0,255,0]
y = [255,215,0]

iconset = {
    "localip": [
        b,g,g,g,g,g,g,b,
        g,b,b,b,b,b,b,g,
        b,b,g,g,g,g,b,b,
        b,g,b,b,b,b,g,b,
        b,b,b,g,g,b,b,b,
        b,b,g,b,b,g,b,b,
        b,b,b,g,g,b,b,b,
        b,b,b,g,g,b,b,b
    ],
    "publicip": [
        b,r,r,r,r,r,r,b,
        r,b,b,b,b,b,b,r,
        b,b,r,r,r,r,b,b,
        b,r,b,b,b,b,r,b,
        b,b,b,r,r,b,b,b,
        b,b,r,b,b,r,b,b,
        b,b,b,r,r,b,b,b,
        b,b,b,r,r,b,b,b
    ],
    "temperature": [
        b,b,b,w,w,b,b,b,
        b,b,w,r,r,w,b,b,
        b,b,w,r,r,w,b,b,
        b,b,w,r,r,w,b,b,
        b,w,w,r,r,w,w,b,
        b,w,r,r,r,r,w,b,
        b,w,r,r,r,r,w,b,
        b,b,w,w,w,w,b,b
    ],
    "disk": [
        w,w,w,w,w,w,b,b,
        w,b,w,b,w,w,w,b,
        w,b,w,w,w,w,b,w,
        w,b,b,b,b,b,b,w,
        w,b,b,b,b,b,b,w,
        w,b,b,b,b,b,b,w,
        w,b,b,b,b,b,b,w,
        w,w,w,w,w,w,w,w
    ],
    "ramuse": [
        b,b,b,b,b,b,b,b,
        b,y,b,y,y,b,y,b,
        b,g,g,g,g,g,g,b,
        b,g,g,g,g,g,g,b,
        b,g,g,g,g,g,g,b,
        b,g,g,g,g,g,g,b,
        b,y,b,y,y,b,y,b,
        b,b,b,b,b,b,b,b
    ],
    "poweroff": [
        b,b,b,w,w,b,b,b,
        b,w,b,w,w,b,w,b,
        w,b,b,w,w,b,b,w,
        w,b,b,w,w,b,b,w,
        w,b,b,w,w,b,b,w,
        w,b,b,b,b,b,b,w,
        b,w,b,b,b,b,w,b,
        b,b,w,w,w,w,b,b
    ],
    "reboot": [
        w,b,w,w,w,w,b,b,
        w,w,b,b,b,b,w,b,
        w,w,w,b,b,b,b,w,
        b,b,b,b,b,b,b,w,
        w,b,b,b,b,b,b,w,
        w,b,b,b,b,b,b,w,
        b,w,b,b,b,b,w,b,
        b,b,w,w,w,w,b,b
    ],
    "cross": [
        r,b,b,b,b,b,b,r,
        b,r,b,b,b,b,r,b,
        b,b,r,b,b,r,b,b,
        b,b,b,r,r,b,b,b,
        b,b,b,r,r,b,b,b,
        b,b,r,b,b,r,b,b,
        b,r,b,b,b,b,r,b,
        r,b,b,b,b,b,b,r
    ],
    "checkmark": [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,g,
        b,b,b,b,b,b,g,b,
        b,b,b,b,b,g,b,b,
        g,b,b,b,g,b,b,b,
        b,g,b,g,b,b,b,b,
        b,b,g,b,b,b,b,b
    ]
}