#-*- codeing =utf-8 -*-
#@Time :2020/7/27 10:52
def number_code(i):
    if  i%15==0 : return 3
    elif i%5==0 : return 2
    elif i%3==0: return 1
    else:return 0

def code_yiyi(i,prediction):
    return [str(i),"fizz","buzz","fizzbuzz"][prediction]
for i in range (100):
 print(code_yiyi(i,number_code(i)))
        