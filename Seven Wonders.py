#place the string in a dictionary having the letter as a key and the count as the value


# a = input()
# dict_count = {}
#
# for count in a:
#     if count not in dict_count:
#         dict_count[count] = 1
#     else:
#         dict_count[count] += 1
#
# print(dict_count)
#
# Square = 2, 2, 2

#if dict_count[count] > 2: mn
# for count in range(len(dict_count)):
#     Result = dict_count.values()
#     print(Result)
#
# #TCGTTC
#
# print(dict_count.keys())


# Input string
cards = input("Enter the scientific cards played (e.g., 'TTCGG'): ")

# Initialize counts for each type of card
count_T = cards.count('T')
count_C = cards.count('C')
count_G = cards.count('G')

# Calculate points for each type of card
points_T = count_T ** 2
points_C = count_C ** 2
points_G = count_G ** 2

# Calculate points for sets of three different cards
sets_of_three = min(count_T, count_C, count_G)
points_sets = sets_of_three * 7

print(sets_of_three, points_sets)

# Total points
total_points = points_T + points_C + points_G + points_sets

# Output the total points
print("Total scientific points:", total_points)
