import socket

def getLocalIP(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    s.connect(("10.254.254", 1))
    ip = s.getsockname()[0]
    return ip