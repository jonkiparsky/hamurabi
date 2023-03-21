from random import random

TURN_COUNT = 10
def no_can_do():
    print("HAMMURABI, I CANNOT DO WHAT YOU WISH.")
    print("GET YOURSELF ANOTHER STEWARD!!!")

def so_long():
    print("SO LONG FOR NOW.")
    print()
    exit()

def random_value():
    return int(random()*5)+1

def not_enough_acres(acres_owned):  # line 720
    print ("HAMMURABI: THINK AGAIN. YOU OWN ONLY "+ str(acres_owned)+ " ACRES. NOW THEN,")

def not_enough_bushels(grain_holdings):
    print("HAMMURABI: THINK AGAIN. YOU HAVE ONLY")
    print(str(grain_holdings)+" BUSHELS OF GRAIN. NOW THEN, ")

def national_fink(deaths_this_turn):
    print()
    print("YOU STARVED "+str(deaths_this_turn)+" PEOPLE IN ONE YEAR!!!")
    print( "DUE TO THIS EXTREME MISMANAGEMENT YOU HAVE NOT ONLY")
    print("BEEN IMPEACHED AND THROWN OUT OF OFFICE BUT YOU HAVE")
    print("BEEN DECLARED NATIONAL FINK!!!")
    so_long()

def compute_plague_quotient():
    return int( 10 * (2 * random() -.3 ))


TERM_SUMMARY_INTRO = "\n".join([
    "IN YOUR TEN-YEAR TERM OF OFFICE, {death_rate} PERCENT OF THE",
    "POPULATION STARVED PER YEAR ON AVERAGE, I.E. A TOTAL OF",
    "{cumulative_deaths} PEOPLE DIED!!",
    "YOU STARTED WITH 10 ACRES PER PERSON AND ENDED WITH",
    "{acres_per_person} ACRES PER PERSON."])

TERM_EVALUATION_LOUSY = "\n".join([
        "YOUR HEAVY-HANDED PERFORMANCE SMACKS OF NERO AND IVAN IV",
        "THE PEOPLE (REMAINING) FIND YOU AN UNPLEASANT RULER AND",
        "FRANKLY, HATE YOUR GUTS!"])

TERM_EVALUATION_MEDIOCRE = "\n".join([
        "YOUR PERFORMANCE COULD HAVE BEEN SOMEWHAT BETTER, BUT",
        "REALLY, WASN'T TOO BAD AT ALL. {} PEOPLE",
        "DEARLY LIKE TO SEE YOU ASSASSINATED, BUT WE ALL HAVE OUR",
        "TRIVIAL PROBLEMS."])

TERM_EVALUATION_GREAT = "\n".join([
    "A FANTASTIC PERFORMANCE!!! CHARLEMAGNE, DISRAELI AND",
    "JEFFERSON COMBINED COULD NOT HAVE DONE BETTER!"])


def compute_population_fed(bushels_to_feed):
    return int(bushels_to_feed / 20)


