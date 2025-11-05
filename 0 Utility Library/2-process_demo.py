import setproctitle
import os
import time
import sys
import platform

def setproctitle_test():
    print(f"当前系统名称: {platform.system()}")
    print("=== 进程信息 ===")
    print(f"PID: {os.getpid()}")
    print(f"Python可执行文件: {sys.executable}")
    print(f"原始进程名: {setproctitle.getproctitle()}")
    
    # 设置进程名
    new_title = "setproctitle test"
    setproctitle.setproctitle(new_title)
    
    print(f"设置的新进程名: {new_title}")
    print(f"当前进程名: {setproctitle.getproctitle()}")
    
    # 验证是否真的改变了
    if setproctitle.getproctitle() == new_title:
        print("✅ 进程名修改成功！")
    else:
        print("❌ 进程名修改失败")
    
    print(f"\n请用以下命令验证:")
    if platform.system() == 'Windows':  # Windows系统
        print(f'tasklist /fi "pid eq {os.getpid()}"')
        print("或者在任务管理器'详细信息'中查看'命令行'列")
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':  # Linux/macOS系统
        print(f'ps -p {os.getpid()} -o args=')
    else:
        print("当前操作系统不支持进程名验证")
    # Re: Windows测试失败
    # 来自pypi的信息：
    ## Note that on Windows there is no way to change the process string: 
    ## what the module does is to create a Named Object 
    ## whose value can be read using a tool such as Process Explorer 
    ## (contribution of a more useful tool to be used together with setproctitle would be well accepted).
    
    # Linux: 
    ## 使用ps命令
    
    # 保持运行
    counter = 0
    try:
        while True:
            counter += 1
            print(f"运行中... [{counter}] - 进程名: {setproctitle.getproctitle()}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n进程结束")

if __name__ == '__main__':
    setproctitle_test()