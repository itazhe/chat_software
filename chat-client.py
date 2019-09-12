from tkinter import *
#import tkinter.messagebox
import socket, threading
from PIL import ImageTk
import json

def main_page():
    '''
    函数内容：聊天登录注册主页面

    '''
    global log_uname
    global log_passwd

    # 创建tk对象
    mychat = Tk()

    # 设置tkinter窗口的位置
    mychat.geometry("+450+200")

    # 设置窗口标题/
    mychat.title("Mychat")

    # # 设置窗口大小
    # mychat.minsize(400, 300)
    # 设置背景图片
    canvas = Canvas(mychat,width = 420, height = 300)
    canvas.pack(expand = YES, fill = BOTH)

    image = ImageTk.PhotoImage(file = r"C:\Users\POWER\Desktop\web\img2\1.jpg")
    canvas.create_image(10, 10, image = image, anchor = NW)

    # 设置窗口能否变长变宽，默认为True
    mychat.resizable(width=False, height=False)

    # 设置用户名标签
    Label(mychat, text="用户名：", font=("Arial", 12)).place(x = 40, y = 110)
    # 设置用户名框，以明文的形式显示
    log_uname = Entry(mychat, show=None, font=(14))
    log_uname.place(x = 115, y = 110)

    # 设置密码标签
    Label(mychat, text="密    码：", font=("Arial", 12)).place(x = 40, y = 160)
    # 设置密码框，以明文的形式显示
    log_passwd = Entry(mychat, show="*", font=(14))
    log_passwd.place(x = 115, y = 160)

    # 设置登录按钮
    Button(mychat, text="登 录", font=("Arial", 12), command=client_login_send).place(x = 150, y = 210)
    # Button(mychat, text="登 录", font=("Arial", 12), command=chat_page).place(x = 150, y = 210)

    Button(mychat, text="注 册", font=("Arial", 12), command=reg_page).place(x = 230, y = 210)

    
    mychat.mainloop()


def chat_page():
    '''
    函数内容：聊天窗口
    '''
    global chat_frame
    global chat_input_frame

    mychat = Tk()
    # 设置窗口标题
    mychat.title("P1901班专属聊天室")

    # 设置窗口大小
    mychat.minsize(650, 460)

    # 设置背景图片
    # canvas = Canvas(mychat, width=1200,height=699,bd=0, highlightthickness=0)

    # canvas = Canvas(mychat)
    # canvas.pack(expand = YES, fill = BOTH)

    # image = ImageTk.PhotoImage(file = r"C:\Users\POWER\Desktop\web\img2\1.jpg")
    # canvas.create_image(10, 10, image = image, anchor = NW)
    

    # 设置tkinter窗口的位置
    mychat.geometry("+360+130")

    # 设置窗口背景颜色
    mychat.configure(bg="#334353")

    #设置窗口能否变长变宽，默认为True
    mychat.resizable(width=False, height=False)

    # 设置聊天框 
    chat_frame = Text(mychat, width=70, height=25)
    chat_frame.place(x = 3, y = 2)
    #窗口不可点击
    chat_frame.configure(state=DISABLED)

    # 设置聊天输入框 
    chat_input_frame = Text(mychat, width=70, height=5)
    chat_input_frame.place(x = 3, y = 350)

    # 信息框
    message_box = Text(mychat, width=20, height=34)
    message_box.place(x = 500, y = 2)
    #窗口不可点击
    message_box.configure(state=DISABLED)

    send_msg_btn = Button(mychat, text="发 送", font=("Arial", 12), command=on_send_msg, width=10)
    # send_msg_btn = Button(mychat, text="发 送", font=("Arial", 12), width=10)
    send_msg_btn.place(x = 390, y = 423)

    threading.Thread(target=recv_chat_data).start()

    mychat.mainloop()
    
