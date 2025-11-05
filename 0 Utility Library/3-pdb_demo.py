import pdb

def debug_example():
    x = 10
    y = 20
    pdb.set_trace()  # 设置断点
    z = x + y
    print(f"结果: {z}")
    return z

if __name__ == "__main__":
    debug_example()

# pdb调用方法：
## 当程序运行到 pdb.set_trace() 断点时，可以使用以下命令：
## l (list): 显示当前代码上下文
## n (next): 执行下一行代码（不进入函数）
## s (step): 执行下一行代码（进入函数）
## c (continue): 继续执行直到下一个断点
## p <variable>: 打印变量值
## pp <variable>: 美化打印变量值
## w (where): 显示当前调用栈
## u (up): 移动到上一层调用栈
## d (down): 移动到下一层调用栈
## h (help): 显示帮助信息
## q (quit): 退出调试器