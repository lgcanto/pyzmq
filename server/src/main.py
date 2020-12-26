import zmq
import time

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv()
        print("Message received from Client: %s" % message)
        socket.send(b"This is from Server")
