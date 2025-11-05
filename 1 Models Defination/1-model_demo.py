from typing import Any


import torch
from torch.fft import Tensor
import torch.nn as nn
import torch.nn.functional as F

class CustomSubModule(nn.Module):
    # 在初始化中，可以接受一些参数，一般方便调用，会定义一些与模型有关的超参数，比如关于维度定义的参数
    ## e.g.:
    ##      def __init__(self, in_channels, out_channels)
    # 超参数的定义也为模型调用提供了丰富度与灵活性
    def __init__(self, *args, **kwargs) -> None:
        # 先调用父类的初始化方法，获得父类的属性方法
        super().__init__(*args, **kwargs)

        # 初始化方法中定义模型子部件作为属性
        ## 举例：定义一个卷积层子部件，这里Conv2d的最父类实际上也是nn.Module
        self.conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)
        ## 举例：定义批次归一化层子部件
        self.bn = nn.BatchNorm2d(num_features=64)
        ## 举例：定义ReLU激活层子部件
        self.relu = nn.ReLU()

    # forward函数是在模型函数被调用时，会自动执行的函数
    ## 举例：
    ## 当我在程序中定义custom_sub_module = CustomSubModule()，这时调用__init__并定义好模型属性与方法
    ## 当我执行custom_sub_module(x)时，会自动调用custom_sub_module.forward(x)函数
    def forward(self, x: Tensor) -> Tensor:
        # 我们定义模块的子模块也是同样的道理，定义好部件后，使用类似conv(x)的方法实际上是在调用conv.forward(x)函数
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        return x


# 测试
if __name__ == '__main__':
    # 定义模型
    custom_sub_module = CustomSubModule()
    # 定义输入数据
    x = torch.randn(1, 3, 224, 224)
    print(f"x.shape: {x.shape}")
    print(f"x: {x}")
    # 模型调用
    y = custom_sub_module(x)
    # 输出结果
    # 1*3*224*224 ->(conv)-> 1*64*224*224 ->(bn)-> 1*64*224*224 ->(relu)-> 1*64*224*224
    ## conv: 64 for channels_change; 224 for stride and padding(padding=0 224->222)
    ## bn: just for 标准化、归一化，维度不变
    ## relu: 非线性进行激活，不改变维度
    print(f"y.shape: {y.shape}")
    print(f"y: {y}")
