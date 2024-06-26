import tkinter as tk
import serial
import glob
from sys import platform
import time

import env

ser = 0

if __name__ =="__main__":
    window = tk.Tk()
    window.title("Hand Control")
    window.geometry('650x500')

    devices = []

    # connect to USB ISS Serial port
    if platform == "linux" or platform == "linux2":
        # linux
        print("Linux not supported at the moment!")
    elif platform == "darwin":
        # OS X
        devices = glob.glob("/dev/cu.*")
    elif platform == "win32":
        # Windows
        for port in list(serial.tools.list_ports.comports()): # create a list of com ['COM1','COM2']
            devices += [port.device]

    usb_iss_label = tk.Label(text="USB ISS Serial port", width=20)
    usb_iss_label.grid(row=0, column=3)

    usb_iss = tk.StringVar()
    port_options = tk.OptionMenu(window, usb_iss, *devices)
    port_options.config(width=20)
    port_options.grid(row=1, column=3)

    connect_button = tk.Button(
        text="Connect",
        width=8,
        height=3,
        bg="white",
        fg="black",
        )

    connect_button.grid(row=2, column=3)

    connection_label = tk.Label(
        text="Not connected",
        fg="white",
        bg="black",
        width=10
    )

    connection_label.grid(row=3, column=3)

    def connect_click(event):
        global ser
        ser = serial.Serial(usb_iss.get())
        ser.close()
        ser.open()
        if ser.isOpen():
            connection_label.config(text="Connected", fg="white", bg="green")

    connect_button.bind("<Button-1>", connect_click)



    # FINGERS MENU

    # THUMB
    thumb_is_selected = tk.IntVar()
    thumb_checkbox = tk.Checkbutton(window, variable = thumb_is_selected, onvalue = 1, offvalue = 0);
    thumb_checkbox.grid(row=5, column=1)

    thumb_label = tk.Label(text="Thumb",width=10)
    thumb_label.grid(row=6, column=1)

    thumb_entry = tk.Entry(width=10)
    thumb_entry.insert(0, "Degress")
    thumb_entry.grid(row=7, column=1)

    # INDEX
    index_is_selected = tk.IntVar()
    index_checkbox = tk.Checkbutton(window, variable = index_is_selected, onvalue = 1, offvalue = 0);
    index_checkbox.grid(row=5, column=2)

    index_label = tk.Label(text="Index",width=10)
    index_label.grid(row=6, column=2)

    index_entry = tk.Entry(width=10)
    index_entry.insert(0, "Degrees")
    index_entry.grid(row=7, column=2)

    # MIDDLE
    middle_is_selected = tk.IntVar()
    middle_checkbox = tk.Checkbutton(window, variable = middle_is_selected, onvalue = 1, offvalue = 0);
    middle_checkbox.grid(row=5, column=3)

    middle_label = tk.Label(text="Middle",width=10)
    middle_label.grid(row=6, column=3)

    middle_entry = tk.Entry(width=10)
    middle_entry.insert(0, "Degrees")
    middle_entry.grid(row=7, column=3)

    # RING
    ring_is_selected = tk.IntVar()
    ring_checkbox = tk.Checkbutton(window, variable = ring_is_selected, onvalue = 1, offvalue = 0);
    ring_checkbox.grid(row=5, column=4)

    ring_label = tk.Label(text="Ring",width=10)
    ring_label.grid(row=6, column=4)

    ring_entry = tk.Entry(width=10)
    ring_entry.insert(0, "Degrees")
    ring_entry.grid(row=7, column=4)

    # PINKY
    pinky_is_selected = tk.IntVar()
    pinky_checkbox = tk.Checkbutton(window, variable = pinky_is_selected, onvalue = 1, offvalue = 0);
    pinky_checkbox.grid(row=5, column=5)

    pinky_label = tk.Label(text="Pinky",width=10)
    pinky_label.grid(row=6, column=5)

    pinky_entry = tk.Entry(width=10)
    pinky_entry.insert(0, "Degrees")
    pinky_entry.grid(row=7, column=5)


    move_button = tk.Button(
        text="Move fingers",
        width=8,
        height=3,
        bg="white",
        fg="black",
        )

    move_button.grid(row=8, column=3)

    def move_thumb(degrees):
        if (degrees < 0 or degrees > 90):
            return

        global ser
        position = env.MIN_POS_THUMB + int((env.MAX_POS_THUMB - env.MIN_POS_THUMB) * (degrees / 90))
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x34\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    def move_index(degrees):
        if (degrees < 0 or degrees > 90):
            return

        global ser
        position = env.MIN_POS_INDEX + int((env.MAX_POS_INDEX - env.MIN_POS_INDEX) * (degrees / 90))
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x36\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    def move_middle(degrees):
        if (degrees < 0 or degrees > 90):
            return

        global ser
        position = env.MIN_POS_MIDDLE + int((env.MAX_POS_MIDDLE - env.MIN_POS_MIDDLE) * (degrees / 90))
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x38\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    def move_ring(degrees):
        if (degrees < 0 or degrees > 90):
            return

        global ser
        position = env.MIN_POS_RING + int((env.MAX_POS_RING - env.MIN_POS_RING) * (degrees / 90))
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x3A\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    def move_pinky(degrees):
        if (degrees < 0 or degrees > 90):
            return

        global ser
        position = env.MIN_POS_PINKY + int((env.MAX_POS_PINKY - env.MIN_POS_PINKY) * (degrees / 90))
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x3C\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))


    def move_click(event):
        if thumb_is_selected.get():
            move_thumb(int(thumb_entry.get()))
            time.sleep(0.5)

        if index_is_selected.get():
            move_index(int(index_entry.get()))
            time.sleep(0.5)

        if middle_is_selected.get():
            move_middle(int(middle_entry.get()))
            time.sleep(0.5)

        if ring_is_selected.get():
            move_ring(int(ring_entry.get()))
            time.sleep(0.5)

        if pinky_is_selected.get():
            move_pinky(int(pinky_entry.get()))
            time.sleep(0.5)


    move_button.bind("<Button-1>", move_click)

