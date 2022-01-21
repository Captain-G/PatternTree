# program to find out what came first:
# the egg or the chicken?
import emoji
egg = emoji.emojize(":egg:")
chicken = emoji.emojize(":chicken:")
arr = [egg, chicken]
arr.sort()
print("Correct order is :", arr)
