import time
start = time.time()

a = [[1,0,1],
	 [0,1,0],
	 [1,0,1],
	 [0,1,0]]

rowsLen,colsLen,movex,movey,lines,linelen = len(a),len(a[0]),0,0,[],0

def findOne():
	global movex,movey
	for x in range(rowsLen):
		for y in range(colsLen):
			if a[x][y] == 1:
				movex,movey = x,y
				return True
	return False

def checknext(x,y):
	global a
	if x < 0 or y < 0:
		return False
	elif x > rowsLen-1 or y > colsLen-1:
		return False
	elif a[x][y] == 0:
		return False
	else:
		return True

def checklinelen(x,y):
	global a,linelen
	a[x][y] = 0
	linelen = linelen + 1
	if checknext(x,y-1) and checknext(x,y+1) and checknext(x-1,y) and checknext(x+1,y):
		return
	if checknext(x,y-1):
		checklinelen(x,y-1)
	if checknext(x,y+1):
		checklinelen(x,y+1)
	if checknext(x-1,y):
		checklinelen(x-1,y)
	if checknext(x+1,y):
		checklinelen(x+1,y)

def findline():
	global lines,a,linelen
	while findOne():
		linelen = 0
		checklinelen(movex,movey)
		lines.append(linelen)

findline()
print(lines)

end = time.time()
print(end - start)