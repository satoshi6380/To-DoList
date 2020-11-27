def tallest_people(**people):
    for name, height in sorted(people.items()):
        if height == max(people.values()):
            print(f'{name} : {height}')
