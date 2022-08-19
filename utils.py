import socket


def get_my_ip()->str:
    """get_my_ip
    
        get public ip adrress
    """

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return ip_address
