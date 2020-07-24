#-*- codeing =utf-8 -*-
#@Time :2020/7/17 14:13
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
torch.set_printoptions(linewidth=120)

train_set=torchvision.datasets.FashionMNIST(
    root='./data/FashionMINIST'
    ,train=True
    ,download=True
    ,transform=transforms.Compose([
        transforms.ToTensor()
    ])
)
train_loader=torch.utils.data.DataLoader(
    train_set,batch_size=10
)

print(len(train_set))#显示照片的存量
print(train_set.train_labels)#显示图片的标签  比如1代表人 2代表动物 3代表车之类的
print(train_set.train_labels.bincount())#bincount 表示频率 输出10组6000，应该就是每组数据的单独量，数据量一样是平衡，否则就是不平衡

sample=next(iter(train_set))#表示一个数据量的对象，然后我们可以进行迭代,next函数是进行对数据集下一个数据元素
len(sample)#检查样品长度
type(sample)#检查样品的标签
images,labels = sample
plt.imshow(images.squeeze(),cmap='gray')
print('label',labels)

batch=next(iter(train_loader))
images, labels=batch
#images.shape  torch.size[10,1,28,28] 10表示10张图片，1表示一种色域，28，28表示长宽都是28像素
#label.shape  torch.size[10] 这个数组表示10张图像
grid=torchvision.utils.make_grid(images,nrow=10)#这个函数创造一个网格，nrow表示一排显示图形数量
plt.figure(figsize=(15,15))#提供长宽高  不提供默认为6.4 ，4.8 figure是表示提供很多图行
plt.imshow(np.transpose(grid,(1,2,0)))
print('label',labels)#可以将图片显示出来
