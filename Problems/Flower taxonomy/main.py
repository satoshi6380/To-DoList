iris = {}


def add_iris(id_n, species, petal_length, petal_width, **args):
    d = {id_n: {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}}
    d[id_n].update(args)
    iris.update(d)

