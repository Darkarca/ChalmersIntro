import zmq
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s"% "80")

while True:
    msg = socket.recv()
    print msg
    socket.send("hej00")
    time.sleep(1)