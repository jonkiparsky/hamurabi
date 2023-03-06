from random import random

def no_can_do():
    print("HAMMURABI, I CANNOT DO WHAT YOU WISH.")
    print("GET YOURSELF ANOTHER STEWARD!!!")

def so_long():
    print("SO LONG FOR NOW.")
    print()
    exit()

def not_enough_acres(acres_owned):  # line 720
    print ("HAMMURABI: THINK AGAIN. YOU OWN ONLY "+ str(acres_owned)+ " ACRES. NOW THEN,")

def not_enough_bushels(grain_holdings):
    print("HAMMURABI: THINK AGAIN. YOU HAVE ONLY")
    print(str(grain_holdings)+" BUSHELS OF GRAIN. NOW THEN, ")

def random_value():
    return int(random()*5)+1

def national_fink(deaths_this_turn):
    print()
    print("YOU STARVED "+str(deaths_this_turn)+" PEOPLE IN ONE YEAR!!!")
    print( "DUE TO THIS EXTREME MISMANAGEMENT YOU HAVE NOT ONLY")
    print("BEEN IMPEACHED AND THROWN OUT OF OFFICE BUT YOU HAVE")
    print("BEEN DECLARED NATIONAL FINK!!!")
    so_long()

def query_bushels_to_feed(grain_holdings):

    while True:
        print("HOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE")
        bushels_allocated_to_populace = int(input())
        if bushels_allocated_to_populace <= 0:
            no_can_do()
            so_long()
        if bushels_allocated_to_populace<grain_holdings:
            break
        else:
            not_enough_bushels(grain_holdings)
    return bushels_allocated_to_populace

def query_acres_to_buy(cost_per_acre, grain_holdings):
    print("LAND IS TRADING AT "+str(cost_per_acre)+" BUSHELS PER ACRE.")
    while True:
        print("HOW MANY ACRES DO YOU WISH TO BUY")
        acres_to_buy = int(input())
        if acres_to_buy < 0:
            no_can_do()
            so_long()
        if cost_per_acre * acres_to_buy < grain_holdings:
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


class Hamurabi:

    def __init__(self):
        self.cumulative_deaths = 0
        self.avg_deaths_per_year = 0
        self.current_year = 0
        self.population = 95
        self.grain_holdings = 2800
        self.harvest = 3000
        self.rat_lossage = self.harvest - self.grain_holdings
        self.yield_per_acre = 3
        self.acres_owned = self.harvest / self.yield_per_acre
        self.immigration = 5
        self.plague_quotient = 1
        self.deaths_this_turn = 0

    def print_intro(self):
        print("HAMMURABI".rjust(32))
        print("CREATIVE COMPUTING MORRISTOWN NEW JERSEY".rjust(15))
        print("\n"*2)
        print("TRY YOUR HAND AT GOVERNING ANCIENT SUMERIA")
        print("FOR A TEN YEAR TERM OF OFFICE")
        print()

    def print_status_report(self):
        print("\n\n")
        print("HAMMURABI I BEG TO REPORT TO YOU,")
        self.current_year = self.current_year + 1
        print("IN YEAR "+str(self.current_year) +
              ", " + str(self.deaths_this_turn) + " PEOPLE STARVED,"
              + str(self.immigration) +" CAME TO THE CITY,")
        self.population = self.population + self.immigration
        if self.plague_quotient <= 0:
            self.population = int(self.population / 2)
            print("A HORRIBLE PLAGUE STRUCK! HALF THE PEOPLE DIED")

        print("THE POPULATION IS NOW "+str(self.population))
        print("THE CITY NOW OWNS "+str(self.acres_owned)+" ACRES.")
        print("YOU HARVESTED "+str(self.yield_per_acre)+" BUSHELS PER ACRE.")
        print("RATS ATE "+str(self.rat_lossage)+" BUSHELS.")
        print("YOU NOW HAVE "+str(self.grain_holdings)+" BUSHELS IN STORE.");print()

    def play(self):

        self.print_intro()

        while True:
            self.print_status_report()
            if self.current_year==11:
                break
            C=int(10*random())
            cost_per_acre = C+17
            acres_to_buy = query_acres_to_buy(cost_per_acre, self.grain_holdings)
            if acres_to_buy != 0:
                self.acres_owned = self.acres_owned + acres_to_buy
                self.grain_holdings = self.grain_holdings - cost_per_acre * acres_to_buy
                C=0
            else:
                acres_to_sell = query_acres_to_sell(self.acres_owned)
                self.acres_owned = self.acres_owned - acres_to_sell
                self.grain_holdings = self.grain_holdings + cost_per_acre * acres_to_sell
                C=0
            print()

            bushels_to_feed = query_bushels_to_feed(self.grain_holdings)
            self.grain_holdings = self.grain_holdings - bushels_to_feed
            C=1;print()
            (self.deaths_this_turn,
             self.grain_holdings) = query_acres_to_sow(self.acres_owned,
                                                       self.grain_holdings,
                                                       self.population)

            (self.harvest,
             self.rat_lossage,
             self.grain_holdings,
             self.yield_per_acre) = compute_harvest(self.deaths_this_turn,
                                                    self.grain_holdings)
            (self.immigration,
             self.plague_quotient,
             self.population,
             self.avg_deaths_per_year,
             self.deaths_this_turn,
             self.cumulative_deaths) = compute_new_population(self.acres_owned,
                                                              self.grain_holdings,
                                                              self.population,
                                                              self.avg_deaths_per_year,
                                                              self.deaths_this_turn,
                                                              self.cumulative_deaths,
                                                              self.current_year,
                                                              bushels_to_feed)

        print_end_result(self.avg_deaths_per_year,
                         self.cumulative_deaths,
                         self.acres_owned,
                         self.population,
                         self.deaths_this_turn)

if __name__== "__main__":
    game = Hamurabi()
    game.play()
