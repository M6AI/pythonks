"""
This module aims to explain Python container and collection types. These
terms are often times used interchangeably, but in terms of abstraction,
the container only has to implement the __contains__ dunder, while
collections should come with the __iter__ and __len__ methods on top of
that.
"""
from collections.abc import Container, Collection


class SingleContainer(Container):

    def __init__(self, item):
        self.item = item

    def __contains__(self, item):
        return item == self.item


class MyCollection(Collection):

    def __init__(self, items: Collection):
        self.items = items

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    single_container = SingleContainer("gift")
    print("surprise" in single_container)
    print("gift" in single_container)

    collection = MyCollection(["item_1", "item_2"])
    print("surprise" in collection)
    print("item_1" in collection)
    print(len(collection))
    for item in collection:
        print(item)
