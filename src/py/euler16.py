def paths(n):
	p=1
	for x in range(1, n+1): 
	  p=p*x
	return p

print(paths(40)/paths(20)/paths(20))
