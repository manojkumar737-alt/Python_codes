movies = []
mov1 = input("enter 1st movie")
mov2 = input("enter 2nd movie")
mov3 = input("enter 3rd movie")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print (movies)

user_inputs = input("enter movies name with space seprated: ")
movies = list(map(str, user_inputs.split()))
print(movies)