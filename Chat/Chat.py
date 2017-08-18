import zmq
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s"% "80")

while True:
    socket.send("dasdasd")
    msg = socket.recv()
    print msg
    time.sleep(1)
