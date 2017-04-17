# Making a Pancake


def make_breakfast(my_breakfast):
    ingredients = input("Provide ingredients for %s : " % my_breakfast)
    print("Get " + ingredients)
    print("Mix 'em up")
    print("Pour into the heated pan, with oil")
    print("Flip to the other side")
    breakfast = "-----Yummy " + my_breakfast + "-----"
    return breakfast

print(make_breakfast("Pancake"))
print(make_breakfast("Eggs"))
