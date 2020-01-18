n = int(input())
l = 1
res = 1
dic = {1: 1}

for i in range(1, n + 1):
	cur = i;
	c = 0
	while i != 1:
		if i % 2 == 0:
			i = i / 2
		else:
			i = 3 * i + 1
		c += 1
		if i in dic:
			c += dic[i]
			break

	if c >= l:
		l = c
		res = cur
	dic[cur] = c

print(res, "-", l)