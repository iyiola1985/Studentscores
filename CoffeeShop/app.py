class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        if order not in self.orders:
            self.orders.append(order)
            order.coffee = self

    def __repr__(self):
        return f"Coffee(name={self.name})"


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        if order not in self.orders:
            self.orders.append(order)
            order.customer = self

    def __repr__(self):
        return f"Customer(name={self.name})"


class Order:
    def __init__(self, coffee=None, customer=None):
        self.coffee = coffee
        self.customer = customer

        if coffee:
            coffee.add_order(self)
        if customer:
            customer.add_order(self)

    def __repr__(self):
        return f"Order(coffee={self.coffee}, customer={self.customer})"


# Example usage:
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

customer1 = Customer("Alice")
customer2 = Customer("Bob")

order1 = Order(coffee=coffee1, customer=customer1)
order2 = Order(coffee=coffee2, customer=customer1)
order3 = Order(coffee=coffee1, customer=customer2)

print(coffee1)  # Coffee(name=Espresso)
print(coffee2)  # Coffee(name=Latte)
print(customer1)  # Customer(name=Alice)
print(customer2)  # Customer(name=Bob)

print(coffee1.orders)  # [Order(coffee=Coffee(name=Espresso), customer=Customer(name=Alice)), Order(coffee=Coffee(name=Espresso), customer=Customer(name=Bob))]
print(customer1.orders)  # [Order(coffee=Coffee(name=Espresso), customer=Customer(name=Alice)), Order(coffee=Coffee(name=Latte), customer=Customer(name=Alice))]
