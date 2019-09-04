#!/usr/bin/python3
# -*- coding: utf -*-

import socket
import threading

def client_chat(sock_conn):
    try:
        while True:
            msg_len_data = sock_conn.recv(15)

            if msg_len == 0:
                break

            msg_len = int(msg_len_data.decode().rstrip())
            recv_size = 0
            msg_content_data = b''
            while recv_size < msg_len:
                tmp += sock_conn.recv(msg_len - recv_size)
                if tmp == 0:
                    break
                msg_data += tmp
                recv_size += len(tmp_data)
            else:
                # 发送给其他所有在线的客户端
                for sock_tmp, tmp_addr in client_socks:
                    # 如果不是自己就发一下
                    if sock_tmp is not sock_conn:
                        try:
                            sock_tmp.send(msg_len_data)
                            sock_tmp.send(msg_content_data)
                        except:
                            client_socks.remove((sock_tmp, tmp_addr))
                            sock_tmp.close()
                continue
            break
                

    finally:
        client_socks.remove((sock_conn, client_addr))
        sock_conn.close()

sock_listen = socket.socket()

# 端口号复用
sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind(("0.0.0.0", 9999))

sock_listen.listen(5)

# 所有客户端的套接字
client_socks = []

while True:
    # 接收连接
    sock_conn, client_addr = sock_listen.accept()
    client_socks.append((sock_conn, client_addr))
    # 创建线程
    threading.Thread(target=client_chat, args=(sock_conn, client_addr)).start()































































