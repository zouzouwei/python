#-*- codeing =utf-8 -*-
#@Time :2020/7/24 12:25
class Lizaed:
    def __init__(self,name):
        self.name = name
    def set_name(self, name):
        self.name = name
        
lizaed= Lizaed('deep')
print(lizaed.name)

lizaed.set_name('lizaed')
print(lizaed.name)