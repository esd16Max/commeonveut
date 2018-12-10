def suitedefibo(max):
	suite = [0,1]
	i = 0
	while i < int(max):
		result = suite[i]+suite[i+1]
		iplus = i + 1
		print(str(suite[i]) + "+" + str(suite[iplus]) + "=" + str(result))
		suite.append(result)
		i += 1

def suite2(max):
	a = 0
	b = 0
	c = 1
	i = 0
	while i < int(max):
		a = b
		b = c
		c = a+b
		print (str(a) + " + " + str(b) + " = " + str(c))
		i += 1


max = raw_input("max?")
suite2(max)