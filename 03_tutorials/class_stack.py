

class Stack():

    def __init__(self,num):
        self.curr_num=num
        self.array=[]
    
    def push(self,item):
        self.array.append(item)
        self.curr_num+=1

    def pop(self):
        self.curr_num-=1
        return self.array.pop()

    def write(self):

        if self.curr_num==0:
                print("0")
                return
        for i in range(self.curr_num):
            print(self.array[i])

    def read_1_item(self):
        new_item=input("Please enter a Number")
        return new_item

    def calculate_sum(self):

        sum=0

        for item in self.array:
            var=float(item)
            sum+=var**3
        return sum