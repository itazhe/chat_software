from tkinter import *
# import tkinter.messagebox
import socket, threading

def main_page():
    '''
    函数内容：聊天登录注册主页面

    '''
    global e1
    global e2

    # 创建tk对象
    mychat = Tk()

    # 设置窗口标题
    mychat.title("Mychat")

    # 设置窗口大小
    mychat.minsize(400, 300)

    # 设置窗口能否变长变宽，默认为True
    mychat.resizable(width=False, height=False)

    # 设置用户名标签
    l1 = Label(mychat, text="用户名：", font=("Arial", 12)).place(x = 40, y = 100)
    # 设置用户名框，以明文的形式显示
    e1 = Entry(mychat, show=None, font=(14)).place(x = 115, y = 100)

    # 设置密码标签
    l2 = Label(mychat, text="密    码：", font=("Arial", 12)).place(x = 40, y = 150)
    # 设置密码框，以明文的形式显示
    e2 = Entry(mychat, show="*", font=(14)).place(x = 115, y = 150)

    # 设置登录按钮
    b1 = Button(mychat, text="登 录", font=("Arial", 12)).place(x = 120, y = 200)

    b2 = Button(mychat, text="注 册", font=("Arial", 12), command=reg_page).place(x = 200, y = 200)


    mychat.mainloop()


def chat_page():
    '''
    函数内容：聊天窗口
    '''
    global chat_msg_box
    global chat_record_box

    # 创建tk对象
    mychat = Tk()
    # 设置窗口标题
    mychat.title("P1901班专属聊天室")

    chat_record_box = Text(mychat)
    # 窗口不可点击
    chat_record_box.configure(state=DISABLED)
    chat_record_box.pack(padx=10, pady=10)

    # 设置窗口能否变长变宽，默认为True
    mychat.resizable(width=False, height=False)

    chat_msg_box = Text(mychat)
    chat_msg_box.configure(width=65, height=5)
    chat_msg_box.pack(side=LEFT, padx=10, pady=10)

    send_msg_btn = Button(mychat, text="发送", command=on_send_msg)
    # send_msg_btn = Button(mychat, text="发送")
    send_msg_btn.pack(side=RIGHT, padx=10, pady=10, ipadx=15, ipady=15)

    threading.Thread(target=recv_chat_data).start()

    mychat.mainloop()

    
def reg_page():
    '''
    函数内容：用户注册页面
    '''
    global e3
    global e4
    global e5
    global e6

    # 创建tk对象
    mychat = Tk()

    # 设置窗口标题
    mychat.title("Mychat-Reg")

    # 设置窗口大小
    mychat.minsize(400, 300)

    # 设置窗口能否变长变宽，默认为True
    mychat.resizable(width=False, height=False)

    # 设置用户名标签
    l3 = Label(mychat, text="用户名：", font=("Arial", 12)).place(x = 35, y = 25)
    # 设置用户名框，以明文的形式显示
    e3 = Entry(mychat, show=None, font=(14)).place(x = 110, y = 25)

    # 设置密码标签
    l4 = Label(mychat, text="密    码：", font=("Arial", 12)).place(x = 35, y = 75)
    # 设置密码框，以明文的形式显示
    e4 = Entry(mychat, show="*", font=(14)).place(x = 110, y = 75)

    # 设置手机号标签
    l5 = Label(mychat, text="手机号：", font=("Arial", 12)).place(x = 35, y = 125)
    # 设置手机号框，以明文的形式显示
    e5 = Entry(mychat, show=None, font=(14)).place(x = 110, y = 125)

    # 设置邮箱标签
    l6 = Label(mychat, text="邮    箱：", font=("Arial", 12)).place(x = 35, y = 175)
    # 设置邮箱框，以明文的形式显示
    e6 = Entry(mychat, show=None, font=(14)).place(x = 110, y = 175)

    # 设置注册按钮
    b = Button(mychat, text="注 册", font=("Arial", 12)).place(x = 185, y = 230)


    mychat.mainloop()


def client_login_send():
    '''
    函数功能：用户登录请求
    '''
    myuname = e1.get(1.0, "end")
    mypasswd = e2.get(1.0, "end")
    req = '{"op": 1, "args":{"uname": "myuname", "passwd": "mypasswd"}}'
    data_top="{:<15}".format(len(req)).encode()
    sock.send(data_top)
    sock.send(req.encode())


