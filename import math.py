import math

print("Refresh Me")

#####TYPES#####

a = "Hello"
print (a)
str

a = 4 
print(a)
int

a = int(a)
print(a)

a = 'hello'

#doesnt store upper
a.upper()

a = a.upper()

a = 3.5
print(a)
float

a = True
print(a)
bool

#saves as nothing
None

a = '2'
a + '1'

#Will through err
a + 1
print(a)

#have to
a + str(1)

a = f"{a}1"

print(a)

######CONDITIONS#######

a = 1

if a > 0

# doesnt print anything
if a < 0:
    print(a < 0)

if a > 0: print("greater")

a = -1 

if a > 0: 
    print("greater")
elif a < 0: 
    print("less")

if a > 0:
    print("greater")

else: 
    print ("Not greater")

a = '2'

# work work bc str to int have to use int()
a > 1


###functions###
def add(x,y):
    return x + y

add(1,2)

#####SEQUENCES#####


a = "python"
a[0]

a[0] + a[1]

tup = (1,2,3)
print tup

tup[0]

tuple

len(tup)


list

ls [3,2,1]
print(ls)

ls.append(4)
print (ls)

ls.sort()
ls

set

st = {1,2,3}

print(st)

st.add(4)

print(st)

#wont add bc its not unique value using set
st.add(1)

####DICT#####

dc {1:'one', 2:'two'}

print(dc)

dc[1]

for i in dc: 
    print(i)

for i in dc.items():
    print(i)

for i in range(10):
    print(i)


colors = ["blue", "red"]
for color in colors:
    print(color)


#######CLASSES####

##Creating objects everything in pi is an object


class Dog():
    def __init__(self, name):
        self.name = name

dog = Dog("Leo")
print(dog)

dog.name

print(dog.name)

####INHERETENCE####

dog.name
'Leo'

class Doodle(Dog):
    def __init__(self,name,curly):
        super().__init__(name)
        self.curly = curly

doodle = Doodle("leo", True)

doodle

doodle.name

doodle.curly

######Error Handling######


a = '1'

a > 1

try: a > 1
    except TypeError:
        print("a is not number")

#####MODULES#####
##import math 
##at top of file

math.sqrt(9)

math.pi
