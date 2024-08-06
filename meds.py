from datetime import datetime,timedelta
from operator import contains
import time
from colorama import Fore,Back,Style
from termcolor import colored,cprint
import os
import requests, threading
import random, string
from gtts import gTTS

#create files for main program
def mnf():

    ml = ['xanax','oxycodone','loratadine','tramadol','temazapam','senokot','fentanyl']
    a = file_path = 'medfile.txt'
    b = file_path =  'medschedule.txt'
    c = file_path = 'vitals.txt'
    d = file_path = 'notes.txt'
    e = file_path = 'nurse.txt'
    f = file_path = 'medlist.txt'
    g = file_path ='ct.txt'

    txt = 'This is a file for the medreminder program do not erase'

    with open (a,'w') as file:
        file.write(' ')
    
    with open (b,'w') as file:
        file.write(' ')
    
    with open (c,'w') as file:
        file.write(' ')

    with open (d,'w') as file:
        file.write(' ')

    with open (e,'w') as file:
        file.write(' ')

    with open (f,'w') as file:
        for i in ml:
            file.write(i +'\n')
    with open (g,'w') as file:
        file.write(' ')
# end create med list
mnf()
#write lines to text file and admin meds
def w2f(mn):
    if mn == 'xanax':
        x = input('Please enter your name: ')
        ct = time.strftime('%Y-%m-%d %H:%M:%S')
        mt = time.strftime('%H:%m')
        xtt = datetime.now() + timedelta(hours=5)
        r = '-----------------' + '\n' + x +' has administered '+ mn +' at '+ ct + '-----------------' 

        medfile = open('medfile', 'a')
        medfile.writelines(r)
        medfile.close()
        medfile = open('medfile', 'r+')

        print(Fore.WHITE+ Back.GREEN+'Xanax has been administered'+Style.RESET_ALL)
        print(Fore.WHITE+ Back.YELLOW+'next pill to be administered at '+ str(xtt) + Style.RESET_ALL)

        xsr = '\n' + str(xtt) +' xanax'
        xs = open('medschedule', 'a')
        xs.writelines(xsr)
        xs.close()
        xs = open('medschedule', 'r+')
        
    elif mn == 'oxycodone':    
        o = input('Please enter your name: ')
        rt = time.strftime('%Y-%m-%d %H:%M:%S')
        ot = time.strftime('%H:%m')
        ott = datetime.now() + timedelta(hours=4)

        oi = '-----------------' + '\n' + o +' has administered '+ mn +' at '+ rt + '-----------------' 

        medfile = open('medfile', 'a')
        medfile.writelines(oi)
        medfile.close()
        medfile = open('medfile','r+')

        print(Fore.WHITE + Back.GREEN +'oxycodone has been administered'+Style.RESET_ALL)
        print(Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(ott)+Style.RESET_ALL)

        osr = '\n' + str(ott) + ' oxycodone'
        os = open('medschedule', 'a')
        os.writelines(str(osr))
        os.close()
        os = open('medschedule', 'r+')
    
    elif mn == 'loratadine':
        ln = input('Please enter your name: ')
        lt = time.strftime('%Y-%m-%d %H:%M:%S')
        ltq = time.strftime('%H:%m')
        ltt = datetime.now() + timedelta(hours=24)

        li = '-----------------' +  '\n' + ln +' has administered '+ mn +' at '+ lt + '-----------------' 

        medfile = open('medfile', 'a')
        medfile.writelines(li)
        medfile.close()
        medfile = open('medfile','r+')

        print(Fore.WHITE + Back.GREEN + 'oxycodone has been administered'+Style.RESET_ALL)
        print(Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(ltt)+Style.RESET_ALL)

        lsr = '\n' + str(ltt) + ' loratadine'
        ls = open('medschedule', 'a')
        ls.writelines(str(lsr))
        ls.close()
        ls = open('medschedule', 'r+')
    
    elif mn == 'tramadol':
        tn = input('Please enter your name: ')
        tt = time.strftime('%Y-%m-%d %H:%M:%S')
        ttq = time.strftime('%H:%m')
        ttt = datetime.now() + timedelta(hours=6)

        ti = '-----------------'  + '\n' + tn +' has administered '+ mn +' at '+ tt + '-----------------' 

        medfile = open('medfile', 'a')
        medfile.writelines(ti)
        medfile.close()
        medfile = open('medfile','r+')

        print(Fore.WHITE + Back.GREEN+ 'Tramadol has been administered'+Style.RESET_ALL)
        print(Fore.WHITE + Back.YELLOW+ 'next pill to be administered at '+ str(ttt)+Style.RESET_ALL)

        tsr = '\n' + str(ttt) + ' tramadol'
        ts = open('medschedule', 'a')
        ts.writelines(str(tsr))
        ts.close()
        ts = open('medschedule', 'r+')
    
    elif mn == 'temazepam':
        ten = input('Please enter your name: ')
        tet = time.strftime('%Y-%m-%d %H:%M:%S')
        tte = time.strftime('%H:%m')
        tte = datetime.now() + timedelta(hours=24)

        te = '-----------------' +'\n' + ten +' has administered '+ mn +' at '+ tet + '-----------------'

        medfile = open('medfile', 'a')
        medfile.writelines(te)
        medfile.close()
        medfile = open('medfile','r+')

        print(Fore.WHITE + Back.GREEN +'temazepam has been administered'+Style.RESET_ALL)
        print(Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(tte)+Style.RESET_ALL)

        tse = '\n' + str(tte) + ' temazepam'
        te = open('medschedule', 'a')
        te.writelines(str(tse))
        te.close()
        te = open('medschedule', 'r+')
    
    elif mn == 'senokot':
        sen = input('Please enter your name: ')
        set = time.strftime('%Y-%m-%d %H:%M:%S')
        ste = time.strftime('%H:%m')
        ste = datetime.now() + timedelta(hours=12)

        se = '-----------------' +'\n' + sen +' has administered '+ mn +' at '+ set + '-----------------'

        medfile = open('medfile', 'a')
        medfile.writelines(se)
        medfile.close()
        medfile = open('medfile','r+')

        print(Fore.WHITE + Back.GREEN+'Senokot has been administered'+Style.RESET_ALL)
        print(Fore.WHITE + Back.YELLOW+'next pill to be administered at '+ str(ste)+Style.RESET_ALL)

        sse = '\n' + str(ste) + ' senokot'
        se = open('medschedule', 'a')
        se.writelines(str(sse))
        se.close()
        se = open('medschedule', 'r+')

    elif mn == 'fentanyl':
        fen = input('Please enter your name: ')
        fet = time.strftime('%Y-%m-%d %H:%M:%S')
        fte = time.strftime('%H:%m')
        fre = datetime.now() + timedelta(hours=24)

        fe = '-----------------' + '\n' + fen +' has administered '+ mn +' at '+ fet + '-----------------' 

        medfile = open('medfile', 'a')
        medfile.writelines(fe)
        medfile.close()
        medfile = open('medfile','r+')

        print(Fore.WHITE + Back.GREEN+'oxycodone has been administered'+Style.RESET_ALL)
        print(Fore.WHITE + Back.YELLOW+'next pill to be administered at '+ str(fre)+Style.RESET_ALL)

        fse = '\n' + str(fre) + ' fentanyl'
        fe = open('medschedule', 'a')
        fe.writelines(str(fse))
        fe.close()
        fe = open('medschedule', 'r+')


    else:
        print(Fore.WHITE + Back.RED+'Please enter med name' + '\n' + '-error 1'+Style.RESET_ALL)
