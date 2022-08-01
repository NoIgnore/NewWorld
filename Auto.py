import win32gui, win32con
import win32clipboard as w
import time
import re
from win32gui import *
import pyautogui
global widthExit, heightExit, h2, w2
global index
index = 1
NoneList = []

#将消息写入剪贴板
def setText(text):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, text)
    w.CloseClipboard()


def GetTitle(name):
    hasPerson = False
    tempName = ""
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
            hasPerson = True
            tempName = t
            break
    if (hasPerson):
        return tempName
    else:
        NoneList.append(name)


#qq搜索栏搜索指定好友
def searchUser(name, winName):
    global widthExit, heightExit, h2, w2
    #鼠标定位qq搜索栏
    hand = win32gui.FindWindow('TXGuiFoundation', winName)
    setText(name)
    ClickExit(widthExit, heightExit)
    time.sleep(1)
    win32gui.SendMessage(hand, 770, 0, 0)
    #表示停止1.5秒再运行（运行太快qq会反应不过来）
    time.sleep(2)
    win32gui.SendMessage(hand, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    return hand


def sendMessage(n, t, name, msg):
    #自动定位聊天窗口
    hand = win32gui.FindWindow('TXGuiFoundation', GetTitle(name))
    setText(msg)
    #重复发送消息
    for i in range(1, n + 1):
        ClickExit(w2, h2)
        time.sleep(0.5)
        win32gui.SendMessage(hand, 770, 0, 0)
        win32gui.SendMessage(hand, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        i = i + 1
        time.sleep(t)
    time.sleep(3)
    win32gui.PostMessage(hand, win32con.WM_CLOSE, 0, 0)


#按重复次数发送消息
def formal(name, msg, winName='QQ'):
    global index
    n = 1  #次数
    t = 0  #时间间隔
    searchUser(name, winName)
    time.sleep(1)
    print("开始发送第", index, "个")
    index += 1
    sendMessage(n, t, name, msg)


def ClickExit(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()


if __name__ == "__main__":
    print("在程序运行前，先打开群聊天窗口并移除遮挡窗口")
    widthExit = float(input("清空群聊搜索的输入框（像素点）的横坐标："))
    heightExit = float(input("清空群聊搜索的输入框（像素点）的纵坐标："))
    w2 = float(input("单独私聊的输入框中心（像素点）的横坐标："))
    h2 = float(input("单独私聊的输入框中心（像素点）的纵坐标："))
    stringFileName =input("请输入保存名字的txt文件名(不包括后缀.txt)：")
    groupL = input("请输入群名：")
    msg=input("请输入要发的消息内容：")
    file_obj = open(".\\" + stringFileName + ".txt", encoding="utf-8")
    all_lines = file_obj.readlines()
    abc = []
    for line in all_lines:
        abc.append(line.rstrip())
    for i in range(len(abc)):
        formal(abc[i], msg, winName=groupL)
    with open(r'.\\非群里人员.txt', 'w') as f:
        for i in NoneList:
            f.write(NoneList[i].rstrip() + '\n')