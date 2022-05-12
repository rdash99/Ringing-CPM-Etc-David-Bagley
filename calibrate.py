from node import BellNode
import sys
import time
import serial.tools.list_ports as serial


def calibrate():
    ports = serial.comports()
    for port in ports:
        print(port)


calibrate()
"""Scan all connected serial ports and create a node for each one to allow for calibrarion of which bell is which port."""
