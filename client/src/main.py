import zmq
import time

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.RCVTIMEO = 10000 # in ms
    socket.linger = 0
    socket.connect("tcp://server:5555")

    while True:
        socket.send(b"This is a message from Client")
        message = socket.recv()
        print("Received message from Server: %s" % message)
        time.sleep(5)
