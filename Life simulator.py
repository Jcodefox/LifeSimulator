print('Type ? for help')
print('Life simulator.\nversion 1.7.1\nNow celebrating 1179 lines of code!')
import os
from time import gmtime, strftime
import time
if os.name == 'nt':
    import winsound
    winsound.SND_ALIAS
    
def beep(freq, dur):
    if os.name == 'nt':
        winsound.Beep(freq, dur)
        
def microwave(microtime, item, new_item):
    if item in pantry:
        while microtime > 0:
            print('microwave ', microtime, jsec)
            time.sleep(1)
            microtime -= 1
        pantry.append(new_item)
        pantry.remove(item)
        print('Food')
        beep(1700, 1000)
        time.sleep(0.5)
        print('is')
        beep(1700, 1000)
        time.sleep(0.5)
        print('ready!')
        beep(1700, 1000)
        time.sleep(0.5)
        beep(1700, 1500)
        time.sleep(1)
                                
import random

basket = []
dq = 0
weather = 'clear'
working = 0
mblhome = 0
rnchhome = 0
logcbn = 0
burger = 2
os.environ['TZ'] = 'US/Eastern'
b = 0
apm = 'am'
clkmin = strftime("%S", gmtime())
clkhr = 6
apples = 2
carrot = 2
money = 1000.00
happiness = 100
hunger = 100
clkhr1 = 1
xxp = 0
payed = 0
pantry = []
checkpriceaple = 0
checkpricecrrts = 0
clkday = 1
home = 'tent'
print('day:', clkday)
work = 0
shoe = 0
mc = 0
jobevent = 0
microwave = 2
apply = []
xp = 0
jsec = 'seconds'

def change_happiness(amount, print_msg=False):
    global happiness
    happiness += amount
    happiness = max(0, min(happiness, 100))
    if print_msg:
        print(happiness,'% happy')
    
def change_weather():
    global weather
    if weather !=  'rain':
        if random.randint(1, 10) == 1:
            print('RAIN!')
            weather = 'rain'
    else:
        if random.randint(1, 100) <= 40:
            weather = 'dry'
            print("It is no longer raining")
    if weather == 'rain':
        change_happiness(random.randint(-10, 5))
    else:
        change_happiness(random.randint(-1, 10))
    
