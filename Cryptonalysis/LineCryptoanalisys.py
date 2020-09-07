from boolean import *
import math

"""
Generate line of values function <lineX, X> XOR <lineY, Y> for all X,Y
"""
def LinearLink(lineX, lineY):
	func = list()
	x = "0" * len(lineX)
	while x != "":
		y = "0" * len(lineY)
		while y != "":
			func.append( (ScalarBool(x, lineX) + ScalarBool(y, lineY)) % 2)
			y = NextBoolVec(y)
		x = NextBoolVec(x)
	return func
	
"""
Generate all linear equations between input and output of s-box: n->m
links is a table with indexes X|Y from 0...0|0...0 to 1...1|1...1
"""
def GenerateLineLinks(n, m):
	links = list()
	lineX = "0" * n
	
	while lineX != "":
		lineY = "0" * m
		while lineY != "":
			links.append(LinearLink(lineX, lineY))
			lineY = NextBoolVec(lineY)
		lineX = NextBoolVec(lineX)
	return links

"""
Generate linear approximation table to sBox n->m
Sbox in hex representation
links - linear i/o equation getted from GenerateLineLinks
"""
def LinearApproximationTable(sBox, n, m, links):
	N = 2**n
	table = [0] * len(links)
	for i in range(0, N):
		#x = ValueToBinaryStr(i, n) + ValueToBinaryStr(sBox[i], m)  
		#index = BinaryStrToValue(x) #index = X|Y= line in links table
		index = (i << m) ^ sBox[i]    #for speed
		for j in range(0, len(links)):
			# if for equation j cell X|Y ==0, it means (i, sBox[i]) satisfy eq with number j
			if links[j][index] == 0:    
				table[j] = table[j] + 1
	b = 2**n / 2
	for i in range(0, len(table)):
		table[i] = table[i] - b
	return table

"""
Print linear approximation table in readable format
"""
def PrintLinearApproximationTable(table, n, m):
	prevX = 0
	print "   ",
	for i in range(0, 2**m):
		print "%2s" % str(i),

	print
	print "%3s" % "0: ",
	for i in range(0, len(table)):
		s = ValueToBinaryStr(i, n + m)
		x = s[:n]
		y = s[n + 1:]
		indexX = BinaryStrToValue(x)
		if indexX != prevX:
			print
			print str(indexX) + ":" + " " * (2 - len(str(indexX))),
		print "%2s" % str(table[i]),
		prevX = indexX
	print

		
		
def LinearApproximateMaximum(table, badIndexes = []):
	max = 0
	for i in range(1, len(table)):    #because table[0] is always max, but no meaningful
		if abs(table[i]) > max and i not in badIndexes:
			max = table[i]
	return max
	
	
"""
Return indexes in array where value = element 
"""
def ElementIndexes(table, element):
	indexes = list()
	for i in range(1, len(table)):  #because table[0] is always max, but no meaningful
		if abs(table[i]) == element:
			indexes.append(i)
	return indexes
	

			
			
			
			
			
			
			
			
			
			
			