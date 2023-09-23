ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list . Lets fix it .")
# .split will split the list
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "song", "frisbee", "corn", "banana", "girl","boy"]

# len will add the number to the list
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    

print("Lets do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) 
print('#'.join(stuff[3:5]))


      

    