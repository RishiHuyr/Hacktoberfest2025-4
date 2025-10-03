def km_to_miles(km): return km * 0.621371
def miles_to_km(miles): return miles / 0.621371
def kg_to_pounds(kg): return kg * 2.20462
def pounds_to_kg(lb): return lb / 2.20462

if __name__ == "__main__":
    print("Unit Converter")
    print("1. KM → Miles")
    print("2. Miles → KM")
    print("3. KG → Pounds")
    print("4. Pounds → KG")

    choice = input("Choose: ")
    val = float(input("Enter value: "))

    if choice == "1": print(f"{val} km = {km_to_miles(val):.2f} miles")
    elif choice == "2": print(f"{val} miles = {miles_to_km(val):.2f} km")
    elif choice == "3": print(f"{val} kg = {kg_to_pounds(val):.2f} lb")
    elif choice == "4": print(f"{val} lb = {pounds_to_kg(val):.2f} kg")
    else: print("Invalid option")
