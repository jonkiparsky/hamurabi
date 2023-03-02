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

def query_bushels_to_feed(S):
    # S: current grain holdings in bushels
    # returns Q = number of bushels to feed to population

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
    return Q

def query_acres_to_buy(yield_per_acre, grain_holdings):
    print("LAND IS TRADING AT "+str(yield_per_acre)+" BUSHELS PER ACRE.")
    while True:
        print("HOW MANY ACRES DO YOU WISH TO BUY")
        acres_to_buy = int(input())
        if acres_to_buy < 0:
            no_can_do()
            so_long()
        if yield_per_acre * acres_to_buy < grain_holdings:
            break
    return acres_to_buy

def query_acres_to_sell(acres_owned):
    # Y: price of land in bushels per acre
    # A: land owned in acres
    # returns Q = number of acres to sell
    while True:
        print("HOW MANY ACRES DO YOU WISH TO SELL")
        acres_to_sell = int(input())
        if acres_to_sell < 0:
            no_can_do()
            so_long()
        if acres_to_sell >= acres_owned:
            not_enough_acres(acres_owned)
        else:
            break
    return acres_to_sell

def query_acres_to_sow(acres_owned, grain_holdings, population):
    # A: land owned in acres
    # S: grain holdings in bushels
    # P: population in people
    # returns D = number of acres to sow and S = modified grain holdings
    while True:
        print("HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED")
        acres_to_sow = int(input())
        if acres_to_sow == 0:
            break
        if acres_to_sow<0:
            no_can_do()
            so_long()
        # ***TRYING TO PLANT MORE ACRES THAN YOU OWN?
        if acres_to_sow>=acres_owned:
            not_enough_acres(acres_owned)
            continue

        # ***ENOUGH GRAIN FOR SEED?
        if int(acres_to_sow / 2) > grain_holdings:
            not_enough_bushels(grain_holdings)
            continue
        # ***ENOUGH PEOPLE TO TEND THE CROPS?
        if acres_to_sow >= 10 * population:

            print("BUT YOU HAVE ONLY " + str(population) + " PEOPLE TO TEND THE FIELDS! NOW THEN, ")
            continue
        grain_holdings = grain_holdings - int(acres_to_sow / 2)
        break
    return acres_to_sow, grain_holdings

def print_intro():
    print("HAMMURABI".rjust(32))
    print("CREATIVE COMPUTING MORRISTOWN NEW JERSEY".rjust(15))
    print("\n"*2)
    print("TRY YOUR HAND AT GOVERNING ANCIENT SUMERIA")
    print("FOR A TEN YEAR TERM OF OFFICE")
    print()


def print_status_report(current_year,
                        deaths_this_turn,
                        immigration,
                        population,
                        plague_quotient,
                        acres_owned,
                        yield_per_acre,
                        bushels_eaten,
                        grain_holdings):
    print("\n\n")
    print("HAMMURABI I BEG TO REPORT TO YOU,")
    current_year = current_year + 1
    print("IN YEAR "+str(current_year) +
          ", " + str(deaths_this_turn) + " PEOPLE STARVED,"
          + str(immigration) +" CAME TO THE CITY,")
    population=population+immigration
    if plague_quotient <= 0:
        population=int(population / 2)
        print("A HORRIBLE PLAGUE STRUCK! HALF THE PEOPLE DIED")

    print("THE POPULATION IS NOW "+str(population))
    print("THE CITY NOW OWNS "+str(acres_owned)+" ACRES.")
    print("YOU HARVESTED "+str(yield_per_acre)+" BUSHELS PER ACRE.")
    print("RATS ATE "+str(bushels_eaten)+" BUSHELS.")
    print("YOU NOW HAVE "+str(grain_holdings)+" BUSHELS IN STORE.");print()
    return current_year, population


