import os
import time
from time import perf_counter as clock
from pynput.mouse import Controller, Button
import pyautogui
from Coordinates import *
from connect import *
import keyboard
import win32api, win32con
from connect import timeleft as tmleft

mouse = Controller()

def main():
    p = mouse.position
    
    while True:
        try:
                x,y = pyautogui.locateCenterOnScreen('Kata\ptop.png')
                a = (x, y)
                break
        except:
                continue
    
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

    def click(a):
##        mouse.click(Button.left,1)
        win32api.SetCursorPos((a[0],a[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    def move(move):
        mouse.position = move
    def undo():
        try:
            try:
                v, b = pyautogui.locateCenterOnScreen('Kata\ccc.png',confidence=0.9)
                
                color = 'Black'
            except:
                v, b = pyautogui.locateCenterOnScreen('Kata\wht.png',confidence=0.8)
                color = 'White'
            k = (v,b)
            tmp = returnpos(k)
            if tmp == None:
                tmp = guess(k, value)
                tmp = returnpos(tmp)
            moves = pktool(tmp,0)
            put('takeback '+moves)
            print('Movek:',moves)
        except:
            time.sleep(0)
    
    exi = 0
    log = []
    def pwh(a):
        timeleft = a
##        timeleft = int(tinput()) 
        print('Timematch:',timeleft,'seconds')
        while exi == 0:
            if keyboard.is_pressed('alt+s') == True:
                break
            if keyboard.is_pressed('esc') == True:
                close = pyautogui.confirm('Are you want to quit?',title='Gomoku Bot',buttons=('Yes','No'))
                if close == 'Yes':
                    end()
                    exit()
                    break            
            try:
                try:
                    v, b = pyautogui.locateCenterOnScreen('Kata\ccc.png',confidence=0.9)
                
                    color = 'Black'
                except:
                    v, b = pyautogui.locateCenterOnScreen('Kata\wht.png',confidence=0.8)
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
                if keyboard.is_pressed('alt+u'):                    
                    undo()
                    x, y = pyautogui.locateCenterOnScreen('Kata\Back.png',confidence=0.9)
                    click((x,y))
                    undo()
                    click((x,y))
                    
                    
                if tk != tmp:
##                    print('--> Moved:', tmp,'-',color)
                    log.append(tmp)
                    moves = pktool(tmp,0)                    
                    if color == 'Black':                        
                        a = clock()
                        movet = playb(moves)
                        ev = movet[1]
                        print('--> Evaluation:',ev)
                        b = clock()
                        if ev == '-M0':
                            break
                        movet = pktool(movet[0],1)
                        moveto = returnmove(movet)
                        click(moveto)
##                        put('turn 14,7')
##                        print(debug())
                        if ev == '+M1':
                            break
                        ##print('Engine move:',movet)
                        tl = round(round(b-a, 3) * 1000)
                        timeleft = timeleft - tl
                        print('-----------------------------------')
                        print('Time left:',timeleft / 1000,'second')
                        print('-----------------------------------')
                        tmleft(timeleft)
                        
                            

            except:
##                restart()
                continue

    def pbl(a):
##            keyboard.wait('Ctrl + B')
##        timeleft = int(tinput())
        timeleft = a 
        print('Timematch:',timeleft,'seconds')
        movet = begin()
        movet = pktool(movet,1)
        moveto = returnmove(movet)
        click(moveto)
        while exi == 0:
            if keyboard.is_pressed('alt+s') == True:
                break
            if keyboard.is_pressed('esc') == True:
                close = pyautogui.confirm('Are you want to quit?',title='Gomoku Bot',buttons=('Yes','No'))
                if close == 'Yes':
                    end()                    
                    break
            if keyboard.is_pressed('alt+u'):                    
                    undo()
                    x, y = pyautogui.locateCenterOnScreen('Kata\Back.png',confidence=0.9)
                    click((x,y))
                    undo()
                    click((x,y))
            try:
                try:
                    v, b = pyautogui.locateCenterOnScreen('Kata\ccc.png')
##                  r = mouse.position
                
                    color = 'Black'
                except:
                    v, b = pyautogui.locateCenterOnScreen('Kata\wht.png',confidence=0.8)
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
                    ##print('--> Moved:', tmp,'-',color)
                    log.append(tmp)
                    moves = pktool(tmp,0)
                
                    if color == 'White':
                        a = clock()
                        movet = playw(moves)
                        b = clock()
                        ev = movet[1]
                        print('--> Evaluation:',ev)                        
                        if ev == '-M0':
                            break
                        movet = pktool(movet[0],1)
                        moveto = returnmove(movet)
                        click(moveto)
                        if ev == '+M1':
                            break
                        ##print('Engine move:',movet)
                        tl = round(round(b-a, 3) * 1000)
                        timeleft = timeleft - tl
                        print('-----------------------------------')
                        print('Time left:',timeleft / 1000,'second')
                        print('-----------------------------------')
                        tmleft(timeleft)
            except:
##                restart()
                continue
        
    while True:
        if keyboard.is_pressed('alt+b') == True:
            timeleft = int(tinput())
            pbl(timeleft)
        if keyboard.is_pressed('alt+w') == True:
            timeleft = int(tinput())
            pwh(timeleft)
        if keyboard.is_pressed('alt+s') == True:            
            outlog = ' '.join(log)
            log.clear()
            f = open('Log.ob','a')
            f.write('Game played\n')
            f.write('----------------\n\n')
            f.write(outlog + '\n')
            f.close()
            restart()            
            if keyboard.is_pressed('alt+b') == True:
                pbl()
            elif keyboard.is_pressed('alt+w') == True:
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