# end write lines to text file. 
#TTS 
def tts(m,s):
    if s.lower() == 'n':
        language = 'en'
        ms = gTTS(text=m,lang=language,slow=False)
        ms.save('md_tts.mp3')
        os.system("start md_tts.mp3")
    
    elif s.lower() == 'y':
        ms = gTTS(text=m,lang=language,slow=True)
        ms.save('md_tts.mp3')
        os.system("start md_tts.mp3")

    else:
        print('error with file handling or error with tts.')
global m,s
#END TTS
def mrn():
        while True:
            mnf()
            ml()
            ps = open('medschedule', 'r')
            pi = ps.readlines()
            for i in pi:
                td = str(datetime.now())

                if td in i:
                    timer = threading.Timer(1.0,mrn)
                    timer.start()
                    message = f'{i} is due to be administered please make sure you log this actvity in the medreminder system. \n If you get lost and need help please type help in medreminder to see all options'
                    print(message)
                    return requests.post(
                    "https://api.mailgun.net/v3/sandbox167904bdf2224e25b135bd1143774c49.mailgun.org/messages",
                    auth=("api", "43ddbc2130afdb049e91f373ab8ab01b-381f2624-f5e1b8d6"),
                    data={"from": "Med reminder <postmaster@sandbox167904bdf2224e25b135bd1143774c49.mailgun.org>",
                    "to": "christopher schellenger <schellengercrew@gmail.com>",
                    "subject": "Hello christopher schellenger",
                    "text": (message)})
                elif td not in i:
                    pass
                else:
                    print(Fore.WHITE + Back.RED+'Error reading file please contact support' + '\n' + '-error 2'+Style.RESET_ALL)
                    timer.cancel()
