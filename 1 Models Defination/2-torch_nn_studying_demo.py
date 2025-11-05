import torch
import torch.nn as nn
import torch.nn.functional as F

# 1. nn.Sequential
## nn.Sequential: 按照定义的顺序运行各个模块

sequential_modeules = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)

## 一种使用方式是利用Sequential构建一层模块，然后通过forward方法运行
class Sequential_Model(nn.Module):
    def __init__(self):
        super(Sequential_Model, self).__init__()
        self.sequential_modeules = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        x = self.sequential_modeules(x)
        return x
## 堆叠过程需要注意的一点是中间模块的输入输出维度都是要首尾对齐的

if __name__ == '__main__':
    # 1. 测试nn.Sequential
    print("1 测试nn.Sequential")
    print(sequential_modeules)
    print(sequential_modeules(torch.rand(1, 784)))
    print(sequential_modeules(torch.rand(1, 784)).shape)

    sequential_modeules_test = Sequential_Model()
    x = torch.rand(1, 784)
    print(sequential_modeules_test(x))
    print(sequential_modeules_test(x).shape)


