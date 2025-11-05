# DeepLearningStudying
This repository is for me to record my study process about deep learning.
## 0 实用工具库
1. argparse
argparse模块用于命令行参数解析。
2. process 进程相关
* setproctitle: 设置进程名称
> Windos测试失败
> Linux应该没有问题
3. pdb: Python调试工具(python debugger)
**pdb常用命令说明**
当程序运行到 pdb.set_trace() 断点时，可以使用以下命令：
* l (list): 显示当前代码上下文
* n (next): 执行下一行代码（不进入函数）
* s (step): 执行下一行代码（进入函数）
* c (continue): 继续执行直到下一个断点
* p <variable>: 打印变量值
* pp <variable>: 美化打印变量值
* w (where): 显示当前调用栈
* u (up): 移动到上一层调用栈
* d (down): 移动到下一层调用栈
* h (help): 显示帮助信息
* q (quit): 退出调试器
4. 脚本命令
```sh
#> 输出重定向
python train.py > train.log 2>&1 &
## >: 输出重定向符号
## 2>&1: 将标准错误(文件描述符2)重定向到标准输出(文件描述符1)
### >&：重定向操作符
### 文件描述符对应关系：
### 0 = 标准输入(stdin)
### 1 = 标准输出(stdout) 
### 2 = 标准错误(stderr)
## &: 后台运行
```
## 1 模型定义
TodoList:
- [ ] 关于初始化时模型的输入参数，def __init__(self, *args, **kwargs) -> None:
- [ ] 模型复用设计
- [ ] 通用子模块的设置与属性
- [ ] 代码与文章的对应

1. model（使用torch.nn.Module定义）
2. torch.nn常用模块
* nn.Sequential



### 1.1 模型复用

# A 深度学习仓库资料（Appendix A）