global mn
global nm
def med_reminder():
    while True:

        #mrn()
        cprint('\n-----MED REMINDER-----','blue')
        ad = input('What would you like to do? ')
        if ad.lower() == 'admin meds':
            fr = open('medlist.txt', 'r')
            content = fr.read()
            print ('------Med list -------- \n '+ content)
            fr.close()
            mn = input('Please enter a med name: ')
            mn.lower()
            w2f(mn)

        elif ad.lower() == 'add meds':
            cprint('\n-----Add new meds-----','blue',attrs=['blink'])
            nm= input('Please enter med name that you would like to add to the system: ')
            medlist =open('medlist.txt', 'a')
            medlist.writelines('\n' + nm)
            medlist.close()
            medlist = open('\medlist.txt','r+')

        elif ad.lower() == 'med info':
            print('welcome to the med information section')
            di = input('Please enter med name that you would like to learn about: ')
            di.lower()
            if di == 'xanax' or di == 'alprazolam':
                xi = open('/Users/bubba/xanax drug info', 'r')
                xc = xi.read()
                print(xc)
                xi.close()

            elif di == 'oxycodone':
                oi = open('/Users/bubba/oi.text', 'r')
                oc = oi.read()
                print(oc)
                oi.close()

            elif di == 'loratadine':
                li = open('/Users/bubba/li.txt', 'r')
                lc = li.read()
                print(lc)
                li.close()

            elif di == 'tramadol':
                ti = open('/Users/bubba/ti.txt', 'r')
                tc = ti.read()
                print(tc)
                ti.close()

            elif di == 'temazepam':
                te = open('/Users/bubba/te.txt', 'r')
                tc = te.read()
                print(tc)
                te.close()


            elif di == 'senokot':
                si = open('/Users/bubba/si.txt', 'r')
                sc = si.read()
                print(sc)
                si.close()


            elif di == 'fentanyl':
                fi = open('/Users/bubba/fi.txt', 'r')
                fc = fi.read()
                print(fc)
                fi.close()


        elif ad.lower() == 'note':
            ntd = time.strftime('%Y-%m-%d %H:%M:%S')
            nt = input('Title: ')
            ntb = input('Note: ')

            n = '\n-------------------------------------------' +'\n'+ ntd + '\n' + nt + '\n' + ntb +'\n-------------------------------------------'

            note = open('/Users/bubba/notes.txt', 'a')
            note.writelines(n)
            note.close()
            note = open('/Users/bubba/notes.txt','r+')


        elif ad.lower() == 'print notes':
            ni = open('/Users/bubba/notes.txt', 'r')
            nc = ni.read()
            print(nc)
            ni.close()

        elif ad.lower() == 'vitials':
            bp = input('Enter Blood pressure: ')
            hr = input('Enter heart rate: ')
            sp = input('Enter SP02 rate: ')
            ctd = time.strftime('%Y-%m-%d %H:%M:%S')

            v = '\n-------------------------------------------'+'\n' +ctd +'\nBlood Pressure: '+ bp + '\nHeart Rate: '+hr + '\nSP02: ' + sp +'\n-------------------------------------------'

            note = open('/Users/bubba/vitals.txt', 'a')
            note.writelines(v)
            note.close()
            note = open('/Users/bubba/vitals.txt','r+')
        elif ad.lower() == 'print vitals':
            vi = open('/Users/bubba/vitals.txt', 'r')
            vc = vi.read()
            print(vc)
            vi.close()
        
        
        elif ad.lower() == 'nurse':
            ny = input('Please enter your name: ')
            ni = input('Would you like to add any notes about todays visit?: ')
            td = time.strftime('%Y-%m-%d %H:%M:%S')
            if ni == 'yes':
                nn = input('Enter your notes now: ')
                d= '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse Notes: '+ nn + '\n-------------------------------------------'
                nv = open('/Users/bubba/nurse.txt', 'a')
                nv.writelines(d)
                nv.close()
                nv = open('/Users/bubba/nurse.txt','r+')
            else:

                e = '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse did not enter any notes'+'\n-------------------------------------------'

                nv1 = open('/Users/bubba/nurse.txt', 'a')
                nv1.writelines(e)
                nv1.close()
                nv1 = open('/Users/bubba/nurse.txt','r+')
                
        


        elif ad.lower() == 'covid test':
            print('Types of tests are Anitgen and PCR')
            pn = input('Please enter the name of the person this test was performed on: ')
            ctt = input ('Please enter the the type of test you have taken: ')
            print('--------------------------------')
            print('pos,neg')
            ttr = input('Please enter the result of the test: ')
            if ttr == 'pos':
                print(Fore.BLACK + Back.RED +'\nPlease isolate for 5 days to ensure the virus does not spread' + Style.RESET_ALL)
            else:
                pass
            tdd = time.strftime('%Y-%m-%d %H:%M:%S')

            cttr = '\n-------------------------------------------'+'\n' +tdd +'\nName of the person this test was performed on: ' + pn +'\ntype of test taken: ' + ctt + '\nResult of the test: ' + ttr +'\n-------------------------------------------'

            covid = open('/Users/bubba/ct.txt', 'a')
            covid.writelines(cttr)
            covid.close()
            covid = open('/Users/bubba/ct.txt','r+')

        elif ad.lower() == 'print meds':
            ml = open('medlist.txt', 'r')
            mi = ml.read()
            print(mi)
            ml.close()

        elif ad.lower() == 'print schedule':
            ps = open('medschedule', 'r')
            pi = ps.read()
            print(pi)
            ps.close()
        elif ad.lower() == 'print activity':
            at = open('medfile', 'r')
            ai = at.read()
            print(ai)
            at.close()
        elif ad.lower() == 'print covid test':
            ct = open('/Users/bubba/ct.txt', 'r')
            ci = ct.read()
            print(ci)
            ct.close()
        elif ad.lower() == 'quit':
            print('Closing system...')
            time.sleep(0.5)
            break

        elif ad.lower() == 'help':
            print('------ Terms within the system ------')
            print('\n Admin meds - To log when you administered medication \n Med info - To get information about a specific medication \n Note - To log any notes \n Nurse - For a nurse to be able to log any notes about a specific visit \n Vitials - To log patient vitals \n Covid test - To log a covid test and what type was taken \n Print notes - Shows all notes in the system \n Print meds - Shows all meds in the system \n Print schedule - Shows a current and past schedule for the meds in the system \n Print activity - Shows all activity within a system and also shows who did a certain task and at which time \n Print covid test - Shows all past covid tests that have been logged into the system \n Quit - To exit the system')
        #texttospeech() https://towardsdatascience.com/easy-text-to-speech-with-python-bfb34250036e
med_reminder()

