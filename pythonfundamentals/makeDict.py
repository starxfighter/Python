def make_dict(list1, list2):
  person_favorite = {}
  person_favorite = zip(list1,list2)
#   print(dict(person_favorite))
  return person_favorite




name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
x = dict(make_dict(name,favorite_animal))
print(x)
