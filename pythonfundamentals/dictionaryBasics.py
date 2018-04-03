# Create a dictionary and print out the key value pairs
def printProfile(myProfile):
    for key,data in myProfile.items():
     print("My ", key, "is ", data)

profile ={
    "name":"Duane Osburn",
    "age":47,
    "country of birth": "The United States",
    "favorit language": "Python"
}
printProfile(profile)
