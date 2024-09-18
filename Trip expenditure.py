print("\033c")
def hotel_cost(nights):
    return 2500*nights

def plane_ride_cost(city):
    if city =="Sylhet":
        return 1500
    elif city =="Bandarban":
        return 1250
    elif city =="Cox":
        return 1800
    elif city =="STMartin":
        return 2375
    
def rental_car_cost(days):
    if days>=7:
        return 800*days - 500
    elif days>=3:
        return 800*days - 250
    else:
        return 800*days
    
def totalamount(city,day):
    return hotel_cost(day)+ plane_ride_cost(city)+ rental_car_cost(day)

c= input("where do u wanna go?[Sylhet,Bandarban,Cox,STMartin]")
d= int(input("How many days do u wanna stay: "))

total = totalamount(c,d)

print()

print(f"hotel cost for {d} days:{hotel_cost(d)}")
print(f"plane ride cost for {d} days:{plane_ride_cost(c)}")
print(f"Rental car cost  for {d} days:{rental_car_cost(d)}")
print(f" total cost for {d} days:{total}")

    
    