import socket

def checkNode(server,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server, int(port)))
        message="Server "+server+":"+port+" reachable\n"
    except socket.error as e:
        message="Server not available:"+server+":"+port+"\n"
    s.close()
    return message


