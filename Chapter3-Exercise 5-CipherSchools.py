#  ask a user for name 
# Example - Divyanshu 
# print count of each word 
# output:
#  D:1
#  i:2
#  v:3
#  y:4
#  a:5
#  N:6
#  s:7
#  h:8
#  u:9



# Using count through while loop

name = input("Please enetr your name: ")
x = ""
i = 0
while i < len(name):
    if name[i] not in x:
        x += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1