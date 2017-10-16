# Control multiple photon neopixels subscribed to different events
# Uses a GUI to select which photon should be commanded and then allows
# changing of the mode, brightness, and RGB

import tkinter

photon_events = {'TV Room': 'chtapodi',
                 'Theo Room': 'chtapodi',
                 }

