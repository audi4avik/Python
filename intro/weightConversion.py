weight = float(input("Enter your weight: "))
scale = input("Choose (K)g or (L)bs: ")

if scale.upper() == "K":
    print("weight in kg: {}".format(weight / 2.205))
elif scale.upper() == "L":
    print("weight in pound: {}".format(weight * 2.205))
else:
    print("invalid choice made: {}; Enter either Kg or Lbs"  .format(scale))