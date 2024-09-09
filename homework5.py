my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', (1, 2, 3)}
print(my_set)
my_set.add(True)
my_set.add(float)
my_set.remove(1)
print(my_set)


my_dict = {'Mango': 'Манго', 'Orange': 'Апельсин'}
print(my_dict)
print(my_dict['Mango'], my_dict.get('Lemon'))
my_dict.update({'Pahlava': 'Medovaya', 'Pomidor': 'Помидорчик'})
self = my_dict.pop('Pahlava')
print(self)
print(my_dict)
