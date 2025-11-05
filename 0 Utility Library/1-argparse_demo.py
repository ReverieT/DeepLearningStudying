"""
file: argparse_demo.py
description: Demonstrate the use of argparse
date: 2025/10/30
"""
import argparse

def parse_arguments():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="这里是脚本的描述，这里的文字可以通过-h参数来展示")
    
    # 必选参数，脚本必须传入的参数
    parser.add_argument("required_1", 
                       help="必选参数1")
    parser.add_argument("required_2", 
                       help="必选参数2")
    
    # 可选参数
    # help: 参数的描述
    # action: 参数的行为，可以是store_true、store_false、store_const、store_action、append、append_const、count、help、version
    ## store_true: 存储布尔值，如果参数被传入，则返回True，否则返回False
    ## store_false: 存储布尔值，如果参数被传入，则返回False，否则返回True
    ## store_const: 存储一个常量值，如果参数被传入，则返回指定的常量值，否则返回None
    ## store_action: 存储一个动作值，如果参数被传入，则返回指定的动作值，否则返回None
    ## append: 将参数值添加到列表中
    ## append_const: 将常量值添加到列表中
    ## count: 计算参数出现的次数
    ## help: 显示帮助信息并退出
    ## version: 显示版本信息并退出
    parser.add_argument("-v", "--verbose", 
                       action="store_true",
                       help="启用详细输出模式")
    # 添加带值的可选参数
    parser.add_argument("-o", "--output", 
                       default="output.txt",
                       help="输出文件名 (默认: output.txt)")
    # 添加限定选项的参数
    # 如果参数传入不在范围内，则进行报错
    parser.add_argument("--format", 
                       choices=["json", "csv", "xml"],
                       default="json",
                       help="输出格式 (默认: json)")
    # 其他参数
    ## type: 参数的数据类型

    # Namespace: argparse 解析后的参数会存储在一个 Namespace 对象中
    # 这个对象包含了所有解析出来的命令行参数，可以通过属性访问方式获取参数值
    # 使用方式: args.verbose, args.output 等
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    print(args.verbose)