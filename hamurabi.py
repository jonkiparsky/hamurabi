# initial pass: literal translation from BASIC to python
from random import random

def no_can_do():
    print("HAMMURABI, I CANNOT DO WHAT YOU WISH.")
    print("GET YOURSELF ANOTHER STEWARD!!!")

def so_long():
    print("SO LONG FOR NOW.")
    print()
    exit()

def not_enough_acres(A):  # line 720
    print ("HAMMURABI: THINK AGAIN. YOU OWN ONLY "+ str(A)+ " ACRES. NOW THEN,")

def not_enough_bushels(S):
    print("HAMMURABI: THINK AGAIN. YOU HAVE ONLY")
    print(str(S)+" BUSHELS OF GRAIN. NOW THEN, ")

def random_value():
    return int(random()*5)+1

def national_fink(D):
    print()
    print("YOU STARVED "+str(D)+" PEOPLE IN ONE YEAR!!!")
    print( "DUE TO THIS EXTREME MISMANAGEMENT YOU HAVE NOT ONLY")
    print("BEEN IMPEACHED AND THROWN OUT OF OFFICE BUT YOU HAVE")
    print("BEEN DECLARED NATIONAL FINK!!!")
    so_long()



print("HAMMURABI".rjust(32))
print("CREATIVE COMPUTING MORRISTOWN NEW JERSEY".rjust(15))
print("\n"*2)
print("TRY YOUR HAND AT GOVERNING ANCIENT SUMERIA")
print("FOR A TEN YEAR TERM OF OFFICE")
print()
D1=0; P1=0
Z=0;P=95;S=2800;H=3000;E=H-S
Y=3;A=H/Y;I=5;Q=1
D=0
while True:
    print("\n"*2)
    print("HAMMURABI I BEG TO REPORT TO YOU,")
    Z=Z+1
    print("IN YEAR "+str(Z)+", "+str(D)+" PEOPLE STARVED," + str(I) +" CAME TO THE CITY,")
    P=P+I
    if Q<=0:
        P=int(P/2)
        print("A HORRIBLE PLAGUE STRUCK! HALF THE PEOPLE DIED")

    print("THE POPULATION IS NOW "+str(P))
    print("THE CITY NOW OWNS "+str(A)+" ACRES.")
    print("YOU HARVESTED "+str(Y)+" BUSHELS PER ACRE.")
    print("RATS ATE "+str(E)+" BUSHELS.")
    print("YOU NOW HAVE "+str(S)+" BUSHELS IN STORE.");print()
    if Z==11:
        break
    C=int(10*random());Y=C+17
    print("LAND IS TRADING AT "+str(Y)+" BUSHELS PER ACRE.")
    print("HOW MANY ACRES DO YOU WISH TO BUY")
    Q=int(input())
    while True:
        if Q<0:
            no_can_do()
            so_long()
        if Y*Q<S:
            break
    if Q!=0:
        A=A+Q;S=S-Y*Q;C=0
    else:
        while True:
            print("HOW MANY ACRES DO YOU WISH TO SELL")
            Q = int(input())
            if Q<0:
                no_can_do()
                so_long()
            if Q>=A:
                not_enough_acres(A)
            else:
                break
        A=A-Q;S=S+Y*Q;C=0
    print()
    while True:
        print("HOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE")
        Q=int(input())
        if Q<=0:
            no_can_do()
            so_long()
        # TRYING TO USE MORE GRAIN THAN IN SILOS?
        if Q<S:
            break
        else:
            not_enough_bushels(S)

    S=S-Q;C=1;print()
    while True:
        print("HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED")
        D = int(input())
        if D==0:
            break
        if D<0:
            no_can_do()
            so_long()
        # ***TRYING TO PLANT MORE ACRES THAN YOU OWN?
        if D>=A:
            not_enough_acres(A)
            continue

        # ***ENOUGH GRAIN FOR SEED?
        if int(D/2) > S:
            not_enough_bushels(S)
            continue
        # ***ENOUGH PEOPLE TO TEND THE CROPS?
        if D>=10*P:

            print("BUT YOU HAVE ONLY "+str(P)+" PEOPLE TO TEND THE FIELDS! NOW THEN, ")
            continue
        S=S-int(D/2)
        break
    C = random_value()


    # ***A BOUNTIFUL HARVEST!
    Y = C; H=D*Y; E=0
    C = random_value()
    if int(C/2) == C/2:
        # *** THE RATS ARE RUNNING WILD!
        E = int(S/C)
    S = S-E+H
    C = random_value()
    # ***LETS HAVE SOME BABIES  ### actually, this is immigration...
    I=int(C*(20*A+S)/P/100+1)
    # ***HOW MANY PEOPLE HAD FULL BELLIES?
    C=int(Q/20)
    # ***HORROR, 15% CHANCE OF PLAGUE
    Q=int(10*(2*random()-.3))
    if P<C:
        continue

    # ***STARVE ENOUGH FOR IMPEACHMENT?
    D=P-C
    if D<=.45*P:
        P1=((Z-1)*P1+D*100/P)/Z
        P=C;D1=D1+D
        continue
    else:
        national_fink(D)

print( "IN YOUR TEN-YEAR TERM OF OFFICE, "+str(P1)+" PERCENT OF THE")
print( "POPULATION STARVED PER YEAR ON AVERAGE, I.E. A TOTAL OF")
print( str(D1)+" PEOPLE DIED!!"); L=A/P
print( "YOU STARTED WITH 10 ACRES PER PERSON AND ENDED WITH")
print( str(L)+" ACRES PER PERSON.")
print()
if P1>33:
    national_fink(D)
if L<7:
    national_fink(D)
if P1>10:
    print( "YOUR HEAVY-HANDED PERFORMANCE SMACKS OF NERO AND IVAN IV")
    print( "THE PEOPLE (REMAINING) FIND YOU AN UNPLEASANT RULER AND")
    print( "FRANKLY, HATE YOUR GUTS!")
    so_long()

if P1>3 or L<10:
    print( "YOUR PERFORMANCE COULD HAVE BEEN SOMEWHAT BETTER, BUT")
    print( "REALLY, WASN'T TOO BAD AT ALL. "+ str(int(P*.8*random()))+" PEOPLE")
    print( "DEARLY LIKE TO SEE YOU ASSASSINATED, BUT WE ALL HAVE OUR")
    print( "TRIVIAL PROBLEMS.")
    so_long()

print( "A FANTASTIC PERFORMANCE!!! CHARLEMAGNE, DISRAELI AND")
print( "JEFFERSON COMBINED COULD NOT HAVE DONE BETTER!")
so_long()
