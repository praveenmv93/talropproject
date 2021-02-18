import json

# def printResults(data):
# 	theJson = json.loads(data)
#
# from html.parser import HTMLParser
#
#
# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#         print("encountered data : ", data)
#         pos = self.getpos()
#
#         print("\tAt line : ", pos[0], " position ", pos[1])
#
#
# def main():
#     parser = MyHTMLParser()
#     f = open("samplehtml.html")
#     if f.mode == "r":
#         contents = f.read()
#         parser.feed(contents)
#
import xml.dom.minidom


class Animal:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.name = kwargs['name']
        self.sound = kwargs['sound']

    def type(self):
        return self.type

    def name(self):
        return self.name

    def sound(self):
        return self.sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError("print_animal(): requires an Animal ")
    print('the {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal(type="Kitten", name="fluffy", sound="rwar")
    print("Animal details", a0)
    print(a0.name)


if __name__ == "__main__": main()