#########################

    # EXTEND FINGERS
    extend_button = tk.Button(
        text="Extend",
        width=8,
        height=3,
        bg="white",
        fg="black",
        )

    extend_button.grid(row=9, column=3)

    def extend_thumb():
        global ser
        ser.write(env.commands["thumb"]["extend"])

    def extend_index():
        global ser
        ser.write(env.commands["index"]["extend"])

    def extend_middle():
        global ser
        ser.write(env.commands["middle"]["extend"])

    def extend_ring():
        global ser
        ser.write(env.commands["ring"]["extend"])

    def extend_pinky():
        global ser
        ser.write(env.commands["pinky"]["extend"])

    def extend_click(event):
        if thumb_is_selected.get():
            extend_thumb()
            time.sleep(0.5)

        if index_is_selected.get():
            extend_index()
            time.sleep(0.5)

        if middle_is_selected.get():
            extend_middle()
            time.sleep(0.5)

        if ring_is_selected.get():
            extend_ring()
            time.sleep(0.5)

        if pinky_is_selected.get():
            extend_pinky()
            time.sleep(0.5)

    extend_button.bind("<Button-1>", extend_click)


    # BEND FINGERS
    bend_button = tk.Button(
        text="Bend",
        width=8,
        height=3,
        bg="white",
        fg="black",
        )

    bend_button.grid(row=10, column=3)

    def bend_thumb():
        global ser
        ser.write(env.commands["thumb"]["bend"])

    def bend_index():
        global ser
        ser.write(env.commands["index"]["bend"])

    def bend_middle():
        global ser
        ser.write(env.commands["middle"]["bend"])
    
    def bend_ring():
        global ser
        ser.write(env.commands["ring"]["bend"])

    def bend_pinky():
        global ser
        ser.write(env.commands["pinky"]["bend"])


    def bend_click(event):
        if thumb_is_selected.get():
            bend_thumb()
            time.sleep(0.5)

        if index_is_selected.get():
            bend_index()
            time.sleep(0.5)

        if middle_is_selected.get():
            bend_middle()
            time.sleep(0.5)

        if ring_is_selected.get():
            bend_ring()
            time.sleep(0.5)

        if pinky_is_selected.get():
            bend_pinky()
            time.sleep(0.5)


    bend_button.bind("<Button-1>", bend_click)

    window.mainloop()