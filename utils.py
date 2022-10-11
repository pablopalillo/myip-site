import socket
import requests


def get_my_ip()->str:
    """get_my_ip
    
        get local ip adrress
    """

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return ip_address

def get_my_public_ip() ->str:
    """get_my_public_ip
    
    
    get the public ip of visitor.
    """

    try:
        ip_request = requests.get('https://api.ipify.org')
        
        if ip_request.status_code != requests.codes.ok:
            ip_request.raise_for_status()
        
        return ip_request.content.decode('utf8')

    except requests.exceptions.HTTPError:
        return None