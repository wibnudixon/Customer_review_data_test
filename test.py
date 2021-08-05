day_hours = 24
week_days = 7

week_hours = day_hours * week_days
print(week_hours)


x=list(range(1,10))
print(x)

y=list(range(1,10,2))
print(y)

# strings = ['qwe','ert']
# float = 23.1, 23.4
# integers = 23
# list can contain lists as well

student_grades = [9.1,7.3,6.5]
# dir(list)
# dir(string) 
# dir(__builtins__)

my_sum = sum(student_grades)

length = len(student_grades)
mean = my_sum / length

studen_grades = [9.1,10,8.1,10,10,4.1,5.6]
print(studen_grades.count(10))

student_grades = {"Ben":9.1, "Sil":10.8,"Jim":8.1}
# keys and values (Dictionaries)
print(student_grades.values())
# student_grades.keys()

# tuples (1,2,3) faster

monday_temperatures = [9.1,8.8,7.5]
# append, clear, index

# dir(list)
# help(list)
# index
monday_temperatures.__getitem__(1)
# or
monday_temperatures[1]

seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)

# accesssing list slices
# monday_temperatures[1:3]/ [:2] / [ 3:]
# postive & negative indexing 

# creating mean function
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1,4,5]))

# identation in a fucntion should be consistent

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) /len(value)
    else : 
        the_mean = sum(value) / len(value)

    return(the_mean)

# string fromatting

user_input = input("Ënter your name:")
message = f"Hello {user_input}"
print(message)

name = input("Ënter your firstname:")
surname = input("Ënter your surname:")
message = "Hello %s %s" % (name, surname)
print(message)


# loops 
monday_temperatures = [9.1,8.8,7.6]

for temperature in monday_temperatures:
    print(round(temperature))

student_grades = {"Ben":9.1, "Sil":10.8,"Jim":8.1}

for grades in student_grades.values(): 
    print(grades)

# values or keys

# While Loops
a = 3

while a>0:
    print(1) 
    # will print 1 indefintely

# username = ''
# while username !="pypy"
  #    username = input("Enter username: ")


#while True:
 #   username = input("Enter username:")
#   if username == 'pypy':
        # break
    # else:
        # continue 

# Simplelistcomprehension

temps = [221,234,340,230]
new_temps = [temp/ 10 for temp in  temps]
print(new_temps)
