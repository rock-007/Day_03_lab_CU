class Pub:

    def __init__(self,name, till):
        self.name=name
        self.till=till
        self.drinks=[]
        #self.food=food
        self.stock={}

    def update_stock(self,stock):
        self.stock=stock
    
    def check_age_of_customer(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def till_update(self, amount):
        self.till += amount
    # def check_stock(self, drink):
    #     print(drink)
    #     for drink in self.stock:
