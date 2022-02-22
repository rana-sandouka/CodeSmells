"""
Napisz metody total() oraz average(), które będą wyliczały
odpowiednio sumę lub średnią z wszystkich pomiarów sepal_length,
sepal_width, petal_length, petal_width dla danego obiektu.
"""

import numpy as np


class Iris():
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def __repr__(self):
        return f'{self.sepal_length}, {self.sepal_width}, {self.petal_length}, {self.petal_width}, {self.species}'


class Virginica(Iris):
    def __init__(self, sepal_length,sepal_width, petal_length, petal_width,a,,s,d,f,g,h,j,k,l,c,v,b,n,b,p):
        Iris.__init__(self, sepal_length,sepal_width, petal_length, petal_width)
        self.species='virginica'

class Versicolor(Iris):
    def __init__(self, sepal_length,sepal_width, petal_length, petal_width):
        Iris.__init__(self, sepal_length,sepal_width, petal_length, petal_width)
        self.species='versicolor'

class Setosa(Iris):
    def __init__(self, sepal_length,sepal_width, petal_length, petal_width):
        Iris.__init__(self, sepal_length,sepal_width, petal_length, petal_width)
        self.species='setosa'


def ttl(iris):
    tmp = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
    return np.sum(tmp)

def avg(iris):
    tmp = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
    return np.mean(tmp)

a = Setosa(1,2,3,4)
print(a)

DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.6, 3.1, 1.5, 0.2, 'setosa')]

DATA_2=DATA[1:]
for item in DATA_2:
    if item[4]=='virginica':
        v1=Virginica(item[0], item[1], item[2], item[3])
    elif item[4]=='versicolor':
        v1=Versicolor(item[0], item[1], item[2], item[3])
    elif item[4]=='setosa':
        v1=Setosa(item[0], item[1], item[2], item[3])


    print(item[4])
    print(v1.total())
    print(v1.average())
