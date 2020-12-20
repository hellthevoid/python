from class_article import Article

class ElectroArticle (Article):

    def __init__(self,name,id,price,voltage,power):

        super().__init__(name,id,price)

        self.voltage=voltage
        self.power=power

    def combined_output(self):
        print(self.name)
        print(self.id)
        print(self.price)
        print(self.voltage)
        print(self.power)
