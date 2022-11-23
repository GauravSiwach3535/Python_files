def details(name,**data):
    print(name)
    for a,b in data.items():
        print(a,b)

details("Goru", place = "Haryana" , age= 19 , no = 9879768768)
import sys

def hello():
    print("hello world")
    hello()