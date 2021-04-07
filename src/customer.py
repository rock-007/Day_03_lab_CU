import pdb
class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def buy_drink(self, drink_to_buy, pub):
        if pub.check_age_of_customer(self) and pub.check_drunkenness(self):
            self.wallet -= drink_to_buy.price
            #pub.till += drink_to_buy.price
            pub.till_update(drink_to_buy.price)
            self.update_drunkenness(drink_to_buy)
            return True
        else:
            return False

    def update_drunkenness(self, drink_to_buy):
        self.drunkenness += drink_to_buy.alcohol_level

    def customer_rejuvenate(self, food):
        self.drunkenness -= food.rejuvenation_level

    def buy_food(self, food_to_buy, pub):
        self.wallet -= food_to_buy.price
        pub.till_update(food_to_buy.price)
        self.customer_rejuvenate(food_to_buy)