def compute_new_population(acres_owned,
                           grain_holdings,
                           population,
                           avg_deaths_per_year,
                           deaths_this_turn,
                           cumulative_deaths,
                           current_year,
                           bushels_to_feed):

    # ***LETS HAVE SOME BABIES  ### actually, this is immigration...
    immigration = int(random_value() * (20 * acres_owned + grain_holdings) / population / 100 + 1)
    # ***HOW MANY PEOPLE HAD FULL BELLIES?
    population_fed = int(bushels_to_feed / 20)
    # ***HORROR, 15% CHANCE OF PLAGUE
    plague_quotient = int( 10 * (2 * random() -.3 ))
    if population < population_fed:
        return (immigration, plague_quotient, population,
                avg_deaths_per_year, deaths_this_turn, cumulative_deaths)
    # ***STARVE ENOUGH FOR IMPEACHMENT?
    deaths_this_turn = population - population_fed
    if deaths_this_turn <= .45 * population:
        avg_deaths_per_year=((current_year - 1) * avg_deaths_per_year +
                             deaths_this_turn * 100 / population) / current_year
        population = population_fed
        cumulative_deaths = cumulative_deaths + deaths_this_turn
    else:
        national_fink(deaths_this_turn)
    return (immigration,
            plague_quotient,
            population,
            avg_deaths_per_year,
            deaths_this_turn,
            cumulative_deaths)


def print_end_result(avg_deaths_per_year, cumulative_deaths,
                     acres_owned, population, deaths_this_turn):

    print( "IN YOUR TEN-YEAR TERM OF OFFICE, " +str(avg_deaths_per_year)+ " PERCENT OF THE")
    print( "POPULATION STARVED PER YEAR ON AVERAGE, I.E. A TOTAL OF")
    print( str(cumulative_deaths)+" PEOPLE DIED!!")
    acres_per_person = acres_owned / population
    print( "YOU STARTED WITH 10 ACRES PER PERSON AND ENDED WITH")
    print( str(acres_per_person)+" ACRES PER PERSON.")
    print()
    if avg_deaths_per_year > 33:
        national_fink(deaths_this_turn)
    if acres_per_person < 7:
        national_fink(deaths_this_turn)
    if avg_deaths_per_year > 10:
        print( "YOUR HEAVY-HANDED PERFORMANCE SMACKS OF NERO AND IVAN IV")
        print( "THE PEOPLE (REMAINING) FIND YOU AN UNPLEASANT RULER AND")
        print( "FRANKLY, HATE YOUR GUTS!")
        so_long()

    if avg_deaths_per_year > 3 or acres_per_person < 10:
        print( "YOUR PERFORMANCE COULD HAVE BEEN SOMEWHAT BETTER, BUT")
        print( "REALLY, WASN'T TOO BAD AT ALL. "+ str(int(population * .8 * random()))+" PEOPLE")
        print( "DEARLY LIKE TO SEE YOU ASSASSINATED, BUT WE ALL HAVE OUR")
        print( "TRIVIAL PROBLEMS.")
        so_long()

    print( "A FANTASTIC PERFORMANCE!!! CHARLEMAGNE, DISRAELI AND")
    print( "JEFFERSON COMBINED COULD NOT HAVE DONE BETTER!")
    so_long()

def compute_harvest(acres_to_sow, grain_holdings):
    yield_per_acre = random_value()
    harvest = acres_to_sow * yield_per_acre
    bushels_eaten = 0
    C = random_value()
    if int(C/2) == C/2:
        # *** THE RATS ARE RUNNING WILD!
        bushels_eaten = int(grain_holdings / C)
    grain_holdings = grain_holdings - bushels_eaten + harvest
    return harvest, bushels_eaten, grain_holdings, yield_per_acre

def main():
    print_intro()
    D1=0; P1=0
    Z=0;P=95;S=2800;H=3000;E=H-S
    Y=3;A=H/Y;I=5;Q=1
    D=0
    while True:
        Z, P = print_status_report(Z, D, I, P, Q, A, Y, E, S)
        if Z==11:
            break
        C=int(10*random());Y=C+17
        Q = query_acres_to_buy(Y, S)
        if Q!=0:
            A=A+Q;S=S-Y*Q;C=0
        else:
            Q = query_acres_to_sell(A)
            A=A-Q;S=S+Y*Q;C=0
        print()

        Q = query_bushels_to_feed(S)
        S=S-Q;C=1;print()
        D, S = query_acres_to_sow(A, S, P)

        H, E, S, Y = compute_harvest(D, S)
        I, Q, P, P1, D, D1 = compute_new_population(A, S, P, P1, D, D1, Z, Q)

    print_end_result(P1, D1, A, P, D)
if __name__== "__main__":
    main()