while b !=  'quit':
    homeshop = 0
    park = 0
    work = 0
    clkhr += 1
    print('You live in a', home)
    print('Current location:', 'In your', home)
    print(clkhr, ':00', apm)
    print('weather:', weather)
    b = input('...') #at home
    change_weather()
    apples += random.randrange(7)
    carrot += random.randrange(5)
    microwave += random.randrange(2)
    burger += random.randrange(2)
    pricemicro = int(random.uniform(59.99, 119.99) * 100) / 100.0
    pricebur = int(random.uniform(3.69, 4.99) * 100) / 100.0
    pricecrrts = int(random.uniform(0.99, 1.59) * 100) / 100.0
    priceaple = int(random.uniform(0.75, 1.29) * 100) / 100.0
    hunger -= random.randrange(3)
    pricefr = priceaple + pricecrrts
    market = 'open'
    microtime = 0
    working = 0
    walking = 0
    pricemicro1 = 0
    if random.randint(1, 20) == 1:
        print('RAINBOW')
        change_happiness(100, True)
        time.sleep(1)
    if random.randint(1, 10) == 1:
        print('OH, look a penny!')
        money += 0.01
        change_happiness(5, True)
        time.sleep(1)
    if shoe == 1:
        money += 0.50
    if (apm == 'am' and clkhr <= 7) or (apm == 'pm' and clkhr >= 9):
        market = 'closed'
    if clkhr == 11:
        if apm == 'pm':
            clkday += 1
            apm = 'am'
            print('day:', clkday)
        elif apm == 'am':
            apm = 'pm'
    if clkhr == 12:
        clkhr = 0
    if random.randint(1, 15) == 1 and home == 'tent':
        print('BEAR!')
        change_happiness(-40)
        time.sleep(2)
        print('.........')
        time.sleep(2.5)
        if random.randint(1, 15) == 15:
            print('You were eaten by a bear!')
            b = 'quit'
            time.sleep(5)
    if hunger < 0:
        print('You starved to death.')
        b = 'quit'
        time.sleep(5)
    if money <= 10:
        print('Low money.You have $', money)
    if b == 'sell':
        print(pantry)
        print(apply)
        sell = input('sell what?:')
        if sell == 'apple' and 'apple' in pantry:
            pantry.remove('apple')
            money += 0.75
        if sell == 'bad apple' and 'bad apple' in pantry:
            print("can't sell")
        if sell == 'carrots' and 'carrots' in pantry:
            pantry.remove('carrots')
            money += 0.99
        if sell == 'cooked carrots' and 'cooked carrots' in pantry:
            pantry.remove('cookedcarrots')
            money += 2.40
        if sell == 'burger' and 'burger' in pantry:
            pantry.remove('burger')
            money += 3.69
        if sell == 'ok burger' and 'ok burger' in pantry:
            pantry.remove('ok burger')
            money += 6.99
        if sell == 'microwave' and 'microwave' in apply:
            apply.remove('microwave')
            money += 2.40
    if b == 'walk': #<----- b is primary input.
        while walking != 'go home':
            market = 'open'
            if apm == 'am':
                if clkhr <= 7:
                    market = 'closed'
            if apm == 'pm':
                if clkhr >= 9:
                    market = 'closed'
            hunger -= random.randrange(3)
            change_weather()
            clkhr += 1
            if clkhr == 11:
                if apm == 'pm':
                    clkday += 1
                    apm = 'am'
                    print('day:', clkday)
                elif apm == 'am':
                    apm = 'pm'
            if clkhr == 12:
                clkhr = 0
            print('Current location:', 'sidewalk somewhere')
            print('Current time:', clkhr, ':00', apm)
            walking = input('--->')
            if walking == '?':          #<-----HELP FOR WALK HERE!
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
            if walking == 'happiness':
                print(happiness, '% happy')
            if walking == 'hunger':
                print('hunger is at:', hunger)
            if walking == 'park':
                while park != 'walk':
                    market = 'open'
                    if apm == 'am':
                        if clkhr <= 7:
                            market = 'closed'
                    if apm == 'pm':
                        if clkhr >= 9:
                            market = 'closed'
                    hunger -= random.randrange(3)
                    print('Current location:', 'park')
                    print('Current time:', clkhr, ':00', apm)
                    change_weather()
                    clkhr += 1
                    print('weather', weather)
                    if clkhr == 11:
                        if apm == 'pm':
                            clkday += 1
                            apm = 'am'
                            print('day:', clkday)
                        elif apm == 'am':
                            apm = 'pm'
                    if clkhr == 12:
                        clkhr = 0
                    park = input('---')
                    if park == '?':
                        print('Type walk to go back to walking')
                        time.sleep(1)
                        print('Type happiness for happy levels')
                        time.sleep(1)
                        print('Type hunger for hunger')
                        time.sleep(1)
                    if park == 'happiness':
                        print(happiness, '% happy')
                    if park == 'hunger':
                        print('hunger is at:', hunger)
            if walking == 'store': #store
                isle = 0
                payed = 'enter'
                pricecrrts1 = 0
                priceaple1 = 0
                print('Current location:', 'store')
                if money >= 0.01:
                    if market == 'open':
                        while payed != 'leave':
                            change_happiness(random.randint(-3, 10), True)
                            isle = input('Which isle:')
                            if isle == '?':
                                print('Isle 1 food..')
                                time.sleep(1)
                                #print('Isle 2 hardware..')
                                #time.sleep(1)
                                #print('Isle 3 medications..')
                                #time.sleep(1)
                                print ('Isle 4 apliances')
                                time.sleep(1)
                                print('checkout to pay and go')
                                time.sleep(1)
                            elif isle == '1':
                                diet = input('fr = fruits&vegis\nmeat = Meat')   #for later \nbrkfst = cereal\n...
                                if diet == 'fr':
                                    if money >= 0.75:
                                        print('we have....')
                                        time.sleep(1)
                                        if apples >= 1:
                                            if money >= priceaple:
                                                print(apples, 'apple(s)$', priceaple, '...')
                                                time.sleep(1)
                                        if carrot >= 1:
                                            if money >= pricecrrts:
                                                print(carrot, 'bag(s) of Bb carrots $', pricecrrts, '...')
                                                time.sleep(1)
                                                pricecrrts1 = pricecrrts
                                        fruit = input('===')
                                        if fruit == 'apple':
                                            if apples >= 1:
                                                if money >= priceaple:
                                                    basket.append("apple") 
                                                    priceaple1 = priceaple # apple arrives
                                                    print('Your basket contains:', basket)
                                                    apples -= 1
                                        elif fruit == 'carrots':
                                            if carrot >= 1:
                                                if money >= pricecrrts:
                                                    basket.append("carrots")
                                                    pricecrrts1 = pricecrrts
                                                    carrot -= 1
                                                    print('Your basket contains:', basket)
                                if diet == 'meat':
                                    if money >= 3.69:
                                        print('we have....')
                                        time.sleep(1)
                                        if burger >= 1:
                                            if money >= pricebur:
                                                print(burger, 'burger(s)(uncooked)(per pound)$', pricebur, '...')
                                                time.sleep(1)
                                        #if carrot > =1:
                                            #if money >= pricecrrts:
                                                #print(carrot, 'bag(s) of Bb carrots $', pricecrrts, '...')
                                                #time.sleep(1)
                                                #pricecrrts1 = pricecrrts
                                        me = input('===')
                                        if me == 'burger':
                                            if burger >= 1:
                                                if money >= pricebur:
                                                    basket.append("burger") 
                                                    pricebur1 = pricebur # apple arrives
                                                    print('Your basket contains:', basket)
                                                    burger -= 1
                                        #elif fruit == 'carrots':
                                            #if carrot >= 1:
                                                #if money >= pricecrrts:
                                                    #basket.append("carrots")
                                                    #pricecrrts1 = pricecrrts
                                                    #orange = carrot - 1
                                                    #carrot = orange
                                                    #print('Your basket contains:', basket)
                            elif isle == '4':
                                if money >= 59.99:
                                    print('We have.....')
                                    time.sleep(1)
                                    if microwave >= 1:
                                        if money >= 59.99:
                                            print(microwave, 'microwave(s)$', pricemicro)
                                            time.sleep(1)
                                        whirlpool = input('===')
                                        if whirlpool == 'microwave':
                                            if money >= pricemicro:
                                                basket.append("microwave")
                                                pricemicro1 = pricemicro # apple arrives
                                                print('Your basket contains:', basket)
                                                microwave -= 1
                            elif isle == 'checkout':
                                print(basket)
                                payit = input('Do you want to buy these:yes/no\n')
                                if payit == 'yes':
                                    pricebur1 = 0
                                    priceaple1 = 0
                                    pricecrrts1 = 0
                                    pricemicro1 = 0
                                    while 'apple' in basket:
                                        checkpriceaple = priceaple1
                                        basket.remove('apple')
                                        pantry.append("apple")
                                        priceaple1 = priceaple1 + priceaple
                                        #if 'apple' in basket:
                                            #priceaple1 = priceaple1-priceaple    #probalem to high price
                                    while 'carrots' in basket:
                                        checkpricecrrts = pricecrrts1
                                        basket.remove('carrots')
                                        pantry.append("carrots")
                                        pricecrrts1 = pricecrrts + pricecrrts1
                                    while 'microwave' in basket:
                                        checkpricemicro = pricemicro1
                                        basket.remove('microwave')
                                        apply.append("microwave")
                                        pricemicro1 = pricemicro1 + pricemicro
                                    while 'burger' in basket:
                                        checkpricebur = pricebur1
                                        basket.remove('burger')
                                        pantry.append("burger")
                                        pricebur1 = pricebur1 + pricebur
                                    if pricecrrts1 >= 0.01:
                                        pricecrrts1 = pricecrrts1 - pricecrrts
                                    if priceaple1 >= 0.01:
                                        priceaple1 = priceaple1 - priceaple #fixed probalem to high price
                                    if pricemicro1 >= 0.01:
                                        pricemicro1 = pricemicro1 - pricemicro
                                    if pricebur1 >= 0.01:
                                        pricebur1 = pricebur1 - pricebur
                                    totalprice = pricecrrts1 + priceaple1 + pricemicro1 + pricebur1
                                    print('$', totalprice)
                                    money -= totalprice
                                    print('Have a nice day.\nYou have $', money)
                                    basket.clear()
                                    payed = 'leave'
                                else :
                                    reciept = 0
                                    payed = ('leave')
                                    print('Have a nice day.')
                                    if 'microwave' in basket:
                                        microwave -= 1
                                    if 'apple' in basket:
                                        apples -= 1
                                    if 'carrots' in basket:
                                        carrot -= 1
                                    if 'burger' in basket:
                                        burger -= 1
                                    while 'apple' in basket:
                                        basket.remove('burger')
                                        burger += 1
                                    while 'apple' in basket:
                                        basket.remove('apple')
                                        apples += 1
                                    while 'carrots' in basket:
                                        basket.remove('carrots')
                                        carrot += 1
                                    while 'microwave' in basket:
                                        basket.remove('microwave')
                                        microwave += 1
    if b == 'eat':
        print(pantry)
        mmm  = input('What to eat?\n')
        if mmm == 'apple':
            if 'apple' in pantry:
                hunger += 5
                pantry.remove('apple')
                print('Your hunger is at', hunger)
        if mmm == 'bad apple':
            if 'bad apple' in pantry:
                hunger -= 5
                pantry.remove('bad apple')
                print('you lose 5 hunger')
                print('Your hunger is at', hunger)
        if mmm == 'carrots':
            if 'carrots' in pantry:
                hunger += 5
                pantry.remove('carrots')
                print('Your hunger is at', hunger)
        if mmm == 'cooked carrots':
            if 'cooked carrots' in pantry:
                hunger += 10
                pantry.remove('cooked carrots')
                print('Your hunger is at', hunger)
        if mmm == 'burger':
            if 'burger' in pantry:
                hunger -= 2
                pantry.remove('burger')
                print('EW!\nLOSE 2 HUNGER!')
                print('Your hunger is at', hunger)
        if mmm == 'ok burger':
            if 'ok burger' in pantry:
                hunger += 20
                pantry.remove('ok burger')
                print('Your hunger is at', hunger)
    if b == '?':
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
    if b == 'happiness':
        print(happiness, '% happy')
    if b == 'rtime':
        print(strftime("Current time is %a, %d %b %Y %I:%M:%S", gmtime()))
        time.sleep(3)
    if b == 'use':
        if home!= 'tent':
            print(apply)
            user = input('use:')
            if user == 'microwave':
                if 'microwave' in apply:
                    print(pantry)
                    usemicro = input('cook:')
                    if usemicro == 'carrots':
                        microwave(30, "carrots", "cooked carrots")
                    elif usemicro == 'burger':
                        microwave(30, "burger", "ok burger")
                    elif usemicro == 'apple':
                        microwave(30, "apple", "bad apple")
    if b == 'versions':
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
    if b == '$':
        print("You have $", money)
        time.sleep(1)
    if b == 'hunger':
        print('hunger is', hunger)
    if b == 'real estate':
        while homeshop != 'go home':
            print('Current location:', 'real estate office.')
            homeshop = input('===')
            if homeshop == '?':
                print('Type search to look for homes.')
                time.sleep(1)
                print("Type info for home info")
                time.sleep(1)
                print("Type sell to sell home")
                time.sleep(1)
            if homeshop == 'sell':
                if home == 'Log cabin':
                    selllc = input('do you want to sell this Log cabin worth $140999 yes/no:')
                    if selllc == 'yes':
                        home = 'tent'
                        logcbn = 0
                        money += 140099
                if home == 'Ranch Home':
                    sellrh = input('do you want to sell this Ranch home worth $70999 yes/no:')
                    if sellrh == 'yes':
                        home = 'tent'
                        rnchhome = 0
                        money += 70099
                if home == 'Mobile home':
                    sellmh = input('do you want to sell this Mobile home worth $9099 yes/no:')
                    if sellmh == 'yes':
                        home = 'tent'
                        mblhome = 0
                        money += 9099
            if homeshop == 'info':
                print('you live in a:', home)
                if home == 'Log cabin':
                    print('worth $150000')
                if home == 'Ranch Home':
                    print('worth $80000')
                if home == 'Mobile home':
                    print('worth $10000')
            if homeshop == 'search':
                if mblhome == 0:
                    print('mobile home $10000')
                    time.sleep(1)
                if rnchhome == 0:
                    print('ranch home $80000')
                    time.sleep(1)
                if logcbn == 0:
                    print ('log cabin $150000')
                    time.sleep(1)
                pckone = input('***')
                if pckone == 'log cabin':
                    if money >= 150000:
                        if logcbn == 0:
                            if mblhome == 0:
                                if rnchhome == 0:
                                    sure = input('are you sure?yes/no:')
                                    if sure == 'yes':
                                        money -= 150000
                                        home = 'Log cabin'
                                        logcbn = 1
                if pckone == 'ranch home':
                    if money >= 80000:
                        if rnchhome == 0:
                            if mblhome == 0:
                                if logcbn == 0:
                                    sure = input('are you sure?yes/no:')
                                    if sure == 'yes':
                                        money -= 80000
                                        home = 'Ranch Home'
                                        rnchhome = 1
                if pckone == 'mobile home':
                    if money >= 10000:
                        if mblhome == 0:
                            if rnchhome == 0:
                                if logcbn == 0:
                                    sure = input('are you sure?yes/no:')
                                    if sure == 'yes':
                                        money -= 10000
                                        home = 'Mobile home'
                                        mblhome = 1                                
    if b == 'job':
        while work != 'go home':
            work = input('>>>')
            if shoe == 0 and mc == 0:
                mr = 3
            if work == '?':
                print('Type find job to find job.')
                time.sleep(1)
                print('Type view for job info.')
                time.sleep(1)
                print('Type go to work to work(and earn money!)')
                time.sleep(1)
                print('Type go home to go home')
                time.sleep(1)
            if work == 'find job':
                print(mr, 'jobs available:')
                time.sleep(1)
                if shoe == 0 and mc == 0 and dq == 0:
                    print('shoeshinning')
                    time.sleep(1)
                if mc == 0 and shoe == 0 and dq == 0:
                    print('mcducks')
                    time.sleep(1)
                if mc == 0 and shoe == 0 and dq == 0:
                    print('dq need 5xp')
                    time.sleep(1)
                if shoe == 0 and mc == 0 and dq == 0:
                    hire = input('---')
                    if hire == 'shoeshinning':
                        print('hired 50 cents an hour\nno need to go to work.')
                        shoe = 1
                    if hire == 'mcducks':
                        print('hired about $7.50 an hour\nneed to go to work')
                        mc = 1
                    if hire == 'dq':
                        print('hired about $10.00 an hour\nneed to go to work')
                        dq = 1
            if work == 'view':
                if mc == 1:
                    print('You are an cashier at mcducks for $7.50 an hour')
                if shoe == 1:
                    print('You shoe shine for $0.50 an hour')
            if work == 'go to work':
                if mc == 1:
                    while working != 'stop':
                        print('Current location:', 'mcducks')
                        working = input('...')
                        jobevent = random.randrange(1,10)
                        clkhr += 1
                        if clkhr == 11:
                            if apm == 'pm':
                                clkday += 1
                                xxp += 1
                                apm = 'am'
                                print('day:', clkday)
                                if xxp >= 7:
                                    xp += 1
                                    xxp = 0
                            elif apm == 'am':
                                apm = 'pm'
                        if clkhr == 12:
                            clkhr = 0
                        happiness -= random.randrange(-10,3)
                        happiness = min(happiness, 100)
                        if happiness <= 10:
                            money += int(random.uniform(0.01, 0.50) * 100) / 100.0
                        elif happiness <= 20:
                            money += int(random.uniform(0.50, 1.00) * 100) / 100.0
                        elif happiness <= 30:
                            money += int(random.uniform(1.00, 1.50) * 100) / 100.0
                        elif happiness <= 40:
                            money += int(random.uniform(1.50, 2.00) * 100) / 100.0
                        elif happiness <= 50:
                            money += int(random.uniform(2.00, 2.50) * 100) / 100.0
                        elif happiness <= 60:
                            money += int(random.uniform(2.50, 3.00) * 100) / 100.0
                        elif happiness <= 70:
                            money += int(random.uniform(3.00, 3.50) * 100) / 100.0
                        elif happiness <= 80:
                            money += int(random.uniform(3.50, 4.00) * 100) / 100.0
                        elif happiness <= 90:
                            money += int(random.uniform(4.00, 7.49) * 100) / 100.0
                        elif happiness <= 100:
                            money += 7.50
                        hunger -= random.randrange(6)
                        print('you have $', money)
                        print(happiness, '% happy')
                        time.sleep(0.5)
                        if working == '?':
                            print('Type eat to eat')
                            time.sleep(1)
                            print('Type stop to (you know) stop working')
                            time.sleep(1)
                        if working == 'eat':
                            print('Choices:bigquack,lil burger,chicknuggets (6 pc)')
                            mcyds = input('Eat what?')
                            if mcyds == 'bigquack':
                                money -= 2.60
                                hunger += 10
                            if mcyds == 'lil burger':
                                money -= 2.20
                                hunger += 9
                            if mcyds == 'chicknuggets':
                                money -= 1.40
                                hunger += 6
                        if clkhr == 11:
                            if apm == 'pm':
                                clkday += 1
                                apm = 'am'
                                print('day:', clkday)
                            elif apm == 'am':
                                apm = 'pm'
                        if clkhr == 12:
                            clkhr = 0
                        if jobevent == 1:
                            jobprblm = input('Someone orderd a blizzard\ndo you:\na:Tell them we do not have that and offer something else?\nb:Send them to DQ?')
                            if jobprblm == 'a':
                                if random.randint(1, 2) == 1:
                                    print('He left upset.\nYou lose $10')
                                    money -= 10
                                else:
                                    print('He orderd a bigquack.\nYou gain $10')
                                    money += 10
                            else:
                                if random.randint(1, 2) == 1:
                                    print('Your boss is mad.\nYou lose $10')
                                    money -= 10
                                else:
                                    print('He left happy.\nYou gain $10')
                                    money += 10
                elif dq == 1:
                    while working != 'stop':
                        print('Current location:', 'dq')
                        working = input('~~~')
                        jobevent = random.randrange(1,10)
                        clkhr += 1
                        if clkhr == 11:
                            if apm == 'pm':
                                clkday += 1
                                xxp += 1
                                apm = 'am'
                                print('day:', clkday)
                                if xxp >= 7:
                                    xp += 2
                                    xxp = 0
                            elif apm == 'am':
                                apm = 'pm'
                        if clkhr == 12:
                            clkhr = 0
                        happiness -= random.randrange(-10,3)
                        happiness = min(happiness, 100)
                        if happiness <= 10:
                            money += int(random.uniform(0.01, 1.00) * 100) / 100.0
                        elif happiness <= 20:
                            money += int(random.uniform(1.00, 2.00) * 100) / 100.0
                        elif happiness <= 30:
                            money += int(random.uniform(2.00, 3.00) * 100) / 100.0
                        elif happiness <= 40:
                            money += int(random.uniform(3.00, 4.00) * 100) / 100.0
                        elif happiness <= 50:
                            money += int(random.uniform(4.00, 5.00) * 100) / 100.0
                        elif happiness <= 60:
                            money += int(random.uniform(5.00, 6.00) * 100) / 100.0
                        elif happiness <= 70:
                            money += int(random.uniform(6.00, 7.00) * 100) / 100.0
                        elif happiness <= 80:
                            money += int(random.uniform(7.00, 8.00) * 100) / 100.0
                        elif happiness<=90:
                            money += int(random.uniform(8.00, 9.00) * 100) / 100.0
                        elif happiness <= 100:
                            money += 10.00
                        hunger -= random.randrange(6)
                        print('you have $', money)
                        print(happiness, '% happy')
                        time.sleep(0.5)
                        if working == '?':
                            print('Type eat to eat')
                            time.sleep(1)
                            print('Type stop to (you know) stop working')
                            time.sleep(1)
                        if working == 'eat':
                            print('Choices:blizzard,dq burger,chicktenders (6 pc)')
                            mcyds = input('Eat what?')
                            if mcyds == 'blizzard':
                                money -= 2.50
                                hunger += 8
                            if mcyds == 'dq burger':
                                money -= 2.20
                                hunger += 12
                            if mcyds == 'chicktenders':
                                money -= 1.40
                                hunger += 7
                        if clkhr == 11:
                            if apm == 'pm':
                                clkday += 1
                                apm = 'am'
                                print('day:', clkday)
                            elif apm == 'am':
                                apm = 'pm'
                        if clkhr == 12:
                            clkhr = 0
                        if jobevent == 1:
                            jobprblm = input('Someone orderd a big quack\ndo you:\na:Tell them we do not have that and offer something else?\nb:Send them to Mcducks?')
                            if jobprblm == 'a':
                                if random.randint(1, 2) == 1:
                                    print('He left upset.\nYou lose $20')
                                    money -= 20
                                else:
                                    print('He orderd a blizzzard.\nYou gain $20')
                                    money += 20
                            else:
                                if random.randint(1, 2) == 1:
                                    print('Your boss is mad.\nYou lose $20')
                                    money -= 20
                                else:
                                    print('He left happy.\nYou gain $20')
                                    money += 20
if os.name == 'nt':
    # Play Windows exit sound.
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
