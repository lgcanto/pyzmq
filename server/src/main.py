import zmq
import time
import threading

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    def receive_messages_loop():
        while True:
            message = socket.recv()
            print("Message received from Client: %s" % message)
            socket.send(b"This is from Server")

    def just_print_something():
        while True:
            print("We're multi-threading!")
            time.sleep(5)

    receive_messages_loop_thread = threading.Thread(target = receive_messages_loop)
    receive_messages_loop_thread.start()
    just_print_something_thread = threading.Thread(target = just_print_something)
    just_print_something_thread.start()
