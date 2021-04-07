class Pub:

    def __init__(self,name, till):
        self.name=name
        self.till=till
        self.drinks=[]
        #self.food=food
        self.stock={}

    def update_stock(self, stock):
        self.stock=stock
    
    def check_age_of_customer(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def till_update(self, amount):
        self.till += amount
   

    def check_drunkenness(
        self, customer):
        if customer.drunkenness <= 0.6:
            return True
        else:
            return False
    
    def check_stock(self, drink):
        return self.stock.get(drink)
    
    def stock_decrease(self, drink):
        self.stock[drink.name] -= 1
