import tkinter as tk
import tkinter.messagebox
import serial
import glob
from sys import platform
import time

import env

ser = 0

if __name__ =="__main__":
    window = tk.Tk()
    window.title("Sign language")
    window.geometry('1400x1200')

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

    usb_iss_label = tk.Label(text="USB ISS Serial port", font=("Arial", 30), width=20)
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
        font=('Helvetica', 40),
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
        ser = serial.Serial(usb_iss.get(), baudrate=38400, timeout=0)
        ser.close()
        ser.open()
        if ser.isOpen():
            connection_label.config(text="Connected", fg="white", bg="green")


    connect_button.bind("<Button-1>", connect_click)


#########################

    # EXTEND FINGERS
    extend_button = tk.Button(
        text="Extend",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    extend_button.grid(row=8, column=4)

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
        extend_thumb()
        time.sleep(0.5)

        extend_index()
        time.sleep(0.5)

        extend_middle()
        time.sleep(0.5)

        extend_ring()
        time.sleep(0.5)

        extend_pinky()


    extend_button.bind("<Button-1>", extend_click)


    # BEND FINGERS
    bend_button = tk.Button(
        text="Bend",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    bend_button.grid(row=8, column=2)

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
        bend_thumb()
        time.sleep(0.5)

        bend_index()
        time.sleep(0.5)

        bend_middle()
        time.sleep(0.5)

        bend_ring()
        time.sleep(0.5)

        bend_pinky()


    bend_button.bind("<Button-1>", bend_click)

    # MOVE FINGERS FUNCTIONALITY


    def move_thumb(position):
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
        global ser
        position = hex(position)[2:].zfill(4)
        first, second = position[0:2], position[2:4]
        b = bytearray(b'\x55\x3C\x08\x02')
        # Append second byte to USB ISS command
        b.extend("{}{}".format('\\x', str(second)).encode())
        # Append first byte to USB ISS command
        b.extend("{}{}".format('\\x', str(first)).encode())
        ser.write(b.decode('unicode_escape').encode("raw_unicode_escape"))

    # SIGN LANGUAGE MENU


    # A
    letter_a = tk.Button(
        text="A",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_a.grid(row=11, column=0)


    def move_a(event):
        move_index(267)
        time.sleep(0.5)

        move_middle(298)
        time.sleep(0.5)

        move_ring(293)
        time.sleep(0.5)

        move_pinky(386)
        time.sleep(0.5)

        move_thumb(615)
        time.sleep(0.5)


    letter_a.bind("<Button-1>", move_a)

    # B
    letter_b = tk.Button(
        text="B",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_b.grid(row=11, column=1)


    def move_b(event):
        move_thumb(545)
        time.sleep(0.5)

        move_index(645)
        time.sleep(0.5)

        move_middle(650)
        time.sleep(0.5)

        move_ring(650)
        time.sleep(0.5)

        move_pinky(662)
        time.sleep(0.5)


    letter_b.bind("<Button-1>", move_b)

    # C
    letter_c = tk.Button(
        text="C",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_c.grid(row=11, column=2)


    def move_c(event):
        move_thumb(626)
        time.sleep(0.5)

        move_index(530)
        time.sleep(0.5)

        move_middle(541)
        time.sleep(0.5)

        move_ring(563)
        time.sleep(0.5)

        move_pinky(613)
        time.sleep(0.5)


    letter_c.bind("<Button-1>", move_c)

    # D
    letter_d = tk.Button(
        text="D",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_d.grid(row=11, column=3)


    def move_d(event):
        move_thumb(541)
        time.sleep(0.5)

        move_index(641)
        time.sleep(0.5)

        move_middle(442)
        time.sleep(0.5)

        move_ring(463)
        time.sleep(0.5)

        move_pinky(525)
        time.sleep(0.5)


    letter_d.bind("<Button-1>", move_d)

    # E
    letter_e = tk.Button(
        text="E",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_e.grid(row=11, column=4)


    def move_e(event):
        move_thumb(521)
        time.sleep(0.5)

        move_index(441)
        time.sleep(0.5)

        move_middle(442)
        time.sleep(0.5)

        move_ring(461)
        time.sleep(0.5)

        move_pinky(525)
        time.sleep(0.5)


    letter_e.bind("<Button-1>", move_e)

    # F
    letter_f = tk.Button(
        text="F",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_f.grid(row=11, column=5)


    def move_f(event):
        move_thumb(566)
        time.sleep(0.5)

        move_index(418)
        time.sleep(0.5)

        move_middle(648)
        time.sleep(0.5)

        move_ring(650)
        time.sleep(0.5)

        move_pinky(663)
        time.sleep(0.5)


    letter_f.bind("<Button-1>", move_f)

    # G
    letter_g = tk.Button(
        text="G",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_g.grid(row=11, column=6)


    def move_g(event):
        move_thumb(595)
        time.sleep(0.5)

        move_index(645)
        time.sleep(0.5)

        move_middle(414)
        time.sleep(0.5)

        move_ring(435)
        time.sleep(0.5)

        move_pinky(520)
        time.sleep(0.5)


    letter_g.bind("<Button-1>", move_g)

    # H
    letter_h = tk.Button(
        text="H",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_h.grid(row=12, column=0)


    def move_h(event):
        move_thumb(595)
        time.sleep(0.5)

        move_index(645)
        time.sleep(0.5)

        move_middle(650)
        time.sleep(0.5)

        move_ring(435)
        time.sleep(0.5)

        move_pinky(520)
        time.sleep(0.5)


    letter_h.bind("<Button-1>", move_h)

    # I
    letter_i = tk.Button(
        text="I",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_i.grid(row=12, column=1)


    def move_i(event):
        move_thumb(590)
        time.sleep(0.5)

        move_index(362)
        time.sleep(0.5)

        move_middle(399)
        time.sleep(0.5)

        move_ring(432)
        time.sleep(0.5)

        move_pinky(663)
        time.sleep(0.5)


    letter_i.bind("<Button-1>", move_i)

    # J
    letter_j = tk.Button(
        text="J",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_j.grid(row=12, column=2)


    def move_j(event):
        move_thumb(590)
        time.sleep(0.5)

        move_index(362)
        time.sleep(0.5)

        move_middle(399)
        time.sleep(0.5)

        move_ring(432)
        time.sleep(0.5)

        move_pinky(663)
        time.sleep(0.5)


    letter_j.bind("<Button-1>", move_j)

    # K
    letter_k = tk.Button(
        text="K",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_k.grid(row=12, column=3)


    def move_k(event):
        move_thumb(610)
        time.sleep(0.5)

        move_index(627)
        time.sleep(0.5)

        move_middle(648)
        time.sleep(0.5)

        move_ring(432)
        time.sleep(0.5)

        move_pinky(505)
        time.sleep(0.5)


    letter_k.bind("<Button-1>", move_k)

    # L
    letter_l = tk.Button(
        text="L",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_l.grid(row=12, column=4)


    def move_l(event):
        move_thumb(674)
        time.sleep(0.5)

        move_index(627)
        time.sleep(0.5)

        move_middle(430)
        time.sleep(0.5)

        move_ring(432)
        time.sleep(0.5)

        move_pinky(505)
        time.sleep(0.5)


    letter_l.bind("<Button-1>", move_l)

    # M
    letter_m = tk.Button(
        text="M",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_m.grid(row=12, column=5)


    def move_m(event):
        tkinter.messagebox.showinfo(message="Currently not suported")


    letter_m.bind("<Button-1>", move_m)

    # N
    letter_n = tk.Button(
        text="N",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_n.grid(row=12, column=6)


    def move_n(event):
        tkinter.messagebox.showinfo(message="Currently not suported")


    letter_n.bind("<Button-1>", move_n)

    # O
    letter_o = tk.Button(
        text="O",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_o.grid(row=13, column=0)


    def move_o(event):
        move_thumb(588)
        time.sleep(0.5)

        move_index(398)
        time.sleep(0.5)

        move_middle(430)
        time.sleep(0.5)

        move_ring(432)
        time.sleep(0.5)

        move_pinky(505)
        time.sleep(0.5)


    letter_o.bind("<Button-1>", move_o)

    # P
    letter_p = tk.Button(
        text="P",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_p.grid(row=13, column=1)


    def move_p(event):
        tkinter.messagebox.showinfo(message="Currently not suported")


    letter_p.bind("<Button-1>", move_p)

    # Q
    letter_q = tk.Button(
        text="Q",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_q.grid(row=13, column=2)


    def move_q(event):
        move_thumb(588)
        time.sleep(0.5)

        move_index(645)
        time.sleep(0.5)

        move_middle(427)
        time.sleep(0.5)

        move_ring(432)
        time.sleep(0.5)

        move_pinky(505)
        time.sleep(0.5)


    letter_q.bind("<Button-1>", move_q)

    # R
    letter_r = tk.Button(
        text="R",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_r.grid(row=13, column=3)


    def move_r(event):
        tkinter.messagebox.showinfo(message="Currently not suported")


    letter_r.bind("<Button-1>", move_r)

    # S
    letter_s = tk.Button(
        text="S",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_s.grid(row=13, column=4)


    def move_s(event):
        move_thumb(595)
        time.sleep(0.5)

        move_index(274)
        time.sleep(0.5)

        move_middle(349)
        time.sleep(0.5)

        move_ring(327)
        time.sleep(0.5)

        move_pinky(424)
        time.sleep(0.5)


    letter_s.bind("<Button-1>", move_s)

    # T
    letter_t = tk.Button(
        text="T",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_t.grid(row=13, column=5)


    def move_t(event):
        tkinter.messagebox.showinfo(message="Currently not suported")

    letter_t.bind("<Button-1>", move_t)

    # U
    letter_u = tk.Button(
        text="U",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_u.grid(row=13, column=6)


    def move_u(event):
        move_thumb(508)
        time.sleep(0.5)

        move_index(627)
        time.sleep(0.5)

        move_middle(641)
        time.sleep(0.5)

        move_ring(327)
        time.sleep(0.5)

        move_pinky(424)
        time.sleep(0.5)

    letter_u.bind("<Button-1>", move_u)

    # V
    letter_v = tk.Button(
        text="V",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_v.grid(row=14, column=0)


    def move_v(event):
        tkinter.messagebox.showinfo(message="Currently not suported")

    letter_v.bind("<Button-1>", move_v)

    # W
    letter_w = tk.Button(
        text="W",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_w.grid(row=14, column=1)


    def move_w(event):
        move_thumb(508)
        time.sleep(0.5)

        move_index(645)
        time.sleep(0.5)

        move_middle(650)
        time.sleep(0.5)

        move_ring(650)
        time.sleep(0.5)

        move_pinky(424)
        time.sleep(0.5)

    letter_w.bind("<Button-1>", move_w)

    # X
    letter_x = tk.Button(
        text="X",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_x.grid(row=14, column=2)


    def move_x(event):
        move_thumb(678)
        time.sleep(0.5)

        move_index(502)
        time.sleep(0.5)

        move_middle(420)
        time.sleep(0.5)

        move_ring(438)
        time.sleep(0.5)

        move_pinky(424)
        time.sleep(0.5)

    letter_x.bind("<Button-1>", move_x)

    # Y
    letter_y = tk.Button(
        text="Y",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_y.grid(row=14, column=3)


    def move_y(event):
        move_thumb(672)
        time.sleep(0.5)

        move_index(263)
        time.sleep(0.5)

        move_middle(354)
        time.sleep(0.5)

        move_ring(368)
        time.sleep(0.5)

        move_pinky(663)
        time.sleep(0.5)

    letter_y.bind("<Button-1>", move_y)

    # Z
    letter_z = tk.Button(
        text="Z",
        width=8,
        height=3,
        bg="white",
        fg="black",
        font=('Helvetica', 30),
        )

    letter_z.grid(row=14, column=4)


    def move_z(event):
        move_thumb(563)
        time.sleep(0.5)

        move_index(645)
        time.sleep(0.5)

        move_middle(354)
        time.sleep(0.5)

        move_ring(368)
        time.sleep(0.5)

        move_pinky(440)
        time.sleep(0.5)

    letter_z.bind("<Button-1>", move_z)

    window.mainloop()