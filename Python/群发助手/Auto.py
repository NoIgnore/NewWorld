import win32gui
import win32con
import win32clipboard as w
import time
import re
from win32gui import *
import pyautogui
import os
import pyautogui as pag
global widthExit, heightExit, NoneList, index
index = 0
NoneList = []

# 将消息写入剪贴板


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
        if (len(t) >= len(name) and pattern.match(t)):
            hasPerson = True
            tempName = t
            break
    if (hasPerson):
        return tempName
    else:
        NoneList.append(name)
        return "NothisPeoplehhj_hhj"


# qq搜索栏搜索指定好友


def searchUser(name, winName):
    # 鼠标定位qq搜索栏
    hand = win32gui.FindWindow('TXGuiFoundation', winName)
    setText(name)
    ClickPoint(widthExit, heightExit)  # 清空搜索栏
    time.sleep(0.5)
    win32gui.SendMessage(hand, win32con.WM_PASTE, 0, 0)  # 粘贴
    # 表示停止1.5秒再运行（运行太快qq会反应不过来）
    time.sleep(1.5)
    win32gui.SendMessage(hand, win32con.WM_KEYDOWN, win32con.VK_RETURN,
                         0)  # 按下回车
    win32gui.SendMessage(hand, win32con.WM_KEYUP, win32con.VK_RETURN,
                         0)  # 释放回车
    return hand


def sendMessage(n, t, name, msg):
    # 自动定位聊天窗口
    name2 = GetTitle(name)
    if name2 == "NothisPeoplehhj_hhj":
        print("查无此人：" + name)
        return
    hand = win32gui.FindWindow('TXGuiFoundation', name2)
    setText(msg)
    # 重复发送消息
    for i in range(1, n + 1):
        time.sleep(0.5)
        win32gui.SendMessage(hand, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(hand, win32con.WM_KEYDOWN, win32con.VK_RETURN,
                             0)  # 按下回车
        win32gui.SendMessage(hand, win32con.WM_KEYUP, win32con.VK_RETURN,
                             0)  # 释放回车
        i = i + 1
        time.sleep(t)
    time.sleep(2)
    win32gui.PostMessage(hand, win32con.WM_CLOSE, 0, 0)


# 按重复次数发送消息
def formal(name, msg, winName='QQ'):
    global index
    n = 1  # 次数
    t = 0  # 时间间隔
    searchUser(name, winName)
    time.sleep(1)
    index += 1
    print("正在发送第", index, "个......")
    sendMessage(n, t, name, msg)


def ClickPoint(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()


def GetXY(str):
    tempX = 0
    tempY = 0
    while True:
        # 获取屏幕的尺寸
        print("请选择" + str + "的坐标")
        screenWidth, screenHeight = pag.size()
        x, y = pag.position()
        # 返回鼠标的坐标
        print('屏幕尺寸: (%s %s),  鼠标坐标 : (%s, %s)' %
              (screenWidth, screenHeight, x, y))
        # 每个1s中打印一次 , 并执行清屏
        if tempX == float(x) and tempY == float(y):
            break
        else:
            tempX = float(x)
            tempY = float(y)
        time.sleep(2)
        # 执行系统清屏指令
        os.system('cls')
    return tempX, tempY


if __name__ == "__main__":
    print("在程序运行前，先打开群聊天窗口并移除遮挡窗口")
    widthExit, heightExit = GetXY("清空按键")
    print("清空群聊搜索的输入框（像素点）的横坐标为：", widthExit)
    print("清空群聊搜索的输入框（像素点）的纵坐标为：", heightExit)
    stringFileName = input("请输入保存名字的txt文件名(不包括后缀.txt)：")
    gap = int(input("输入大约间隔时间数字/秒：（例如：5）  "))
    groupL = input("请输入群名：")
    msg = input("请输入要发的消息内容：")
    try:
        file_obj = open(".\\" + stringFileName + ".txt", encoding="utf-8")
        print("UTF-8格式打开文件")
    except:
        file_obj = open(".\\" + stringFileName + ".txt",
                        encoding='gbk',
                        errors='ignore')
        print("GBK格式打开文件")
    all_lines = file_obj.readlines()
    abc = []
    for line in all_lines:
        abc.append(line.rstrip())
    for i in range(len(abc)):
        if (len(abc[i])) > 0:
            formal(abc[i], msg, winName=groupL)
            time.sleep(gap)
    if len(NoneList) > 0:
        with open(r'.\\非群里人员.txt', 'w') as f:
            for i in NoneList:
                f.write(i + '\n')
