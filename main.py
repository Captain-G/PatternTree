# this program forms a tree of *
# variable num_of_stars to store the no of *
# variable space to store the whitespace

num_of_stars = 1
count = 0
lines = int(input("Enter the number of lines you desire in your tree : "))
space = lines - 1
while count < lines:
    print(" "*space + "*"*num_of_stars)
    space = space - 1
    num_of_stars = num_of_stars + 2
    count = count + 1
