import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('程序执行失败')
elif pid == 0:
    print('子进程')
    #获取当前进程的PID
    print('打印子进程的PID：',os.getpid())
    #获取父进程的PID
    print('打印子进程的父ID：',os.getppid())
else:
    print('这是父进程')
    print('打印子进程的PID：',pid)
    print('打印父进程的PID：',os.getpid())