for n in range(2, 10000):
	n = float(n)
	poly = n ** (1.0/n)
	exp = 1.00095355

	if poly < exp:
		print int(n)
		break

