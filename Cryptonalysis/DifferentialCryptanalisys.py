from boolean import *

def DifferentialTable(sBox, n, m):
	N = 2 ** n
	M = 2 ** m
	table  = [0] * 2 ** (n + m)
	for alpha in range(0, N):
		for betta in range (0, M):
			#tableIndex = BinaryStrToValue(ValueToBinaryStr(alpha, n) + ValueToBinaryStr(betta, m))
			tableIndex = (alpha << m) ^ betta  #for speed
			for x in range(0, N):
				if sBox[x] ^ sBox[x ^ alpha] == betta:
					table[tableIndex] += 1
	return table
	
def PrintDifferentialTable(table, n, m):
	prevX = 0
	print "     ",
	for i in range(0, 2**m):
		print "%2s" % hex(i),
	print
	print "%3s" % "0x0: ",
	for i in range(0, len(table)):
		s = ValueToBinaryStr(i, n + m)
		x = s[:n]
		y = s[n + 1:]
		indexX = BinaryStrToValue(x)
		if indexX != prevX:
			print
			print "%3s" % hex(indexX) + ": ",
		print "%3s" % str(table[i]),
		prevX = indexX
	print

	
def DecodeIndexAsDif(index, n, m):
	val = ValueToBinaryStr(index, n + m);
	difX = int(val[:n], 2)
	difY = int(val[n:], 2)
	return hex(difX) + "->" + hex(difY)
	
def DifferentialMaximum(table):
	max = 0
	for i in range(1, len(table)):    #because table[0] is always max, but no meaningful
		if table[i] > max:
			max = table[i]
	return max
	
def DiffElementIndexes(table, element):
	indexes = list()
	for i in range(1, len(table)):  #because table[0] is always max, but no meaningful
		if table[i] == element:
			indexes.append(i)
	return indexes
		
				