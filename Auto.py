from turtle import title
import win32gui, win32con
import win32clipboard as w
import time
import re
from win32gui import *
from datetime import datetime 

#将消息写入剪贴板
def setText(text):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, text)
    w.CloseClipboard()

def GetTitle(name):
    titles = set()

    def foo(hwnd, mouse):
        if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
            titles.add(GetWindowText(hwnd))

    EnumWindows(foo, 0)
    lt = [t for t in titles if t]
    lt.sort()
    pattern = re.compile(r'(.*)' + name + r'(.*)')
    for t in lt:
        if (pattern.match(t)):
            return t

#qq搜索栏搜索指定好友
def searchUser(name):
    #鼠标定位qq搜索栏
    hand = win32gui.FindWindow('TXGuiFoundation', 'QQ')
    setText(name)
    win32gui.SendMessage(hand, 770, 0, 0)
    #表示停止1.5秒再运行（运行太快qq会反应不过来）
    time.sleep(1.5)
    win32gui.SendMessage(hand, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    return hand

def sendMessage(n,t,name,msg):
    #自动定位聊天窗口
    hand = win32gui.FindWindow('TXGuiFoundation', GetTitle(name))
    setText(msg)
    #重复发送消息
    for i in range(1, n + 1):
        win32gui.SendMessage(hand, 770, 0, 0)
        win32gui.SendMessage(hand, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        i = i + 1
        time.sleep(t)
    print("运行完成!")
    win32gui.PostMessage(hand, win32con.WM_CLOSE, 0, 0)

#按重复次数发送消息
def formal(name, msg):
    n = 1#次数
    t = 0#时间间隔
    searchUser(name)
    time.sleep(1)
    print("开始发送")
    print('...')
    sendMessage(n,t,name,msg)


if __name__ == "__main__":#在程序运行前，先点击qq的搜索
    name = "敦刻尔"
    #msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formal(name, msg)
