months = ["January","February","March","April","May","June","July","August","September", "October", "November", "December"]
days = [31,28,31,30,31,30,31,31,30,31,30,31]

print("How many days a month have...")
month = int(input("Type a month number: "))
print(f"{months[month-1]} has {days[month-1]} days!")