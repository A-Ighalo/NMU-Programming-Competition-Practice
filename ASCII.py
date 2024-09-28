# This script draws a square of size NxN using ASCII characters.
# The square is drawn using '|' for vertical sides, '-' for horizontal sides,
# '+' for corners, and spaces for the interior.
# Input: An integer N (0 <= N <= 1000) representing the interior side length of the square.
# Output: The ASCII representation of the square.

a = int(input())
print('+' + '-' * a + '+')

for n in range(a):
    print('|' + ' ' * a + '|')
print('+' + '-' * a + '+')
