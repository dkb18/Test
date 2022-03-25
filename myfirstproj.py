
mylist = "john", "amy", "dex"
print(mylist)

num_users = len(mylist)
print("number of elements in mylist: " + str(num_users))
#age = input("how old are you?")
#age = int(age)
#if age<=4: print("eat shit")
#elif (age > 5) and (age <= 10) : print("eat pussy")
#elif (age>10) and (age <= 12) : print("ass cheeks")

dasyan = {'height' : 10 , 'name' : "dasyan", 'poes': "big", 'stekkies' : 0 }

print(str(dasyan['height']))
das_stekkies = dasyan.get('stekkies')
print(das_stekkies)
dasyan['assholes'] = 2
print(dasyan['assholes'])

def greet_person():
    """greet a human"""
    print("wk poes")

greet_person()

def greet_madhir(madhir):
    print("wk " + madhir )

greet_madhir("madhir")

def add_number(x,y,z):
    return x + y + z
print(str(add_number(12,34,56)))

class Dog():

    def __init__(self,name):
        self.name = name
    def sit(self):
        print(self.name + "is sitting")

mydog = Dog('peso')

sent_list = "fun","times","in","junction"

for key, value in dasyan.items() :
    print(key + " = " + str(value))

for idx, td in enumerate(sent_list) :
    print(idx, td)

pop = [3**x for x in range(0,5)]

print(pop)





