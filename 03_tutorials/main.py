from  class_stack import Stack
import sys

print(sys.path)

stack1=Stack(0)
stack2=Stack(0)
#stack1.array.append(2)

for i in range(1,4):
    stack1.push(stack1.read_1_item())

print("Stack1: ")
stack1.write()
print("Stack2: ")
stack2.write()

for i in range(1,4):
    stack2.push(stack1.pop())

print("Stack1: ")
stack1.write()
print("Stack2: ")
stack2.write()

print("Cubes of stack 3: " + str(stack2.calculate_sum()))