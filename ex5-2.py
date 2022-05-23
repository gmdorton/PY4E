
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
   
    if smallest is None:
        smallest = int(num)

    elif smallest > int(num):
        smallest = int(num)

    elif largest is None:
        largest = int(num)

    elif largest < int(num):
        largest = int(num)
    

print("Maximum is", largest)
print('Minimum is', smallest)
