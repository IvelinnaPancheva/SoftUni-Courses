class Inventory:
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []
        self.capacity = self.__capacity

    def add_item(self, item: str):
        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
print()
inventory_new = Inventory(6)
inventory_new.add_item("perfume")
inventory_new.add_item("shower cream")
inventory_new.add_item("deo spray")
print(inventory_new.get_capacity())
print(inventory_new)

print()
inventory_new = Inventory(4)
inventory_new.add_item("tooth paste")
inventory_new.add_item("mouth wash")
inventory_new.add_item("brush")
inventory_new.add_item("bamboo brush")
print(inventory_new.get_capacity())
print(inventory_new)