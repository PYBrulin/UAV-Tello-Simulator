#
# Tello Python3 Control Demo
# Modified to control the virtual Tello
#
# This script was initially released by http://www.ryzerobotics.com/ on 1/1/2018
#

import threading
import socket

host = ""
port = 9000  # The receiving port
locaddr = (host, port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ("127.0.0.1", 8889)  # The sending port
sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print("Received from Tello : '{}'".format(data.decode(encoding="utf-8")))
        except Exception:
            print("\nException occured . . .\n")
            break


print(
    "\r\n\r\nTello Python3 Demo.\r\n\n"
    + "Tello: command takeoff land flip forward back left right \r\n"
    + "up down cw ccw speed speed?\r\n\n"
    + "Use 'end' -- to quit the demo.\r\n"
)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True:

    try:
        msg = input("")

        if not msg:
            break

        if "end" in msg:
            print("EXITING")
            sock.close()
            break

        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print("\n . . .\n")
        sock.close()
        break
