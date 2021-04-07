import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food
class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.stock= {"beer":5, "alcohol":6}
        self.drink_1 = Drink("wine", 8, 0.12)
        self.drink_2 = Drink("absinthe", 8, 0.8)
        self.food_1 = Food("pizza", 6, 0.4)
        self.customer_1 = Customer("Craig", 20, 18)
        self.customer_2 = Customer("Jack", 20, 18)
        self.customer_3 = Customer("Jack", 20, 17)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_buy_drink_customer_wallet_update(self):
        self.customer_1.buy_drink(self.drink_1, self.pub)
        self.assertEqual(12, self.customer_1.wallet)

    def test_buy_drink_till_update(self):
        self.customer_1.buy_drink(self.drink_1, self.pub)
        self.assertEqual(108, self.pub.till)

    def test_buy_drink_customer_over_18(self):
        update_status = self.customer_2.buy_drink(self.drink_1, self.pub)
        self.assertEqual(True, update_status)

    def test_buy_drink_customer_under_18(self):
        update_status = self.customer_3.buy_drink(self.drink_1, self.pub)
        self.assertEqual(False, update_status)

    def test_drunkenness_update(self):
        self.customer_1.buy_drink(self.drink_1, self.pub)
        self.assertEqual(0.12, self.customer_1.drunkenness)
        
    def test_too_drunk(self):
        customer_check = self.customer_2.buy_drink(self.drink_1, self.pub)
        self.assertEqual(True, customer_check)

    def test_not_too_drunk(self):
        self.customer_2.buy_drink(self.drink_2, self.pub)
        customer_check_2 = self.customer_2.buy_drink(self.drink_2, self.pub)
        self.assertEqual(False, customer_check_2)
        self.assertEqual(12, self.customer_2.wallet)

    def test_customer_rejuvenate(self):
        self.customer_2.buy_drink(self.drink_2, self.pub)
        self.customer_2.buy_food(self.food_1, self.pub)
        self.assertEqual(0.4, self.customer_2.drunkenness)

    # def test_check_stock(self):
    #     self.pub.update_stock(self.stock)
    #     stock = self.pub.check_stock("beer")
    #     self.assertEqual(5, stock)
     