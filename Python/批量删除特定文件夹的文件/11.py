import os

fileList = os.listdir()
def Del(filepath):
    if os.path.exists(filepath):
           os.remove(filepath)

for file in fileList:
    if file[:3] == "xxx":
        os.chdir(r'./' + file + r'/')
        print(file+"\n")
        for i in range(1, 29):
            if i % 2 == 0:
                fileName = ("00" + str(i)) if len(str(i)) < 2 else("0" + str(i))
                fileName = "image"+fileName+".png"
                pwd = os.getcwd()
                Del(fileName)
        Del("xxxx.xxx")
        os.chdir(r'../')

print('Finished.')
