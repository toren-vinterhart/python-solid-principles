ice_cream_flavors = ["chocolate", "vanilla"]


class MakeIceCream:
    def __init__(self, flavor):
        self.flavor = flavor

    def make(self):
        if self.flavor in ice_cream_flavors:
            print("Great success. You now have ice cream.")
        else:
            print("Epic fail. No ice cream for you.")


class AddIceCream:
    def __init__(self, flavor):
        self.flavor = flavor

    def add(self):
        ice_cream_flavors.append(self.flavor)


add_strawberry_flavor = AddIceCream("strawberry")
add_strawberry_flavor.add()

make_strawberry_ice_cream = MakeIceCream("strawberry")
make_strawberry_ice_cream.make()


""" This code snippet violates Open-Closed Principle(OCP)
ice_cream_flavors = ['chocolate', 'vanilla']

class MakeIceCream:

    def __init__(self, flavor):
        self.flavor = flavor

    def make(self):
        if self.flavor in ice_cream_flavors:
            print("Great success. You now have ice cream.")
        else:
            print("Epic fail. No ice cream for you.")
"""
