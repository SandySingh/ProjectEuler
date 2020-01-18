n = int(input())

s = str(2 ** n)

res = 0
for i in range(0, len(s)):
	res += int(s[i])

print(res)