# Division-
t = int(input())
for _ in range(t):
	n = int(input())
	if n >= 1900:
		print("Division 1")
	if 1900 > n >= 1600:
		print("Division 2")
	if 1600 > n >= 1400:
		print("Division 3")
	if n < 1400:
		print("Division 4")
