class order:
    def __init__(self, order_id, customer_name, items,quantity,price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.quantity = quantity
        self.price = price
    def display_order(self):
        print("order_id:", self.order_id)    
        print("customer_name:", self.customer_name)
        print("items:", self.items)
        print("quantity:", self.quantity)
        print("price:", self.price)
        print("total:", self.total_price)
    def calculate_total(self):
        self.total_price = self.quantity * self.price
order1 = order("kavya", "rice", 2, 50)
order2 = order("tharun", "milk", 1, 30)
#display obj attributes
      print("order1 details")
      print("order_id:', order1.order_id)
      print("customer_name:", order1.customer_name)
      print("items:", order1.items)
      print("quantity:", order1.quantity)
      print("price:", order1.price)
      print("total":, order1.total_price)
      print()
      print("order2 details")
      pritnt("order_id:", order2.order_id)
      print(order2.customer_name)
      print("order2 items:", items)
      print("order2 quantity:", order2.quantity)
      print("order2 price:", order2.price)
      print()
      #calling 
      print("complete order details")
      order1.display_order()
      order2.display_order()
      


















