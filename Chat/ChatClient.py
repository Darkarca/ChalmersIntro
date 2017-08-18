import zmq
import sys
import time

username = str(raw_input("Enter Username: "))

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://10.132.203.242:%s"% "80")

while True:
    msg = socket.recv()
    print msg
    socket.send("$&" + username)
    time.sleep(10)