def client_login_recv():
    '''
    函数功能：用户登录响应
    '''
    data_len = sock.recv(15).decode().rstrip()
    if len(data_len) > 0:
        data_len = int(data_len)

        recv_size = 0
        json_data = b""
        while recv_size < data_len:
            tmp = sock.recv(data_len - recv_size)
            if tmp == 0:
                break
            json_data += tmp
            recv_size += len(tmp)

        json_data = json_data.decode()
        rsp = json.loads(json_data)
        if rsp["error_code"] == 0:
            # print("登录成功！")
            chat_page()


def client_reg_send():
    '''
    函数功能：用户注册请求
    '''
    myuname = e3.get(1.0, "end")
    mypasswd = e4.get(1.0, "end")
    myphone = e5.get(1.0, "end")
    myemail = e6.get(1.0, "end")
    req = '{"op": 2, "args": {"uname": "myuname", "passwd": "mypasswd", "phone": "myphone", "email": "myemail"}}'
    data_top = "{:<15}".format(len(req)).encode()
    sock.send(data_top)
    sock.send(req.encode())


def client_reg_recv():
    '''
    函数功能：用户注册响应
    '''
    data_len = sock.recv(15).decode().rstrip()
    if len(data_len) > 0:
        data_len = int(data_len)

        recv_size = 0
        json_data = b""
        while recv_size < data_len:
            tmp = sock.recv(data_len - recv_size)
            if tmp == 0:
                break
            json_data += tmp
            recv_size += len(tmp)

        json_data = json_data.decode()
        rsp = json.loads(json_data)
        if rsp["error_code"] == 0:
            reg_success_page()
        else:
            # print("注册失败！")
            reg_failed_page()


def reg_success_page():
    '''
    函数内容：注册成功界面
    '''
    # 创建tk对象
    mychat = Tk()

    # 设置窗口标题
    mychat.title("注册成功！")

    # 设置窗口大小
    mychat.minsize(400, 300)

    # 设置窗口能否变长变宽，默认为True
    mychat.resizable(width=False, height=False)

    # 设置用户名标签
    l1 = Label(mychat, text="恭喜注册成功!!!", font=("Arial", 18)).place(x = 110, y = 120)
    
    b2 = Button(mychat, text="返回登录界面", font=("Arial", 12), command=main_page).place(x = 270, y = 250)

    mychat.mainloop()


def reg_failed_page():
    '''
    函数内容：注册失败界面
    '''
    # 创建tk对象
    mychat = Tk()

    # 设置窗口标题
    mychat.title("注册失败！")

    # 设置窗口大小
    mychat.minsize(400, 300)

    # 设置窗口能否变长变宽，默认为True
    mychat.resizable(width=False, height=False)

    # 设置用户名标签
    l1 = Label(mychat, text="注册失败!!!", font=("Arial", 18)).place(x = 110, y = 120)
    
    b2 = Button(mychat, text="返回注册界面", font=("Arial", 12), command=reg_page).place(x = 270, y = 250)

    mychat.mainloop()


def on_send_msg():
    '''
    函数功能：发送聊天消息
    '''
    nick_name = main_page.e1.get(1.0, "end")
    chat_msg = chat_msg_box.get(1.0, "end")
    if chat_msg == "\n":
        return

    chat_data = nick_name + ":" + chat_msg
    chat_data = chat_data.encode()
    data_len = "{:<15}".format(len(chat_data)).encode()
    try:
        sock.send(data_len + chat_data)
    except:
        messagebox.showerror("温馨提示", "发送消息失败，请检查网络连接！")
    else:
        chat_msg_box.delete(1.0, "end")
        chat_record_box.configure(state=NORMAL)
        chat_record_box.insert("end", chat_data.decode() + "\n")
        chat_record_box.configure(state=DISABLED)


def recv_chat_data():
    '''
    函数功能：接收聊天消息
    '''
    global sock

    while True:
        try:
            while True:
                msg_len_data = sock.recv(15)
                if not msg_len_data:
                    break

                msg_len = int(msg_len_data.decode().rstrip())
                recv_size = 0
                msg_content_data = b""
                while recv_size < msg_len:
                    tmp_data = sock.recv(msg_len - recv_size)
                    if not tmp_data:
                        break
                    msg_content_data += tmp_data
                    recv_size += len(tmp_data)
                else:
                    # 显示
                    chat_record_box.configure(state=NORMAL)
                    chat_record_box.insert("end", msg_content_data.decode() + "\n")
                    chat_record_box.configure(state=DISABLED)
                    continue
                break
        finally:
                sock.close()
                sock = socket.socket()
                sock.connect(("127.0.0.1", 9999))

# sock = socket.socket()
# sock.connect(("127.0.0.1", 9999))

# threading.Thread(target=recv_chat_data).start()

if __name__ == "__main__":
    main_page()
    # chat_page()
    # reg_page()
    # reg_failed_page()

# sock.close()