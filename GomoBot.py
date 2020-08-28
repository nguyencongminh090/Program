import os
import time
from time import perf_counter as clock
from pynput.mouse import Controller, Button
import pyautogui
from Coordinates import *
from connect import *
import keyboard

mouse = Controller()

def main():
    p = mouse.position
    
    x, y = pyautogui.locateCenterOnScreen('Playok/Logo.png')
    pyautogui.moveTo(x,y,duration=0.0)
    mouse.click(Button.left,1)
    time.sleep(0.3)
    try:
        x, y = pyautogui.locateCenterOnScreen('Playok/Topr.png')
    except:
        x, y = pyautogui.locateCenterOnScreen('Pk/Trrs.png')
    
    pyautogui.moveTo(x,y,duration=0.0)
    a = mouse.position
    print('A:', a)

    
    kcx = 41.6
    print('kx:',kcx)
    kcy = 41.6
    print('ky:',kcy)

    x = a[0] + kcx
    y = a[1] - kcy

    list = []
    value = []
    char = ["o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
    for i in range(0,15):
        for j in range(0,15):
            k = j
            output = char[i] + str(-(k-15))
            list.append(output)
    for i in range(1,16):
        x -= kcx
        y1 = y
        for j in range(1,16):
                y1 += kcy
                output = (round(x), round(y1))
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
    def findi(a,b):
        
        for i in range(len(b)):
            if str(a) == str(b[i]):
                return i
                break
    def guess(b,a):
        a0 = []
        a1 = []

        for i in range(len(a)):
            a0.append(a[i][0])
            a1.append(a[i][1])

        for i in range(len(a0)):
            if -4 < (int(a0[i]) - int(b[0])) < 4:
                out0 = a0[i]
        for i in range(len(a1)):
            if -4 < (int(a1[i]) - int(b[1])) < 4:
                out1 = a1[i]           
            
        output = (out0,out1)
        return output
        

        
    def returnpos(s):
        output = 0
        for i in value:
            if s == i:
                k = findi(s, value)
                output = list[k]
                return output

    def click():
        mouse.click(Button.left,1)
    
    def move(move):
        mouse.position = move
        
    
    exit = 0
    def pwh():
        timeleft = int(tinput()) 
        print('Timematch:',timeleft,'seconds')
        while exit == 0:
            if keyboard.is_pressed('alt+s') == True:
                break
            try:
                try:
                    v, b = pyautogui.locateCenterOnScreen('Playok\sss.png',confidence=0.9)
##                  r = mouse.position
                
                    color = 'Black'
                except:
                    v, b = pyautogui.locateCenterOnScreen('Playok\pts.png',confidence=0.9)
                    color = 'White'
                k = (v,b)
                try:
                    tk = tmp
                except:
                    tk = ''
                tmp = returnpos(k)
                if tmp == None:
                    tmp = guess(k, value)
                    tmp = returnpos(tmp)
                if tk != tmp:
                    print('--> Moved:', tmp,'-',color)
                    moves = pktool(tmp,0)
                
                    if color == 'Black':
                        a = clock()
                        movet = playb(moves)
                        b = clock()
                        movet = pktool(movet,1)
                        pyautogui.moveTo(returnmove(movet))
                        click()
                        print('Engine move:',movet)
                        tl = round(round(b-a, 3) * 1000)
                        timeleft = timeleft - tl
                        print('-----------------------------------')
                        print('Time left:',timeleft / 1000,'second')
                        print('-----------------------------------')
                        timeleft(timeleft)
            except:
##                restart()
                continue

    def pbl():
##            keyboard.wait('Ctrl + B')
        timeleft = int(tinput()) 
        print('Timematch:',timeleft,'seconds')
        movet = begin()
        movet = pktool(movet,1)
        pyautogui.moveTo(returnmove(movet))
        click()
        while exit == 0:
            if keyboard.is_pressed('alt+s') == True:
                break
            try:
                try:
                    v, b = pyautogui.locateCenterOnScreen('Playok\sss.png',confidence=0.9)
##                  r = mouse.position
                
                    color = 'Black'
                except:
                    v, b = pyautogui.locateCenterOnScreen('Playok\pts.png',confidence=0.9)
                    color = 'White'
                k = (v,b)
                try:
                    tk = tmp
                except:
                    tk = ''
                tmp = returnpos(k)
                if tmp == None:
                    tmp = guess(k, value)
                    tmp = returnpos(tmp)
                if tk != tmp:
                    print('--> Moved:', tmp,'-',color)
                    moves = pktool(tmp,0)
                
                    if color == 'White':
                        a = clock()
                        movet = playw(moves)
                        b = clock()
                        movet = pktool(movet,1)
                        pyautogui.moveTo(returnmove(movet))
                        click()
                        print('Engine move:',movet)
                        tl = round(round(b-a, 3) * 1000)
                        timeleft = timeleft - tl
                        print('-----------------------------------')
                        print('Time left:',timeleft / 1000,'second')
                        print('-----------------------------------')
                        timeleft(timeleft)

            except:
##                restart()
                continue
        
    while True:
        if keyboard.is_pressed('alt+b') == True:
            pbl()
        if keyboard.is_pressed('alt+w') == True:
            pwh()
        if keyboard.is_pressed('alt+s') == True:
            restart()
            if keyboard.is_pressed('alt+b') == True:
                pbl()
            elif keyboard.is_pressed('alt+w') == True:
                pwh()
            pa = pyautogui.confirm('Play as?',title='Gomoku Bot',buttons=('Black','White'))
            if pa == 'Black':
                pbl()
            elif pa == 'White':
                pwh()
        if keyboard.is_pressed('esc') == True:
            close = pyautogui.confirm('Are you want to quit?',title='Gomoku Bot',buttons=('Yes','No'))
            if close == 'Yes':
                end()
                break
            else:
                continue
    

                    

                    
                
                
                


##        pyautogui.moveTo(v,b,duration=0.0)
        

    print('Game end!')

	

main()
os.system('pause>nul')
