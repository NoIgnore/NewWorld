import time
from pynput.keyboard import Controller, Key

key = Controller()
times = int(input("请输入次数："))
print("请等待3s...")
time.sleep(3)
for i in range(times):
    time.sleep(1)
    key.press(Key.right)
    key.release(Key.right)
