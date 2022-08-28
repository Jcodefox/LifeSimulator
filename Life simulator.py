print('Type ? for help')
print('Life simulator.\nversion 1.7.1\nNow celebrating 1179 lines of code!')
import os
from time import gmtime, strftime
from collections import deque
import time
if os.name == 'nt':
	import winsound
import os
import random
if os.name == 'nt':
	winsound.SND_ALIAS 
basket = []
dq=0
weather='clear'
working=0
mblhome=0
rnchhome=0
logcbn=0
burger=int(2)
os.environ['TZ'] = 'US/Eastern'
a=0
b=0
apm='am'
clkmin=strftime("%S", gmtime())
clkhr=int(6)
apples=int(2)
carrot=int(2)
money=float(1000.00)
happiness=int(100)
hunger = int(100)
clkhr1=int(1)
xxp=int(0)
payed=0
pantry=[]
checkpriceaple=0
checkpricecrrts=0
clkday=int(1)
clktick=':00'
home = 'tent'
location='Current location:'
print('day:',clkday)
work=0
shoe=0
mc=0
jobevent=0
microwave=2
apply=[]
xp=int(0)
jsec='seconds'
while b !='quit':
    homeshop=0
    park=0
    work=0
    clkhr1=clkhr+1
    clkhr=clkhr1
    print('You live in a',home)
    print(location,'In your',home)
    print(clkhr,clktick,apm)
    print('weather:',weather)
    b=input('...') #at home
    if weather!='rain':
        wet=int(random.randrange(10))
        if wet>8:
            print('RAIN!')
            weather='rain'
    else:
        dry=int(random.randrange(10))
        if dry>4:
            weather='dry'
    if weather=='rain':
        happy=int(random.randrange(-5,10))
        hppy=happiness-happy
        happiness=hppy
    else:
        happy=int(random.randrange(-10,1))
        hppy=happiness-happy
        happiness=hppy
    newaples=int(random.randrange(7)) #new apples determined
    newcrrt=int(random.randrange(5)) #new carrots determined
    reaples=newaples+apples
    recrrt=carrot+newcrrt
    apples=reaples
    carrot=recrrt
    newmicro=int(random.randrange(2)) #new microwaves determined
    remicro=microwave+newmicro
    microwave=remicro
    newbur=int(random.randrange(2)) #new burgers determined
    rebur=burger+newbur
    burger=rebur
    tpricemicro=float(random.uniform(59.99, 119.99)) #carrots priced
    xpricemicro=tpricemicro * 100
    ymicro=int(xpricemicro)
    zmicro=float(ymicro)
    pricemicro=zmicro / 100
    tpricebur=float(random.uniform(3.69, 4.99)) #carrots priced
    xpricebur=tpricebur * 100
    ybur=int(xpricebur)
    zbur=float(ybur)
    pricebur=zbur / 100
    tpricecrrts=float(random.uniform(0.99, 1.59)) #carrots priced
    tpriceaple=float(random.uniform(0.75, 1.29)) #apples priced
    xpricecrrts=tpricecrrts * 100
    ycrrts=int(xpricecrrts)
    zcrrts=float(ycrrts)
    pricecrrts=zcrrts / 100
    xpriceaple=tpriceaple * 100
    yaple=int(xpriceaple)
    zaple=float(yaple)
    priceaple=zaple / 100
    dollars=money
    hungry=int(random.randrange(3))
    hngr=hunger-hungry
    hunger=hngr
    pricefr=priceaple+pricecrrts
    rbevent=int(random.randrange(1,20))
    pnyevent=int(random.randrange(1,10))
    brevent=int(random.randrange(1,15))
    market='open'
    microtime=int(0)
    working=0
    walking=0
    pricemicro1=0
    if rbevent==1:
        print('RAINBOW')
        happiness=int(100)
        print(happiness,'% HAPPY')
        time.sleep(1)
    if pnyevent==1:
        print('OH,look a penny!')
        pennymny=money+0.01
        money=pennymny
        hppypnny=happiness+10
        happiness=hppypnny
        if happiness>100:
            happiness=int(100)
        print(happiness,'% HAPPY')
        time.sleep(1)
    if happiness>100:
        happiness=int(100)
    if shoe==1:
        shoepay=money+0.50
        money=shoepay
    if apm=='am':
        if clkhr<=7:
            market='closed'
    if apm=='pm':
        if clkhr>=9:
            market='closed'
    if clkhr ==11:
        if apm =='pm':
            clkadd=clkday+1
            clkday=clkadd
            apm=('am')
            print('day:',clkday)
        elif apm=='am':
            apm=('pm')
    if clkhr ==12:
        clkhr=int(0)
    if brevent <=1:
        if home=='tent':
            print('BEAR!')
            bearhappy=happiness-40
            happiness=bearhappy
            bear=int(random.randrange(15))
            time.sleep(2)
            print('.........')
            time.sleep(2.5)
            if bear ==15:
                print('You were eaten by a bear!')
                b='quit'
                time.sleep(5)
    if hunger<0:
        print('You starved to death.')
        b='quit'
        time.sleep(5)
    if money<=10:
        print('Low money.You have $',money)
    if b=='sell':
        print(pantry)
        print(apply)
        sell=input('sell what?:')
        if sell=='apple':
            if 'apple' in pantry:
                pantry.remove('apple')
                sellapple=money+0.75
                money=sellapple
        if sell=='bad apple':
            if 'bad apple' in pantry:
                print("can't sell")
        if sell=='carrots':
            if 'carrots' in pantry:
                pantry.remove('carrots')
                sellcrrt=money+0.99
                money=sellcrrt
        if sell=='cooked carrots':
            if 'cooked carrots' in pantry:
                pantry.remove('cookedcarrots')
                sellccrrt=money+2.40
                money=sellccrrt
        if sell=='burger':
            if 'burger' in pantry:
                pantry.remove('burger')
                sellbur=money+3.69
                money=sellbur
        if sell=='ok burger':
            if 'ok burger' in pantry:
                pantry.remove('ok burger')
                sellkbur=money+6.99
                money=sellkbur
        if sell=='microwave':
            if 'microwave' in apply:
                apply.remove('microwave')
                sellmicy=money+2.40
                money=sellmicy
    if b=='walk': #<----- b is primary input.
        while walking!='go home':
            market='open'
            if apm=='am':
                if clkhr<=7:
                    market='closed'
            if apm=='pm':
                if clkhr>=9:
                    market='closed'
            hungry=int(random.randrange(3))
            hngr=hunger-hungry
            hunger=hngr
            if weather!='rain':
                wet=int(random.randrange(10))
                if wet>8:
                    print('RAIN!')
                    weather='rain'
            else:
                dry=int(random.randrange(10))
                if dry>4:
                    weather='dry'
            if weather=='rain':
                happy=int(random.randrange(-10,10))
                hppy=happiness-happy
                happiness=hppy
            else:
                happy=int(random.randrange(-5,1))
                hppy=happiness-happy
                happiness=hppy 
            clkhr1=clkhr+1
            clkhr=clkhr1
            if clkhr ==11:
                if apm =='pm':
                    clkadd=clkday+1
                    clkday=clkadd
                    apm=('am')
                    print('day:',clkday)
                elif apm=='am':
                    apm=('pm')
            if clkhr ==12:
                clkhr=int(0)
            if happiness>100:
                happiness=int(100)
            print(location,'sidewalk somewhere')
            print('Current time:',clkhr,clktick,apm)
            walking=input('--->') #What does \a do?
            if walking=='?':          #<-----HELP FOR WALK HERE!
                print('Type store to go to store')
                time.sleep(1)
                print('Type go home to go home')
                time.sleep(1)
                print('Type park to go to the park')
                time.sleep(1)
                print('Type happiness for happy levels')
                time.sleep(1)
                print('Type hunger for hunger')
                time.sleep(1)
            if walking=='happiness':
                print(happiness,'% happy')
            if walking=='hunger':
                print('hunger is at:',hunger)
            if walking=='park':
                while park !='walk':
                    market='open'
                    if apm=='am':
                        if clkhr<=7:
                            market='closed'
                    if apm=='pm':
                        if clkhr>=9:
                            market='closed'
                    hungry=int(random.randrange(3))
                    hngr=hunger-hungry
                    hunger=hngr
                    print(location,'park')
                    print('Current time:',clkhr,clktick,apm)
                    if weather!='rain':
                        wet=int(random.randrange(10))
                        if wet>8:
                            print('RAIN!')
                            weather='rain'
                    else:
                        dry=int(random.randrange(10))
                        if dry>4:
                            weather='dry'
                    if weather=='rain':
                        happy=int(random.randrange(-15,10))
                        hppy=happiness-happy
                        happiness=hppy
                    else:
                        happy=int(random.randrange(-10,1))
                        hppy=happiness-happy
                        happiness=hppy
                    clkhr1=clkhr+1
                    clkhr=clkhr1
                    print('weather',weather)
                    if happiness>100:
                        happiness=int(100)
                    if clkhr ==11:
                        if apm =='pm':
                            clkadd=clkday+1
                            clkday=clkadd
                            apm=('am')
                            print('day:',clkday)
                        elif apm=='am':
                            apm=('pm')
                    if clkhr ==12:
                        clkhr=int(0)
                    park=input('---')
                    if park=='?':
                        print('Type walk to go back to walking')
                        time.sleep(1)
                        print('Type happiness for happy levels')
                        time.sleep(1)
                        print('Type hunger for hunger')
                        time.sleep(1)
                    if park=='happiness':
                        print(happiness,'% happy')
                    if park=='hunger':
                        print('hunger is at:',hunger)
            if walking=='store':#store
                isle=0
                payed=('enter')
                pricecrrts1=0
                priceaple1=0
                print(location,'store')
                if money >=0.01:
                    if market=='open':
                        while payed!='leave':
                            happy=int(random.randrange(-10,3))
                            hppy=happiness-happy
                            happiness=hppy
                            if happiness>100:
                                happiness=int(100)
                            print(happiness,'% happy')
                            isle=input('Which isle:')
                            if isle=='?':
                                print('Isle 1 food..')
                                time.sleep(1)
                                #print('Isle 2 hardware..')
                                #time.sleep(1)
                                #print('Isle 3 medications..')
                                #time.sleep(1)
                                print ('Isle 4 apliances')
                                time.sleep
                                print('checkout to pay and go')
                                time.sleep(1)
                            elif isle == '1':
                                diet=input('fr=fruits&vegis\nmeat=Meat')   #for later \nbrkfst=cereal\n...
                                if diet=='fr':
                                    if money >= 0.75:
                                        print('we have....')
                                        time.sleep(1)
                                        if apples>=1:
                                            if money >=priceaple:
                                                print(apples,'apple(s)$',priceaple,'...')
                                                time.sleep(1)
                                        if carrot>=1:
                                            if money >=pricecrrts:
                                                print(carrot,'bag(s) of Bb carrots $',pricecrrts,'...')
                                                time.sleep(1)
                                                pricecrrts1=pricecrrts
                                        fruit=input('===')
                                        if fruit=='apple':
                                            if apples>=1:
                                                if money >=priceaple:
                                                    basket.append("apple") 
                                                    priceaple1=priceaple          # apple arrives
                                                    print('Your basket contains:',basket)
                                                    red=apples-1
                                                    apples=red
                                        elif fruit=='carrots':
                                            if carrot>=1:
                                                if money >=pricecrrts:
                                                    basket.append("carrots")
                                                    pricecrrts1=pricecrrts
                                                    orange=carrot-1
                                                    carrot=orange
                                                    print('Your basket contains:',basket)
                                if diet=='meat':
                                    if money >=3.69:
                                        print('we have....')
                                        time.sleep(1)
                                        if burger>=1:
                                            if money >=pricebur:
                                                print(burger,'burger(s)(uncooked)(per pound)$',pricebur,'...')
                                                time.sleep(1)
                                        #if carrot>=1:
                                            #if money >=pricecrrts:
                                                #print(carrot,'bag(s) of Bb carrots $',pricecrrts,'...')
                                                #time.sleep(1)
                                                #pricecrrts1=pricecrrts
                                        me=input('===')
                                        if me=='burger':
                                            if burger>=1:
                                                if money >=pricebur:
                                                    basket.append("burger") 
                                                    pricebur1=pricebur         # apple arrives
                                                    print('Your basket contains:',basket)
                                                    rede=burger-1
                                                    burger=rede
                                        #elif fruit=='carrots':
                                            #if carrot>=1:
                                                #if money >=pricecrrts:
                                                    #basket.append("carrots")
                                                    #pricecrrts1=pricecrrts
                                                    #orange=carrot-1
                                                    #carrot=orange
                                                    #print('Your basket contains:',basket)
                            elif isle =='4':
                                if money>=59.99:
                                    print('We have.....')
                                    time.sleep(1)
                                    if microwave>=1:
                                        if money>=59.99:
                                            print(microwave,'microwave(s)$',pricemicro)
                                            time.sleep(1)
                                        whirlpool=input('===')
                                        if whirlpool=='microwave':
                                            if money >=pricemicro:
                                                basket.append("microwave")
                                                pricemicro1=pricemicro           # apple arrives
                                                print('Your basket contains:',basket)
                                                black=microwave-1
                                                microwave=black
                            elif isle =='checkout':
                                print(basket)
                                payit= input('Do you want to buy these:yes/no\n')
                                if payit=='yes':
                                    while 'apple' in basket:
                                        checkpriceaple=priceaple1
                                        basket.remove('apple')
                                        pantry.append("apple")
                                        priceaple1=priceaple1+priceaple
                                        #if 'apple' in basket:
                                            #priceaple1=priceaple1-priceaple    #probalem to high price
                                    while 'carrots' in basket:
                                        checkpricecrrts=pricecrrts1
                                        basket.remove('carrots')
                                        pantry.append("carrots")
                                        pricecrrts1=pricecrrts+pricecrrts1
                                    while 'microwave' in basket:
                                        checkpricemicro=pricemicro1
                                        basket.remove('microwave')
                                        apply.append("microwave")
                                        pricemicro1=pricemicro1+pricemicro
                                    while 'burger' in basket:
                                        checkpricebur=pricebur1
                                        basket.remove('burger')
                                        pantry.append("burger")
                                        pricebur1=pricebur1+pricebur
                                    if pricecrrts1 >=0.01:
                                        pricecrrts1=pricecrrts1-pricecrrts
                                    if priceaple1 >=0.01:
                                        priceaple1=priceaple1-priceaple #fixed probalem to high price
                                    if pricemicro1 >=0.01:
                                        pricemicro1=pricemicro1-pricemicro
                                    if pricebur1 >=0.01:
                                        pricebur1=pricebur1-pricebur
                                    checkpricebur=pricebur1
                                    checkpricecrrts=pricecrrts1
                                    checkpriceaple=priceaple1
                                    checkpricemicro=pricemicro1
                                    totalprice=checkpricecrrts+checkpriceaple+checkpricemicro+checkpricebur
                                    reciept=money-totalprice
                                    print('$',totalprice)
                                    money=reciept
                                    reciept=0
                                    totalprice=0
                                    checkpricecrrts=0
                                    checkpriceaple=0
                                    checkpricemicro=0
                                    print('Have a nice day.\nYou have $',money)
                                    del basket[:]
                                    payed='leave'
                                else :
                                    reciept=0
                                    payed=('leave')
                                    print('Have a nice day.')
                                    if 'microwave' in basket:
                                        black=microwave-1
                                        microwave=black
                                    if 'apple' in basket:
                                        red=apples-1
                                        apples=red
                                    if 'carrots' in basket:
                                        orange=carrot-1
                                        carrot=orange
                                    if 'burger' in basket:
                                        pink=burger-1
                                        burger=pink
                                    while 'apple' in basket:
                                        basket.remove('burger')
                                        red=burger+1
                                        burger=red
                                    while 'apple' in basket:
                                        basket.remove('apple')
                                        red=apples+1
                                        apples=red
                                    while 'carrots' in basket:
                                        basket.remove('carrots')
                                        orange=carrot+1
                                        carrot=orange
                                    while 'microwave' in basket:
                                        basket.remove('microwave')
                                        black=microwave+1
                                        microwave=black
    if b=='eat':
        print(pantry)
        mmm =input('What to eat?\n')
        if mmm=='apple':
            if 'apple' in pantry:
                eatapple=hunger+5
                hunger=eatapple
                pantry.remove('apple')
                print('Your hunger is at', hunger)
        if mmm=='bad apple':
            if 'bad apple' in pantry:
                eatbapple=hunger-5
                hunger=eatbapple
                pantry.remove('bad apple')
                print('you lose 5 hunger')
                print('Your hunger is at', hunger)
        if mmm=='carrots':
            if 'carrots' in pantry:
                eatcrrts=hunger+5
                hunger=eatcrrts
                pantry.remove('carrots')
                print('Your hunger is at', hunger)
        if mmm=='cooked carrots':
            if 'cooked carrots' in pantry:
                eatccrrts=hunger+10
                hunger=eatccrrts
                pantry.remove('cooked carrots')
                print('Your hunger is at', hunger)
        if mmm=='burger':
            if 'burger' in pantry:
                eatbur=hunger-2
                hunger=eatbur
                pantry.remove('burger')
                print('EW!\nLOSE 2 HUNGER!')
                print('Your hunger is at', hunger)
        if mmm=='ok burger':
            if 'ok burger' in pantry:
                eatkbur=hunger+20
                hunger=eatkbur
                pantry.remove('ok burger')
                print('Your hunger is at', hunger)
    if b=='?':
        print("Type quit to quit, but please don't")
        time.sleep(1)
        print('Type rtime for real time')
        time.sleep(1)
        print('Type $ for money')
        time.sleep(1)
        print('Type hunger for, of course, hunger')
        time.sleep(1)
        print('Type store to go to store. Sorry must walk to go to store')
        time.sleep(1)
        print('Type walk to go for a walk')
        time.sleep(1)
        print('Type versions for previous versions')
        time.sleep(1)
        print('Type job for joby stuff')
        time.sleep(1)
        print('Type real estate for home info')
        time.sleep(1)
        print('Type use to use items')
        time.sleep(1)
        print('Type happiness to see happiness')
        time.sleep(1)
    if b=='happiness':
        print(happiness,'% happy')
    if b=='rtime':
        a=strftime("Current time is %a, %d %b %Y %I:%M:%S", gmtime())
        print(a)
        time.sleep(3)
    if b=='use':
        if home!='tent':
            print(apply)
            user=input('use:')
            if user=='microwave':
                if 'microwave' in apply:
                    print(pantry)
                    usemicro=input('cook:')
                    if usemicro=='carrots':
                        if 'carrots' in pantry:
                            microtime=int(30)
                            while microtime!=0:
                                print('microwave ',microtime,jsec)
                                time.sleep(1)
                                microtime1=microtime-1
                                microtime=microtime1
                            pantry.append('cooked carrots')
                            pantry.remove('carrots')
                            print('Food')
                            if os.name == 'nt':
                            	winsound.Beep(1700, 1000)
                            time.sleep(0.5)
                            print('is')
                            if os.name == 'nt':
                            	winsound.Beep(1700, 1000)
                            time.sleep(0.5)
                            print('ready!')
                            if os.name == 'nt':
                            	winsound.Beep(1700, 1000)
                            	time.sleep(0.5)
                            	winsound.Beep(1700, 1500)
                            	time.sleep(1)
                    if usemicro=='burger':
                        if 'burger' in pantry:
                            microtime=int(240)
                            while microtime!=0:
                                print('microwave ',microtime,jsec)
                                time.sleep(1)
                                microtime1=microtime-1
                                microtime=microtime1
                            pantry.append('ok burger')
                            pantry.remove('burger')
                            print('Food')
                            if os.name == 'nt':
                            	winsound.Beep(1700, 1000)
                            time.sleep(0.5)
                            print('is')
                            if os.name == 'nt':
                            	winsound.Beep(1700, 1000)
                            time.sleep(0.5)
                            print('ready!')
                            if os.name == 'nt':
                            	winsound.Beep(1700, 1000)
                            	time.sleep(0.5)
                            	winsound.Beep(1700, 1500)
                            	time.sleep(1)
                    if usemicro=='apple':
                        if 'apple' in pantry:
                            microtime=int(30)
                            while microtime!=0:
                                print('microwave ',microtime,jsec)
                                time.sleep(1)
                                microtime1=microtime-1
                                microtime=microtime1
                            pantry.append('bad apple')
                            pantry.remove('apple')
                            print('Food')
                            winsound.Beep(1700, 1000)
                            time.sleep(0.5)
                            print('is')
                            winsound.Beep(1700, 1000)
                            time.sleep(0.5)
                            print('ready!')
                            winsound.Beep(1700, 1000)
                            time.sleep(0.5)
                            winsound.Beep(1700, 1500)
                            time.sleep(1)
    if b=='versions':
        print('1.0:The original')
        time.sleep(1)
        print('1.1:The tent update')
        time.sleep(1)
        print('1.2:The clock update')
        time.sleep(1)
        print('1.3:The work update')
        time.sleep(1)
        print('1.4:The house update')
        time.sleep(1)
        print('1.5:The happiness update')
	time.sleep(1)
	print('1.6:Undocumented update')
	time.sleep(1)
	print('1.7:The 1163 lines of code update')
	time.sleep(1)
	print('1.7.1:Universal update')
    if b=='$':
        print("You have $",money)
        time.sleep(1)
    if b=='hunger':
        print('hunger is',hunger)
    if b=='real estate':
        while homeshop!='go home':
            print(location,'real estate office.')
            homeshop=input('===')
            if homeshop=='?':
                print('Type search to look for homes.')
                time.sleep(1)
                print("Type info for home info")
                time.sleep(1)
                print("Type sell to sell home")
                time.sleep(1)
            if homeshop=='sell':
                if home=='Log cabin':
                    selllc=input('do you want to sell this Log cabin worth $140999 yes/no:')
                    if selllc=='yes':
                        home='tent'
                        logcbn=0
                        sldlc=money+140099
                        money=sldlc
                if home=='Ranch Home':
                    sellrh=input('do you want to sell this Ranch home worth $70999 yes/no:')
                    if sellrh=='yes':
                        home='tent'
                        rnchhome=0
                        sldrh=money+70099
                        money=sldrh
                if home=='Mobile home':
                    sellmh=input('do you want to sell this Mobile home worth $9099 yes/no:')
                    if sellmh=='yes':
                        home='tent'
                        mblhome=0
                        sldmh=money+9099
                        money=sldmh
            if homeshop=='info':
                print('you live in a:',home)
                if home=='Log cabin':
                    print('worth $150000')
                if home=='Ranch Home':
                    print('worth $80000')
                if home=='Mobile home':
                    print('worth $10000')
            if homeshop=='search':
                if mblhome==0:
                    print('mobile home $10000')
                    time.sleep(1)
                if rnchhome==0:
                    print('ranch home $80000')
                    time.sleep(1)
                if logcbn==0:
                    print ('log cabin $150000')
                    time.sleep(1)
                pckone=input('***')
                if pckone=='log cabin':
                    if money>=150000:
                        if logcbn==0:
                            if mblhome==0:
                                if rnchhome==0:
                                    sure=input('are you sure?yes/no:')
                                    if sure=='yes':
                                        bghtlgcbn=money-150000
                                        money=bghtlgcbn
                                        home='Log cabin'
                                        logcbn=1
                if pckone=='ranch home':
                    if money>=80000:
                        if rnchhome==0:
                            if mblhome==0:
                                if logcbn==0:
                                    sure=input('are you sure?yes/no:')
                                    if sure=='yes':
                                        bghtrnch=money-80000
                                        money=bghtrnch
                                        home='Ranch Home'
                                        rnchhome=1
                if pckone=='mobile home':
                    if money>=10000:
                        if mblhome==0:
                            if rnchhome==0:
                                if logcbn==0:
                                    sure=input('are you sure?yes/no:')
                                    if sure=='yes':
                                        bghtmblhm=money-10000
                                        money=bghtmblhm
                                        home='Mobile home'
                                        mblhome=1                                
    if b=='job':
        while work!='go home':
            work=input('>>>')
            if shoe==0:
                if mc==0:
                    mr=int(3)
            if work=='?':
                print('Type find job to find job.')
                time.sleep(1)
                print('Type view for job info.')
                time.sleep(1)
                print('Type go to work to work(and earn money!)')
                time.sleep(1)
                print('Type go home to go home')
                time.sleep(1)
            if work=='find job':
                print(mr,'jobs available:')
                time.sleep(1)
                if shoe==0:
                    if mc==0:
                        if dq==0:
                            print('shoeshinning')
                            time.sleep(1)
                if mc==0:
                    if shoe==0:
                        if dq==0:
                            print('mcducks')
                            time.sleep(1)
                if mc==0:
                    if shoe==0:
                        if dq==0:
                            print('dq need 5xp')
                            time.sleep(1)
                if shoe==0:
                    if mc==0:
                        if dq==0:
                            hire=input('---')
                            if hire=='shoeshinning':
                                print('hired 50 cents an hour\nno need to go to work.')
                                shoe=1
                            if hire=='mcducks':
                                print('hired about $7.50 an hour\nneed to go to work')
                                mc=1
                            if hire=='dq':
                                print('hired about $10.00 an hour\nneed to go to work')
                                dq=1
            if work=='view':
                if mc==1:
                    print('You are an cashier at mcducks for $7.50 an hour')
                if shoe==1:
                    print('You shoe shine for $0.50 an hour')
            if work=='go to work':
                if mc==1:
                    while working!='stop':
                        print(location,'mcducks')
                        working=input('...')
                        jobevent=0
                        jobevent=int(random.randrange(1,10))
                        clkhr1=clkhr+1
                        clkhr=clkhr1
                        if clkhr ==11:
                            if apm =='pm':
                                clkadd=clkday+1
                                clkday=clkadd
                                xxxp=xxp+1
                                xxp=xxxp
                                apm=('am')
                                print('day:',clkday)
                                if xxp>=7:
                                    xsp=xp+1
                                    xp=xsp
                                    xxp=int(0)
                            elif apm=='am':
                                apm=('pm')
                        if clkhr ==12:
                            clkhr=int(0)
                        happy=int(random.randrange(-10,3))
                        hppy=happiness-happy
                        happiness=hppy
                        if happiness>100:
                            happiness=int(100)
                        if happiness<=10:
                            t10mc=float(random.uniform(0.01, 0.50)) #carrots priced
                            x10mc=t10mc * 100
                            y10mc=int(x10mc)
                            z10mc=float(y10mc)
                            k10mcpay=z10mc / 100
                            k210mcpay=money+k10mcpay
                            mchap=k210mcpay
                            money=k210mcpay
                        elif happiness<=20:
                            t20mc=float(random.uniform(0.50, 1.00)) #carrots priced
                            x20mc=t20mc * 100
                            y20mc=int(x20mc)
                            z20mc=float(y20mc)
                            k20mcpay=z20mc / 100
                            k220mcpay=money+k20mcpay
                            mchap=k220mcpay
                            money=k220mcpay
                        elif happiness<=30:
                            t30mc=float(random.uniform(1.00, 1.50)) #carrots priced
                            x30mc=t30mc * 100
                            y30mc=int(x30mc)
                            z30mc=float(y30mc)
                            k30mcpay=z30mc / 100
                            k230mcpay=money+k30mcpay
                            mchap=k230mcpay
                            money=k230mcpay
                        elif happiness<=40:
                            t40mc=float(random.uniform(1.50, 2.00)) #carrots priced
                            x40mc=t40mc * 100
                            y40mc=int(x40mc)
                            z40mc=float(y40mc)
                            k40mcpay=z40mc / 100
                            k240mcpay=k40mcpay+money
                            mchap=k240mcpay
                            money=k240mcpay
                        elif happiness<=50:
                            t50mc=float(random.uniform(2.00, 2.50)) #carrots priced
                            x50mc=t50mc * 100
                            y50mc=int(x50mc)
                            z50mc=float(y50mc)
                            k50mcpay=z50mc / 100
                            k250mcpay=k50mcpay+money
                            mchap=k250mcpay
                            money=k250mcpay
                        elif happiness<=60:
                            t60mc=float(random.uniform(2.50, 3.00)) #carrots priced
                            x60mc=t60mc * 100
                            y60mc=int(x60mc)
                            z60mc=float(y60mc)
                            k60mcpay=z60mc / 100
                            k260mcpay=money+k60mcpay
                            mchap=k260mcpay
                            money=k260mcpay
                        elif happiness<=70:
                            t70mc=float(random.uniform(3.00, 3.50)) #carrots priced
                            x70mc=t70mc * 100
                            y70mc=int(x70mc)
                            z70mc=float(y70mc)
                            k70mcpay=z70mc / 100
                            k270mcpay=money+k70mcpay
                            mchap=k270mcpay
                            money=k270mcpay
                        elif happiness<=80:
                            t80mc=float(random.uniform(3.50, 4.00)) #carrots priced
                            x80mc=t80mc * 100
                            y80mc=int(x80mc)
                            z80mc=float(y80mc)
                            k80mcpay=z80mc / 100
                            k280mcpay=money+k80mcpay
                            mchap=k280mcpay
                            money=k280mcpay
                        elif happiness<=90:
                            t90mc=float(random.uniform(4.00, 7.49)) #carrots priced
                            x90mc=t90mc * 100
                            y90mc=int(x90mc)
                            z90mc=float(y90mc)
                            k90mcpay=z90mc / 100
                            k290mcpay=k90mcpay+money
                            mchap=k290mcpay
                            money=k290mcpay
                        elif happiness<=100:
                            k2100mcpay=money+7.50
                            mchap=k2100mcpay
                            money=k2100mcpay
                        hungry=int(random.randrange(6))
                        hngr=hunger-hungry
                        hunger=hngr
                        print('you have $',mchap)
                        print(happiness,'% happy')
                        time.sleep(0.5)
                        if working=='?':
                            print('Type eat to eat')
                            time.sleep(1)
                            print('Type stop to (you know) stop working')
                            time.sleep(1)
                        if working=='eat':
                            print('Choices:bigquack,lil burger,chicknuggets (6 pc)')
                            mcyds=input('Eat what?')
                            if mcyds=='bigquack':
                                eatbgmc=money-2.60
                                money=eatbgmc
                                atebgmc=hunger+10
                                hunger=atebgmc
                            if mcyds=='lil burger':
                                eatqtr=money-2.20
                                money=eatqtr
                                ateqtr=hunger+9
                                hunger=ateqtr
                            if mcyds=='chicknuggets':
                                eatnugget=money-1.40
                                money=eatnugget
                                atenugget=hunger+6
                                hunger=atenugget
                        if clkhr ==11:
                            if apm =='pm':
                                clkadd=clkday+1
                                clkday=clkadd
                                apm=('am')
                                print('day:',clkday)
                            elif apm=='am':
                                apm=('pm')
                        if clkhr ==12:
                            clkhr=int(0)
                        if jobevent==1:
                            jobeventdq=random.choice('de')
                            jobprblm=input('Someone orderd a blizzard\ndo you:\na:Tell them we do not have that and offer something else?\nb:Send them to DQ?')
                            if jobprblm=='a':
                                if jobeventdq==d:
                                    print('He left upset.\nYou lose $10')
                                    dqlose=money-10
                                    money=dqlose
                                if jobeventdq==e:
                                    print('He orderd a bigquack.\nYou gain $10')
                                    dqwin=money+10
                                    money=dqwin
                            else:
                                if jobeventdq==e:
                                    print('Your boss is mad.\nYou lose $10')
                                    dqlose1=money-10
                                    money=dqlose1
                                if jobeventdq==d:
                                    print('He left happy.\nYou gain $10')
                                    dqwin1=money+10
                                    money=dqwin1
                elif dq==1:
                    while working!='stop':
                        print(location,'dq')
                        working=input('~~~')
                        jobevent=0
                        jobevent=int(random.randrange(1,10))
                        clkhr1=clkhr+1
                        clkhr=clkhr1
                        if clkhr ==11:
                            if apm =='pm':
                                clkadd=clkday+1
                                clkday=clkadd
                                xxxp=xxp+1
                                xxp=xxxp
                                apm=('am')
                                print('day:',clkday)
                                if xxp>=7:
                                    xsp=xp+2
                                    xp=xsp
                                    xxp=int(0)
                            elif apm=='am':
                                apm=('pm')
                        if clkhr ==12:
                            clkhr=int(0)
                        happy=int(random.randrange(-10,3))
                        hppy=happiness-happy
                        happiness=hppy
                        if happiness>100:
                            happiness=int(100)
                        if happiness<=10:
                            t10mc=float(random.uniform(0.01, 1.00)) #carrots priced
                            x10mc=t10mc * 100
                            y10mc=int(x10mc)
                            z10mc=float(y10mc)
                            k10mcpay=z10mc / 100
                            k210mcpay=money+k10mcpay
                            mchap=k210mcpay
                            money=k210mcpay
                        elif happiness<=20:
                            t20mc=float(random.uniform(1.00, 2.00)) #carrots priced
                            x20mc=t20mc * 100
                            y20mc=int(x20mc)
                            z20mc=float(y20mc)
                            k20mcpay=z20mc / 100
                            k220mcpay=money+k20mcpay
                            mchap=k220mcpay
                            money=k220mcpay
                        elif happiness<=30:
                            t30mc=float(random.uniform(2.00, 3.00)) #carrots priced
                            x30mc=t30mc * 100
                            y30mc=int(x30mc)
                            z30mc=float(y30mc)
                            k30mcpay=z30mc / 100
                            k230mcpay=money+k30mcpay
                            mchap=k230mcpay
                            money=k230mcpay
                        elif happiness<=40:
                            t40mc=float(random.uniform(3.00, 4.00)) #carrots priced
                            x40mc=t40mc * 100
                            y40mc=int(x40mc)
                            z40mc=float(y40mc)
                            k40mcpay=z40mc / 100
                            k240mcpay=k40mcpay+money
                            mchap=k240mcpay
                            money=k240mcpay
                        elif happiness<=50:
                            t50mc=float(random.uniform(4.00, 5.00)) #carrots priced
                            x50mc=t50mc * 100
                            y50mc=int(x50mc)
                            z50mc=float(y50mc)
                            k50mcpay=z50mc / 100
                            k250mcpay=k50mcpay+money
                            mchap=k250mcpay
                            money=k250mcpay
                        elif happiness<=60:
                            t60mc=float(random.uniform(5.00, 6.00)) #carrots priced
                            x60mc=t60mc * 100
                            y60mc=int(x60mc)
                            z60mc=float(y60mc)
                            k60mcpay=z60mc / 100
                            k260mcpay=money+k60mcpay
                            mchap=k260mcpay
                            money=k260mcpay
                        elif happiness<=70:
                            t70mc=float(random.uniform(6.00, 7.00)) #carrots priced
                            x70mc=t70mc * 100
                            y70mc=int(x70mc)
                            z70mc=float(y70mc)
                            k70mcpay=z70mc / 100
                            k270mcpay=money+k70mcpay
                            mchap=k270mcpay
                            money=k270mcpay
                        elif happiness<=80:
                            t80mc=float(random.uniform(7.00, 8.00)) #carrots priced
                            x80mc=t80mc * 100
                            y80mc=int(x80mc)
                            z80mc=float(y80mc)
                            k80mcpay=z80mc / 100
                            k280mcpay=money+k80mcpay
                            mchap=k280mcpay
                            money=k280mcpay
                        elif happiness<=90:
                            t90mc=float(random.uniform(8.00, 9.00)) #carrots priced
                            x90mc=t90mc * 100
                            y90mc=int(x90mc)
                            z90mc=float(y90mc)
                            k90mcpay=z90mc / 100
                            k290mcpay=k90mcpay+money
                            mchap=k290mcpay
                            money=k290mcpay
                        elif happiness<=100:
                            k2100mcpay=money+10.00
                            mchap=k2100mcpay
                            money=k2100mcpay
                        hungry=int(random.randrange(6))
                        hngr=hunger-hungry
                        hunger=hngr
                        print('you have $',mchap)
                        print(happiness,'% happy')
                        time.sleep(0.5)
                        if working=='?':
                            print('Type eat to eat')
                            time.sleep(1)
                            print('Type stop to (you know) stop working')
                            time.sleep(1)
                        if working=='eat':
                            print('Choices:blizzard,dq burger,chicktenders (6 pc)')
                            mcyds=input('Eat what?')
                            if mcyds=='blizzard':
                                eatbgmc=money-2.50
                                money=eatbgmc
                                atebgmc=hunger+8
                                hunger=atebgmc
                            if mcyds=='dq burger':
                                eatqtr=money-2.20
                                money=eatqtr
                                ateqtr=hunger+12
                                hunger=ateqtr
                            if mcyds=='chicktenders':
                                eatnugget=money-1.40
                                money=eatnugget
                                atenugget=hunger+7
                                hunger=atenugget
                        if clkhr ==11:
                            if apm =='pm':
                                clkadd=clkday+1
                                clkday=clkadd
                                apm=('am')
                                print('day:',clkday)
                            elif apm=='am':
                                apm=('pm')
                        if clkhr ==12:
                            clkhr=int(0)
                        if jobevent==1:
                            jobeventdq=random.choice('ac')
                            jobprblm=input('Someone orderd a big quack\ndo you:\na:Tell them we do not have that and offer something else?\nb:Send them to Mcducks?')
                            if jobprblm=='a':
                                if jobeventdq=='a':
                                    print('He left upset.\nYou lose $20')
                                    dqlose=money-20
                                    money=dqlose
                                if jobeventdq=='c':
                                    print('He orderd a blizzzard.\nYou gain $20')
                                    dqwin=money+20
                                    money=dqwin
                            else:
                                if jobeventdq=='c':
                                    print('Your boss is mad.\nYou lose $20')
                                    dqlose1=money-20
                                    money=dqlose1
                                if jobeventdq=='a':
                                    print('He left happy.\nYou gain $20')
                                    dqwin1=money+20
                                    money=dqwin1
if os.name == 'nt':
	# Play Windows exit sound.
	winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
