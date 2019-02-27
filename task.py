#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Syarhey Matusevich"
another_string_email = "riferman@mail.ru"

# Define a hierarchy and create multiple colors. Collect a bouquet (you can use accessories) to determine its value.
# Determine the time of its withering by the average lifetime of all flowers in a bouquet.
# Allow the sorting of flowers in a bouquet based on various parameters (freshness / color / stem length / cost ...)
# Implement a search for flowers in the bouquet according to certain parameters.
# Find out if there is a flower in the bouquet.


default_price = 0
default_freshness = 0


class Bouquet(object):
    def __init__(self, *flowers):
        self.list_flowers = list(flowers)

    def add_flower(self, flower):
        self.list_flowers.append(flower)

    def remove_flower(self, flower):
        if flower in self.list_flowers:
            self.list_flowers.remove(flower)

    def add_flowers(self, *flowers):
        for flower in flowers:
            self.list_flowers.append(flower)

    def remove_flowers(self, *flowers):
        for flower in flowers:
            self.list_flowers.remove(flower)

    def overall_price(self):
        total_price = 0
        for flower in self.list_flowers:
            total_price = total_price + flower.price
        return total_price

    def bouquet_lifetime(self):
        total_time = 0
        for flower in self.list_flowers:
            total_time = total_time + flower.freshness
        return int(total_time / len(self.list_flowers))

    def flower_available(self, flower):
        if flower in self.list_flowers:
            return ('The {} is already in the bouquet'.format(flower.name))
        else:
            return ('The {} is not in the bouquet'.format(flower.name))

    def flowers_quantity(self):
        return len(self.list_flowers)

    def sorted_flowers_by_price(self):
        flowers = {flower.name: flower.price for flower in self.list_flowers}
        sorted_flowers = sorted(flowers.items(), key=lambda item: item[1])
        return sorted_flowers

    def sorted_flowers_by_freshness(self):
        flowers = {flower.name: flower.freshness for flower in self.list_flowers}
        sorted_flowers = sorted(flowers.items(), key=lambda item: item[1])
        return sorted_flowers

    def find_flower_by_price(self, price):
        flowers = [flower.name for flower in self.list_flowers if price == flower.price]
        if len(flowers) == 0:
            return ('Flower with price {} is not found'.format(price))
        else:
            return ('Flowers with price {}: '.format(price) + str(flowers))


class Flower(Bouquet):
    def __init__(self, name, stalk_lenght, color, price=default_price, freshness=default_freshness):
        self.stalk_lenght = stalk_lenght
        self.color = color
        self.price = price
        self.freshness = freshness
        self.name = name


class Buttercup(Flower):
    def __init__(self, name, stalk_lenght, color, price=default_price, freshness=default_freshness):
        super(Buttercup, self).__init__(name, stalk_lenght, color, price, freshness)


class Rose(Flower):
    def __init__(self, name, stalk_lenght, color, price=default_price, freshness=default_freshness):
        super(Rose, self).__init__(name, stalk_lenght, color, price, freshness)


class Pion(Flower):
    def __init__(self, name, stalk_lenght, color, price=default_price, freshness=default_freshness):
        super(Pion, self).__init__(name, stalk_lenght, color, price, freshness)


rose1 = Rose(name='rose1', stalk_lenght=5, color="red", price=5, freshness=20)
pion1 = Pion(name='pion1', stalk_lenght=7, color="green", price=5, freshness=20)
buttercup1 = Buttercup(stalk_lenght=8, name='buttercup1', color="yellow", price=20, freshness=10)

pion2 = Pion(name='pion2', stalk_lenght=7, color="green", price=7, freshness=20)
rose2 = Rose(name='rose2', stalk_lenght=5, color="red", price=23, freshness=13)
buttercup2 = Buttercup(name='buttercup2', stalk_lenght=4, color="yellow", price=5)

buket1 = Bouquet()
buket1.add_flower(buttercup1)
buket1.add_flower(rose1)
buket1.add_flower(pion1)

buket2 = Bouquet()
buket2.add_flower(buttercup2)
buket2.add_flower(rose2)
buket2.add_flower(pion2)

print('Bouquet1:')
print('Bouquet overall price {}'.format(buket1.overall_price()))
print('Bouquet lifetime {}'.format(buket1.bouquet_lifetime()))
print('Flowers quantity in bouquet {}'.format(buket1.flowers_quantity()))
print(buket1.flower_available(pion2))
print('Sorted flowers by price {}'.format(buket1.sorted_flowers_by_price()))
print('Sorted Flowers by freshness {}'.format(buket1.sorted_flowers_by_freshness()))

print('Bouquet2:')
print('Bouquet overall price {}'.format(buket2.overall_price()))
print('Bouquet lifetime {}'.format(buket2.bouquet_lifetime()))
print('Flowers quantity in bouquet {}'.format(buket2.flowers_quantity()))
print(buket2.flower_available(pion1))
print(buket2.flower_available(pion2))
print('Sorted flowers by price {}'.format(buket2.sorted_flowers_by_price()))
print('Sorted Flowers by freshness {}'.format(buket2.sorted_flowers_by_freshness()))
print(buket2.find_flower_by_price(10))
print(buket2.find_flower_by_price(5))
