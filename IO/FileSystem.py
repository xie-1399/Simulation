#Learn about File System
import os
import stat

def write_open(filename):
    fd = os.open(filename, os.O_WRONLY| os.O_APPEND|os.O_CREAT,0)
    print("fd number:", fd)
    return fd

def read_open(filename):
    # kind = os.umask(0)  #umask得到权限
    # print(kind)
    fd = os.open(filename,os.O_RDONLY|os.O_CREAT,0) #注意需要给定对应的权限
    print("fd number:",fd)
    return fd

def read(filename,size):
    fd = read_open(filename)
    os.chmod(filename, 0o777)
    bytes = os.read(fd,size)
    print("bytes:",bytes)
    os.close(fd)
    return bytes

#获取文件的元数据
def get_stat(path):
    structure = os.stat(path)
    if(stat.S_ISDIR(structure.st_mode)):
        print("this is a dir")
        get_dir(path)
    elif(stat.S_ISREG(structure.st_mode)):
        print("this is file")
    else:
        print("others")

def get_dir(path):
    print(os.listdir(path))

def write(filename,data):
    fd = write_open(filename)
    os.chmod(filename, 0o777)
    os.write(fd,str(data).encode())
    os.close(fd)


if __name__ == '__main__':
    # write("a.txt","hello111\n")
    # read("a.txt",100)
    get_stat(".")