def reg_page():
    '''
    函数内容：用户注册页面
    '''
    global reg_uname
    global reg_passwd
    global reg_phone
    global reg_email

    # 创建tk对象
    mychat = Tk()

    # 设置窗口标题
    mychat.title("Mychat-Reg")

    # 设置窗口大小
    mychat.minsize(430, 302)

    # 设置窗口背景颜色
    mychat.configure(bg="#334353")
    # 设置背景图片
    # canvas2 = Canvas(mychat,width = 420, height = 300)
    # canvas2.pack(expand = YES, fill = BOTH)

    # image2 = ImageTk.PhotoImage(file = r"C:\Users\POWER\Desktop\web\img2\3.jpg")
    # canvas2.create_image(10, 10, image = image2, anchor = NW)

    # 设置tkinter窗口的位置
    mychat.geometry("+450+202")

    # 设置窗口能否变长变宽，默认为True
    mychat.resizable(width=False, height=False)

    # 设置用户名标签
    Label(mychat, text="用户名：", font=("Arial", 12)).place(x = 45, y = 35)
    # 设置用户名框，以明文的形式显示
    reg_uname = Entry(mychat, show=None, font=(14))
    reg_uname.place(x = 120, y = 35)

    # 设置密码标签
    Label(mychat, text="密    码：", font=("Arial", 12)).place(x = 45, y = 85)
    # 设置密码框，以明文的形式显示
    reg_passwd = Entry(mychat, show="*", font=(14))
    reg_passwd.place(x = 120, y = 85)

    # 设置手机号标签
    Label(mychat, text="手机号：", font=("Arial", 12)).place(x = 45, y = 135)
    # 设置手机号框，以明文的形式显示
    reg_phone = Entry(mychat, show=None, font=(14))
    reg_phone.place(x = 120, y = 135)

    # 设置邮箱标签
    Label(mychat, text="邮    箱：", font=("Arial", 12)).place(x = 45, y = 185)
    # 设置邮箱框，以明文的形式显示
    reg_email = Entry(mychat, show=None, font=(14))
    reg_email.place(x = 120, y = 185)

    # 设置注册按钮
    Button(mychat, text="注     册", font=("Arial", 12), command=client_reg_send, width=15, bg="#334353", fg="white").place(x = 160, y = 240)
    # Button(mychat, text="注 册", font=("Arial", 12)).place(x = 185, y = 230)


    mychat.mainloop()


def client_login_send():
    '''
    函数功能：用户登录请求
    '''
    myuname = log_uname.get()
    mypasswd = log_passwd.get()
    req = {"op": 1, "args":{"uname": myuname, "passwd": mypasswd}}
    req = json.dumps(req)
    data_top="{:<15}".format(len(req)).encode()
    sock.send(data_top)
    sock.send(req.encode())
    client_login_recv()


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
    myuname = reg_uname.get()
    mypasswd = reg_passwd.get()
    myphone = reg_phone.get()
    myemail = reg_email.get()
    req = {"op": 2, "args": {"uname": myuname, "passwd": mypasswd, "phone": myphone, "email": myemail}}
    req = json.dumps(req).encode()
    data_top = "{:<15}".format(len(req)).encode()
    sock.send(data_top)
    sock.send(req)
    client_reg_recv()


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
    Label(mychat, text="恭喜注册成功!!!", font=("Arial", 18)).place(x = 110, y = 120)
    
    Button(mychat, text="返回登录界面", font=("Arial", 12), command=main_page).place(x = 270, y = 250)

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
    Label(mychat, text="注册失败!!!", font=("Arial", 18)).place(x = 110, y = 120)
    
    Button(mychat, text="返回注册界面", font=("Arial", 12), command=reg_page).place(x = 270, y = 250)

    mychat.mainloop()

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

def on_send_msg():
    '''
    函数功能：发送聊天消息
    '''
    nick_name = log_uname.get()
    chat_msg = chat_input_frame.get(1.0, "end")
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
        chat_input_frame.delete(1.0, "end")
        chat_frame.configure(state=NORMAL)
        chat_frame.insert("end", chat_data.decode() + "\n")
        chat_frame.configure(state=DISABLED)


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
                    chat_frame.configure(state=NORMAL)
                    chat_frame.insert("end", msg_content_data.decode() + "\n")
                    chat_frame.configure(state=DISABLED)
                    continue
                break
        finally:
                sock.close()
                sock = socket.socket()
                sock.connect(("127.0.0.1", 9999))

# sock = socket.socket()
# sock.connect(("127.0.0.1", 9999))


if __name__ == "__main__":
    main_page()
    # chat_page()
    # reg_page()
    # reg_failed_page()


# sock.close()