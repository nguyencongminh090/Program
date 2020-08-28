import subprocess, time
import os


engine = subprocess.Popen('Engine\Embryo\pbrain-embryo20_s.exe', universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
def put(command):
    engine.stdin.write(command+'\n')

def check():
    engine.stdin.write('start 15\n')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'OK':
##            print('Text:',text)
            break
def get():
    while True:
        try:
            text = engine.stdout.readline().strip()
            if (',' in text) == True:
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
    put('info timeout_match '+b)
    time.sleep(0)
    put('info timeout_turn '+b)
    time.sleep(0)
    put('INFO game_type 0')
    time.sleep(0)
    put('info rule 1')
    time.sleep(0)
    put('INFO time_left '+b)
    time.sleep(0)
    check()
    return a
a = timematch()
def tinput():
    return a
def begin():
    time.sleep(1)
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
    output = str(get())
    return output
def playb(inp):
##    while playing == True:
    put('turn ' + inp)
    return str(get())
def end():
    put('end')
def restart():
    put('RESTART')
def timeleft(a):
    put('info timeleft ' + str(a))
##print(playb('7,7'))
##print(playb('8,9'))
##print('tinput:',  tinput())



