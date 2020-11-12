import subprocess, time
import os

f = open('Log.txt', 'a')
engine = subprocess.Popen('Engine\Embryo\pbrain-embryo20_s.exe', universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
def put(command):
    engine.stdin.write(command+'\n')
    f.write(command+'\n')

def check():
    engine.stdin.write('start 15\n')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'OK':
            f.write(text+'\n')
##            print('Text:',text)
            break
def get():
    while True:
        try:
            text = engine.stdout.readline().strip()
            if (',' in text) == True:
                f.write(text+'\n')
                return text
                break
        except:
            text = engine.stdout.readline().strip()
##        if text !='':
##            print(text)
##            time.sleep(0.5)
##            break
def timematch():
    tm = input('Time match: ')
    a = int(tm) * 1000
    b = str(a)
    put('INFO max_memory -1048576000')
    put('info timeout_match '+b)
    put('info timeout_turn '+b)
    put('INFO game_type 0')
    put('info rule 1')
    put('INFO time_left '+b)
    check()
    return a
a = timematch()
def tinput():
    return a
def begin():
    
    put('begin')
    output = str(get())
    return output
def playw(inp):
##    time.sleep(1)
##    put('begin')
##    time.sleep(2)
##    get()
##    time.sleep(1)
    put('turn ' + inp)
    a = getms()
    ev = a.split(' ')[4]
    output = str(get())
    return output, ev
def playb(inp):
##    while playing == True:
    put('turn ' + inp)
    a = getms()
    ev = a.split(' ')[4]
    return str(get()), ev
def end():
    put('end')
def restart():
    engine.stdin.write('RESTART'+'\n')
def timeleft(a):
    put('INFO time_left ' + str(a))
def getms():
    while True:
        try:
            text = engine.stdout.readline().strip()
            if ('MESSAGE' in text) == True:
                return text
                break
        except:
            text = engine.stdout.readline().strip()
def clse():
    f.close()
def debug():
    text = engine.stdout.read()
    f.write(text+'\n')
    return text
##    while True:
##        try:
##            text = engine.stdout.readline().strip()
##            if text != '':
##                f.write(text+'\n')
##                break
##        except:
##            text = engine.stdout.readline().strip()
    
##a = playb('7,7')
##print(a[0])
##print('Ev:',a[1])






