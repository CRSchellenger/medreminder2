from datetime import datetime,timedelta
from operator import contains
import time
from colorama import Fore,Back,Style
from termcolor import colored,cprint
import os
import requests, threading
import random, string
from gtts import gTTS
import smtplib
import webbrowser

#create files for main program
#<-- DO NOT EDIT THIS FUNCTION --> 
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
#<-- DO NOT EDIT THIS FUNCTION -->
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

        message = f'{mn} has been adminstered by {x} the next dose is due at {xtt}'
        emailc(message)

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

        message = f'{mn} has been adminstered by {o} the next dose is due at {ott}'
        emailc(message)

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

        message = f'{mn} has been adminstered by {ln} the next dose is due at {ltt}'
        emailc(message)

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

        message = f'{mn} has been adminstered by {tn} the next dose is due at {ttt}'
        emailc(message)

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

        message = f'{mn} has been adminstered by {ten} the next dose is due at {tte}'
        emailc(message)

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

        message = f'{mn} has been adminstered by {sen} the next dose is due at {ste}'
        emailc(message)

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
        fre = datetime.now() + timedelta(hours=0.1)

        fe = '-----------------' + '\n' + fen +' has administered '+ mn +' at '+ fet + '-----------------' 

        medfile = open('medfile', 'a')
        medfile.writelines(fe)
        medfile.close()
        medfile = open('medfile','r+')

        message = f'{mn} has been adminstered by {fen} the next dose is due at {fre}'
        emailc(message)

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
#GLOBAL VARIABLES 
global mn
global nm
#END GLOBAL VARIABLES 
#email conntection
#<-- DO NOT EDIT THIS FUNCTION -->
def emailc(message):
    e = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    e.ehlo
    e.starttls
    e.ehlo
    e.login("publicmedreminder@gmail.com","ahdn auvk bpnv vfeo")
    msg = f'''\
... Subject: Medreminder notifaction...
...
...  {message} ''' 
    e.sendmail("publicmedreminder@gmail.com",'schellengercrew@gmail.com', msg)
    e.quit
#endemail connection
#scheduled emails
#<-- DO NOT EDIT THIS FUNCTION -->
def sche():
    cnt = 0
    fl = open('medschedule','r')
    s = fl.readlines()
    td = datetime.now()
    for i in s:
        if i == td:
            cnt = 0
            message = f'Important notifaction from medreminder:{i} \nPlease log activity in medreminder so we can continue to remind you'
            emailc(message)
        else:
            if cnt <3:
                cnt = cnt+1
                k = threading.Timer(60,sche)
                k.start()
            elif cnt ==3:
                time.sleep(5.0)
                break
                

            
            
    fl.close()
#end scheduled emails 
#pill ident
#<-- DO NOT EDIT THIS FUNCTION -->
def pillid():
    print('<-- launching pill ident in a webbrowser -->')
    time.sleep(5.0)
    webbrowser.open_new('https://www.drugs.com/imprints.php')
#end pill ident 
#med interaction check
#<-- DO NOT EDIT THIS FUNCTION -->
def medint():
    print('<-- launching Medication interaction checker in a webbrowser -->')
    time.sleep(5.0)
    webbrowser.open_new('https://www.drugs.com/drug_interactions.html')
#end med interaction check
#<-- DO NOT EDIT THIS FUNCTION -->
def med_reminder():
    while True:
        #mrn()
        sche()
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
            di = input('\n**This is will open a webbrowser window**\n\nPlease enter med name that you would like to learn about: ')
            di.lower()
            message = 'Opening webbrowser' 
            print(message)
            print('\nYou can search for any drug in this system')
            time.sleep(5.0)
            webbrowser.open_new(f'https://www.drugs.com/{di}.html')
            


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
            print('For yes enter "yes" if no press enter')
            ni = input('Would you like to add any notes about todays visit?: ')
            td = time.strftime('%Y-%m-%d %H:%M:%S')
            if ni == 'yes':
                nn = input('Enter your notes now: ')
                d= '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse Notes: '+ nn + '\n-------------------------------------------'
                nv = open('nurse.txt', 'a')
                nv.writelines(d)
                nv.close()
                nv = open('nurse.txt','r+')
            else:

                e = '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse did not enter any notes'+'\n-------------------------------------------'

                nv1 = open('nurse.txt', 'a')
                nv1.writelines(e)
                nv1.close()
                nv1 = open('nurse.txt','r+')
                
        


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
            print('\n Admin meds - To log when you administered medication \n Med info - To get information about a specific medication \n Note - To log any notes \n Nurse - For a nurse to be able to log any notes about a specific visit \n Vitials - To log patient vitals \n Covid test - To log a covid test and what type was taken \n Print notes - Shows all notes in the system \n Print meds - Shows all meds in the system \n Print schedule - Shows a current and past schedule for the meds in the system \n Print activity - Shows all activity within a system and also shows who did a certain task and at which time \n Print covid test - Shows all past covid tests that have been logged into the system \n Pill ident - Helps you idenify unknown pills (this feature launches in a new window externally \n Med int - Helps you check interactions between two medications (this feature launches in a new window)\n Quit - To exit the system')
        #texttospeech() https://towardsdatascience.com/easy-text-to-speech-with-python-bfb34250036e

        elif ad.lower()  == 'pill ident':
            pillid()
        elif ad.lower() == 'med int':
            medint()


#main program call 
#<-- DO NOT ERASE -->
med_reminder()

