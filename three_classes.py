# Write your solution here
class Checklist:
    def __init__(self, header, entries):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id, balance, discount):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model, length, max_speed, bidirectional):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional

if __name__ == "__main__":
    checklist1 = Checklist("Shopping List", ["Apples", "Bananas", "Milk"])
    customer1 = Customer("1234", 100.0, 5)
    cable1 = Cable("Ethernet", 1.5, 1000, True)

    print(checklist1.header, checklist1.entries)
    print(customer1.id, customer1.balance, customer1.discount)
    print(cable1.model, cable1.length, cable1.max_speed)