class Hamurabi:

    def __init__(self):
        self.cumulative_deaths = 0
        self.avg_death_rate_per_year = 0
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

    def query_acres_to_buy(self, cost_per_acre):
        print("LAND IS TRADING AT "+str(cost_per_acre)+" BUSHELS PER ACRE.")
        while True:
            print("HOW MANY ACRES DO YOU WISH TO BUY")
            acres_to_buy = int(input())
            if acres_to_buy < 0:
                no_can_do()
                so_long()
            if cost_per_acre * acres_to_buy < self.grain_holdings:
                break
        return acres_to_buy

    def query_acres_to_sell(self):
        while True:
            print("HOW MANY ACRES DO YOU WISH TO SELL")
            acres_to_sell = int(input())
            if acres_to_sell < 0:
                no_can_do()
                so_long()
            if acres_to_sell >= self.acres_owned:
                not_enough_acres(self.acres_owned)
            else:
                break
        return acres_to_sell

    def query_bushels_to_feed(self):
        while True:
            print("HOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE")
            bushels_allocated_to_populace = int(input())
            if bushels_allocated_to_populace <= 0:
                no_can_do()
                so_long()
            if bushels_allocated_to_populace < self.grain_holdings:
                break
            else:
                not_enough_bushels(self.grain_holdings)
        return bushels_allocated_to_populace

    def query_acres_to_sow(self):
        while True:
            print("HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED")
            self.acres_to_sow = int(input())
            if self.acres_to_sow == 0:
                break
            if self.acres_to_sow<0:
                no_can_do()
                so_long()
            # ***TRYING TO PLANT MORE ACRES THAN YOU OWN?
            if self.acres_to_sow>=self.acres_owned:
                not_enough_acres(self.acres_owned)
                continue

            # ***ENOUGH GRAIN FOR SEED?
            if int(self.acres_to_sow / 2) > self.grain_holdings:
                not_enough_bushels(self.grain_holdings)
                continue
            # ***ENOUGH PEOPLE TO TEND THE CROPS?
            if self.acres_to_sow >= 10 * self.population:

                print("BUT YOU HAVE ONLY " + str(self.population) + " PEOPLE TO TEND THE FIELDS! NOW THEN, ")
                continue
            self.grain_holdings = self.grain_holdings - int(self.acres_to_sow / 2)
            break
        return self.acres_to_sow, self.grain_holdings

    def compute_harvest(self):
        self.yield_per_acre = random_value()
        self.harvest = self.acres_to_sow * self.yield_per_acre
        self.rat_lossage = 0
        C = random_value()
        if int(C/2) == C/2:
            # *** THE RATS ARE RUNNING WILD!
            self.rat_lossage = int(self.grain_holdings / C)
        self.grain_holdings = self.grain_holdings - self.rat_lossage + self.harvest

    def compute_immigration(self):
        self.immigration = int(random_value() *
                               (20 * self.acres_owned + self.grain_holdings) /
                               self.population / 100 + 1)

    def impeach(self):
        return self.deaths_this_turn > .45 * self.population

    def average_death_rate_per_year(self):
        return ((self.current_year - 1) * self.avg_death_rate_per_year +
                self.deaths_this_turn * 100 / self.population) / self.current_year

    def compute_new_population(self, bushels_to_feed):
        self.compute_immigration()
        population_fed = compute_population_fed(bushels_to_feed)
        self.plague_quotient = compute_plague_quotient()
        if self.population < population_fed:
            return (self.immigration, self.plague_quotient, self.population,
                    self.avg_death_rate_per_year, self.deaths_this_turn, self.cumulative_deaths)
        self.deaths_this_turn = self.population - population_fed
        if not self.impeach():
            self.avg_death_rate_per_year = self.average_death_rate_per_year()
            self.population = population_fed
            self.cumulative_deaths = self.cumulative_deaths + self.deaths_this_turn
        else:
            national_fink(self.deaths_this_turn)

    def print_end_result(self):
        acres_per_person = self.acres_owned / self.population
        print(TERM_SUMMARY_INTRO.format(death_rate=self.avg_death_rate_per_year,
                                        cumulative_deaths=self.cumulative_deaths,
                                        acres_per_person=acres_per_person))

        print()

        if self.avg_death_rate_per_year > 33:
            national_fink(self.deaths_this_turn)
        if acres_per_person < 7:
            national_fink(self.deaths_this_turn)
        if self.avg_death_rate_per_year > 10:
            print(TERM_EVALUATION_LOUSY)
            so_long()

        if self.avg_death_rate_per_year > 3 or acres_per_person < 10:
            haters = str(int(self.population * .8 * random()))
            print(TERM_EVALUATION_MEDIOCRE.format(haters))
            so_long()

        print(TERM_EVALUATION_GREAT)
        so_long()

    def buy_land(self, cost_per_acre):
        acres_to_buy = self.query_acres_to_buy(cost_per_acre)
        if acres_to_buy != 0:
            self.acres_owned = self.acres_owned + acres_to_buy
            self.grain_holdings = self.grain_holdings - cost_per_acre * acres_to_buy
            return acres_to_buy
        else:
            return 0

    def sell_land(self, cost_per_acre):
        acres_to_sell = self.query_acres_to_sell()
        self.acres_owned = self.acres_owned - acres_to_sell
        self.grain_holdings = self.grain_holdings + cost_per_acre * acres_to_sell

    def play(self):
        self.print_intro()
        while self.current_year < TURN_COUNT:
            self.print_status_report()
            cost_per_acre = int(10*random()) + 17
            acres_to_buy = self.buy_land(cost_per_acre)
            if acres_to_buy == 0:
                self.sell_land(cost_per_acre)

            print()

            bushels_to_feed = self.query_bushels_to_feed()
            self.grain_holdings = self.grain_holdings - bushels_to_feed
            self.query_acres_to_sow()
            self.compute_harvest()
            self.compute_new_population(bushels_to_feed)

        self.print_status_report()
        self.print_end_result()

if __name__== "__main__":
    game = Hamurabi()
    game.play()
