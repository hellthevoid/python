class Article():
    def __init__(self,name,id,price):
        self.name=name
        self.id=id
        self.price=price
    
    def combined_output(self):
        print(self.name)
        print(self.id)
        print(self.price)

    def combined_input(self):
        self.name=input("Please enter the name:")
        self.price=input("Price:")
        self.id=input("ID:")



