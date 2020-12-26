import zmq
import time
import threading

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.RCVTIMEO = 10000 # in ms
    socket.linger = 0
    socket.connect("tcp://server:5555")

    def send_messages_loop():
        while True:
            socket.send(b"This is a message from Client")
            message = socket.recv()
            print("Received message from Server: %s" % message)
            time.sleep(5)

    def just_print_something():
        while True:
            print("We're multi-threading!")
            time.sleep(5)

    send_messages_loop_thread = threading.Thread(target = send_messages_loop)
    send_messages_loop_thread.start()
    just_print_something_thread = threading.Thread(target = just_print_something)
    just_print_something_thread.start()
