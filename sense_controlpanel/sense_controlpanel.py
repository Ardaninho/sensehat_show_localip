#!/usr/bin/env python
# Copyright (C) 2026 Ardaninho

# required libs
from sense_hat import SenseHat
from scontrol_resources import sense_control_icons
from scontrol_resources import sense_control_show_ip
from gpiozero import CPUTemperature
from threading import Thread
import shutil
import psutil
import time
import os

# vars
sense = SenseHat()
cpu = CPUTemperature()
icons = list(sense_control_icons.iconset.keys())
n_option = 0
mode = "menu"
pending_action = None
confirm_index = 0

# funcs
def exec_option(opt):
    sense.clear()
    if opt == "ramuse":
        ram = psutil.virtual_memory()
        sense.show_message(str(ram.percent)+ "% | "+str(round(ram.used/1e9,2))+"GB/"+str(round(ram.total/1e9,2))+"GB", 0.05)
    elif opt == "localip":
        sense.show_message(sense_control_show_ip.getlocalip(), 0.05)
    elif opt == "publicip":
        sense.show_message(sense_control_show_ip.getpublicip(), 0.05)
    elif opt == "temperature":
        sense.show_message(str(round(cpu.temperature))+" C", 0.05)
    elif opt == "disk":
        # using GB instead of GiB
        total, used, free = shutil.disk_usage("/")
        vtotal = total/(10**9)
        vused = used/(10**9) 
        sense.show_message(str(round(used/total*100))+"% | "+str(round(vused,0))+"GB/"+str(round(vtotal,0))+"GB", 0.05)
    elif opt == "poweroff":
        sense.clear()
        os.system("poweroff")
    elif opt == "reboot":
        sense.clear()
        os.system("reboot")

def on_joystick_push(event):
    global n_option, mode, pending_action, confirm_index
    if event.action != "released":
        return
    if mode == "menu":
        if event.direction == "left" and n_option > 0:
            n_option -= 1
        elif event.direction == "right" and n_option < len(icons) -3:
            n_option += 1
        elif event.direction == "middle":
            selected = icons[n_option]
            if selected in ["poweroff", "reboot"]:
                mode = "confirm"
                pending_action = selected
                confirm_index = 0
                sense.set_pixels(sense_control_icons.iconset["cross"])
                return
            else:
                exec_option(icons[n_option])
                sense.clear()
        sense.set_pixels(sense_control_icons.iconset[icons[n_option]])
    else:
        if event.direction == "left":
            confirm_index = 0
            sense.set_pixels(sense_control_icons.iconset["cross"])
        elif event.direction == "right":
            confirm_index = 1
            sense.set_pixels(sense_control_icons.iconset["checkmark"])
        elif event.direction == "middle":
            if confirm_index == 1:
                exec_option(pending_action)
            mode = "menu"
            pending_action = None
            sense.set_pixels(sense_control_icons.iconset[icons[n_option]])

# main
sense.clear()
sense.stick.direction_any = on_joystick_push
while True: pass