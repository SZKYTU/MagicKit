import json
import socket
from re import S
from http import client
from NetworkTools.pcinfomodule import UserInfo
from NetworkTools.config import socketHost, socketPort


def clientJsonSend(ip, hostname, mac):
    global json, socket
    UserInfoJS = {
        "IP": UserInfo.getIP(),
        "Hostname": UserInfo.getHostname(),
        "MAC": UserInfo.getMAC()}

    json = json.dumps(UserInfoJS)

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((socketHost, socketPort))

    json = json.encode("utf8")

    socket.sendall(json)
