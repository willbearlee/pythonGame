cars = {'audi', 'bmw', 'subaru', 'toyota'}

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car.lower() == 'audi':
        print("Audi!!")
    else:
        print(car.title())

mag_num = 10
if (mag_num < 15) and (mag_num > 3):
    print("MAGIC")

if (mag_num < 15) or (mag_num > 3):
    print("MAGIC")

if "audi" in cars:
    print("AUDI !!")

if "audii" not in cars:
    print("NO AUDII !!")

##
# Check if list are empty
request_toppings = []

if request_toppings:
    print("Has someting")
else:
    print("Noting")

## Multi list
avail_toppings = ['mushroms', 'olives', 'fish']
request_toppings = ['mushroms', 'fish']

for request_topping in request_toppings:
    if request_topping in avail_toppings:
        print(f"add request {request_topping} toppings")
    else:
        print("Can't fulfill")
