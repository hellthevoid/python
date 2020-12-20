class Stack(object):
    def __init__(self,num):
        self.curr_num=num
        self.array=[]
    
    def push(self,item):
        self.array.append(item)
        self.curr_num+=1

    def pop(self):
        return self.array.pop()

    def write(self):
        for i in range(self.curr_num+1):
            print(self.array[i])
    
    def read_1_item(self):
        pass

    def calculate_sum(self):
        pass
