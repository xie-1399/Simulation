'''
关于链接，如何实现一个链接器，即如何将各种代码和数据片段收集并组合成一个单一的文件
编译器和汇编器生成可重定位的目标文件（包括共享目标文件），通过连接器之后生成可执行目标文件
共享目标文件可以在加载或者运行时被动态加载进内存中并进行链接

:链接器如何处理多重定义的全局符号，主要是根据强弱符号的定义，函数和已初始化的全局变量是强符号，未初始化的全局变量是弱符号
（1）不允许有多个同名的强符号
（2）强符号和弱符号同名选择强符号
（3）有多个弱符号同名则随便选择一个
'''

import os
def compile(*args):
    file = ""
    for arg in args:
        file += " " + arg
    command = "gcc -Og -o output" + file
    os.system(command)

def showELF(file):
    os.system("readelf -a " + file + ">>out.txt" )

def checkWerror():
    print("using -Werror check global var define")



if __name__ == '__main__':
    compile("./demo/main.c","./demo/sum.c")
    showELF("./output")