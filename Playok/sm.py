from pynput.mouse import Button, Controller
from boardsp import getf
from boardsp import getXY

import time
mouse = Controller()
def move(move):
	mouse.position = move
def click():
	mouse.click(Button.left, 1)
##print('Value a[0]: ', getXY(a,1), ' Value c[0]: ', getXY(c, 1), ' Value a[0] - c[0] = ', getXY(a,1) - getXY(c,1))
ready = input('Are you ready? (y/n): ').upper()
while ready != 'Y':
    ready = input('Are you ready? (y/n): ').upper()
    continue
print('Di chuyen chuot den goc phai cua ban co, giu chuot 5s!')
time.sleep(5)
a = mouse.position
name = input('Nhap ban co: ')
dbn = getf(name)
kcx = dbn[0]
kcy = dbn[1]
x = getXY(a, 1)+ kcx
y = getXY(a, 2) - kcy
print('Toa do XY: (x = ', x, ', y = ', y, ', khoang cach = ',kcx, '/', kcy, ')')
list = []
value = []
char = ["o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
for i in range(0,15):
	for j in range(0, 15):
		k = j
		output = char[i] + str(-(k - 15))
		list.append(output)
for i in range(1,16):
        x -= kcx
        y1 = y
        for j in range(1,16):
                y1 += kcy
                output = (x, y1)
                value.append(output)
        y1 = y
def find(a,b):
    for i in range(len(b)):
        if a == b[i]:
            return i
            break
def returnmove(s):
    output = 0
    for i in list:
        if s == i:
            k = find(s, list)
            output = value[k]
    return output    
exit = 0

    
    
    
