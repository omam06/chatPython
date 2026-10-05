# collects any number of keyword arguments into a dictionary
def show(**kwargs):
    print(kwargs)
show(name='Gunna', age=34, country='USA')

print()

# can work with the dictionary created
def show(**kwargs):
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['country'])
show(name='Gunna', age=34, country='USA')

# a function can accept bith args and kwargs
def show(*args, **kwargs):
    print(args)
    print(kwargs)
show('Foden', 47, club='Man City', country='England')
