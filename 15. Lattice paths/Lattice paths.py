grid_size = int(input())

# Formula is (Total Distance)! / ( (Grid Size)! X (Grid Size)! )
# Total distance is (Grid Size X 2)

dividend = 1
for i in range(grid_size + 1, grid_size * 2 + 1):
	dividend = dividend * i

divisor = 1
for i in range(2, grid_size + 1):
	divisor = divisor * i

res = dividend / divisor
print(int(res))