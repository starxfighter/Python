def printNames(myList):
    for x in range(0, len(myList)):
        # print(myList[x]["first_name"])
        print(myList[x]["first_name"], myList[x]["last_name"])

# Part II
def classPrint(myDict):
    # counter = 1
    for key, data in myDict.items():
        print(key)
        for x in range(0, len(data)):
            firstname = data[x]["first_name"]
            lastname = data[x]["last_name"]
            full_name = firstname + lastname
            length = len(full_name)
            print(x+1, "-", firstname, " ", lastname, "-", length)



students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
printNames(students)
print("Version II")
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
classPrint(users)
