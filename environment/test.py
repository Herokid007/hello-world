def x():
    x = input("Would you like to buy stamps, envelope, or make copy? ")
    if x == "stamps":
     print("We have stamps avaliable. ")
    elif x == "envelope":
     print("We have all sizes avaliable. ")
    elif x == "copy":
     copies = input("How many copies? ")
     print("You can have{}".format(copies))
    else:
     print("Thank you. ")

while True:
    x()