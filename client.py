def stuff():
        
    import os
    import socket
    import time

    s = socket.socket()

    while True:
        try:
            s.connect(("localhost", 44000))
            break
        except:
            time.sleep(1)

    messages = [os.name, "quit"]
    x = 0
    while x <= len(messages):
        s.send(messages[x])
        x += 1
    string = "stuff"
    return string
    s.close()

