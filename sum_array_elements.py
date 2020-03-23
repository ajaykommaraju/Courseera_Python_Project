
input_string = input("eneter the list of elements seperated by space: ")
arr = input_string.split()
print("list",arr)
tot = 0
for num in arr:
    tot += int(num)
print(tot) 
    