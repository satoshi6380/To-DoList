# finish the function
def find_the_parent(child):
    for c in (Drinks, Pastry, Sweets):
        if issubclass(child, c):
            print(c.__name__)
