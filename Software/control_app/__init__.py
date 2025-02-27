import tkinter as tk
import serial
from serial.tools import list_ports
import glob
from sys import platform
import time

extend_thumb = b'\x55\x34\x04\x01\x02'
bend_thumb = b'\x55\x34\x04\x01\x01'

extend_index = b'\x55\x36\x04\x01\x02'
bend_index = b'\x55\x36\x04\x01\x01'

extend_middle = b'\x55\x38\x04\x01\x02'
bend_middle = b'\x55\x38\x04\x01\x01'

extend_ring = b'\x55\x3A\x04\x01\x02'
bend_ring = b'\x55\x3A\x04\x01\x01'

extend_pinky = b'\x55\x3C\x04\x01\x02'
bend_pinky = b'\x55\x3C\x04\x01\x01'

commands = {}
commands["thumb"] = {}
commands["thumb"]["extend"] = extend_thumb
commands["thumb"]["bend"] = bend_thumb

commands["index"] = {}
commands["index"]["extend"] = extend_index
commands["index"]["bend"] = bend_index

commands["middle"] = {}
commands["middle"]["extend"] = extend_middle
commands["middle"]["bend"] = bend_middle

commands["ring"] = {}
commands["ring"]["extend"] = extend_ring
commands["ring"]["bend"] = bend_ring

commands["pinky"] = {}
commands["pinky"]["extend"] = extend_pinky
commands["pinky"]["bend"] = bend_pinky

MAX_POS_THUMB = 655
MIN_POS_THUMB = 377

MAX_POS_INDEX = 649
MIN_POS_INDEX = 250

MAX_POS_MIDDLE = 650
MIN_POS_MIDDLE = 295

MAX_POS_RING = 650
MIN_POS_RING = 265

MAX_POS_PINKY = 662
MIN_POS_PINKY = 300

ser = 0

if __name__ =="__main__":
    window = tk.Tk()
    window.title("Hand Control")
    window.geometry('500x400')

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
    port_options = tk.OptionMenu(window, usb_iss, 'COM1', *devices)
    port_options.config(width=20)
    port_options.grid(row=1, column=3)

    # Open serial open
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
        ser.open()
        if ser.isOpen():
            connection_label.config(text="Connected", fg="white", bg="green")

    connect_button.bind("<Button-1>", connect_click)

    # Close serial port
    close_button = tk.Button(
        text="Close",
        width=8,
        height=3,
        bg="white",
        fg="black",
        )

    close_button.grid(row=2, column=4)

    def close_click(event):
        global ser
        if ser.isOpen():
            ser.close()
            connection_label.config(text="Not Connected", fg="white", bg="black")

    close_button.bind("<Button-1>", close_click)

    # FINGERS MENU

    # THUMB
    thumb_is_selected = tk.IntVar()
    thumb_checkbox = tk.Checkbutton(window, variable = thumb_is_selected, onvalue = 1, offvalue = 0);
    thumb_checkbox.grid(row=5, column=1)

    thumb_label = tk.Label(text="Thumb",width=10)
    thumb_label.grid(row=6, column=1)

    thumb_entry = tk.Entry(width=10)
    thumb_entry.insert(0, "Position")
    thumb_entry.grid(row=7, column=1)

    # INDEX
    index_is_selected = tk.IntVar()
    index_checkbox = tk.Checkbutton(window, variable = index_is_selected, onvalue = 1, offvalue = 0);
    index_checkbox.grid(row=5, column=2)

    index_label = tk.Label(text="Index",width=10)
    index_label.grid(row=6, column=2)

    index_entry = tk.Entry(width=10)
    index_entry.insert(0, "Position")
    index_entry.grid(row=7, column=2)

    # MIDDLE
    middle_is_selected = tk.IntVar()
    middle_checkbox = tk.Checkbutton(window, variable = middle_is_selected, onvalue = 1, offvalue = 0);
    middle_checkbox.grid(row=5, column=3)

    middle_label = tk.Label(text="Middle",width=10)
    middle_label.grid(row=6, column=3)

    middle_entry = tk.Entry(width=10)
    middle_entry.insert(0, "Position")
    middle_entry.grid(row=7, column=3)

    # RING
    ring_is_selected = tk.IntVar()
    ring_checkbox = tk.Checkbutton(window, variable = ring_is_selected, onvalue = 1, offvalue = 0);
    ring_checkbox.grid(row=5, column=4)

    ring_label = tk.Label(text="Ring",width=10)
    ring_label.grid(row=6, column=4)

    ring_entry = tk.Entry(width=10)
    ring_entry.insert(0, "Position")
    ring_entry.grid(row=7, column=4)

    # PINKY
    pinky_is_selected = tk.IntVar()
    pinky_checkbox = tk.Checkbutton(window, variable = pinky_is_selected, onvalue = 1, offvalue = 0);
    pinky_checkbox.grid(row=5, column=5)

    pinky_label = tk.Label(text="Pinky",width=10)
    pinky_label.grid(row=6, column=5)

    pinky_entry = tk.Entry(width=10)
    pinky_entry.insert(0, "Position")
    pinky_entry.grid(row=7, column=5)

    empty_label = tk.Label(text="",width=10)
    empty_label.grid(row=10, column=3)

    move_button = tk.Button(
        text="Move fingers",
        width=10,
        height=3,
        bg="white",
        fg="black",
        )

    move_button.grid(row=11, column=3)

    def move_thumb(position):
        if (position < MIN_POS_THUMB or position > MAX_POS_THUMB):
            return

        global ser
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x34\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    def move_index(position):
        if (position < MIN_POS_INDEX or position > MAX_POS_INDEX):
            return

        global ser

        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x36\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    def move_middle(position):
        if (position < MIN_POS_MIDDLE or position > MAX_POS_MIDDLE):
            return

        global ser
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x38\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    def move_ring(position):
        if (position < MIN_POS_RING or position > MAX_POS_RING):
            return

        global ser
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x3A\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    def move_pinky(position):
        if (position < MIN_POS_PINKY or position > MAX_POS_PINKY):
            return

        global ser
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

    extend_button.grid(row=11, column=4)

    def extend_thumb():
        global ser
        ser.write(commands["thumb"]["extend"])

    def extend_index():
        global ser
        ser.write(commands["index"]["extend"])

    def extend_middle():
        global ser
        ser.write(commands["middle"]["extend"])

    def extend_ring():
        global ser
        ser.write(commands["ring"]["extend"])

    def extend_pinky():
        global ser
        ser.write(commands["pinky"]["extend"])

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

    bend_button.grid(row=11, column=2)

    def bend_thumb():
        global ser
        ser.write(commands["thumb"]["bend"])

    def bend_index():
        global ser
        ser.write(commands["index"]["bend"])

    def bend_middle():
        global ser
        ser.write(commands["middle"]["bend"])

    def bend_ring():
        global ser
        ser.write(commands["ring"]["bend"])

    def bend_pinky():
        global ser
        ser.write(commands["pinky"]["bend"])


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