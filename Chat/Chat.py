import zmq
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s"% "80")

while True:
    socket.send("server message to cliet3")
    msg = socket.recv()
    print msg
    time.sleep(1)
