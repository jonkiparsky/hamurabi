import hamurabi
from hamurabi import (
    compute_harvest,
    compute_new_population,
    Hamurabi,
    national_fink,
    no_can_do,
    not_enough_acres,
    not_enough_bushels,
    print_end_result,
    query_acres_to_buy,
    query_acres_to_sell,
    query_acres_to_sow,
    query_bushels_to_feed,
    so_long,
)
from pytest import (
    raises,
)

def assert_in_stdout(expected, captured):
    stdout, _ = captured.readouterr()
    assert expected in stdout

def assert_not_in_stdout(unexpected, captured):
    stdout, _ = captured.readouterr()
    assert unexpected not in stdout

def test_so_long():
    with raises(SystemExit):
        so_long()

def test_no_can_do(capsys):
    no_can_do()
    assert_in_stdout( "ANOTHER STEWARD", capsys)

def test_not_enough_bushels(capsys):
    not_enough_bushels(5)
    assert_in_stdout("5 BUSHELS OF GRAIN", capsys)

def test_not_enough_acres(capsys):
    not_enough_acres(200)
    assert_in_stdout("ONLY 200 ACRES", capsys)

def test_national_fink(capsys):
    with raises(SystemExit):
        national_fink(500)
    assert_in_stdout("STARVED 500 PEOPLE", capsys)

def test_print_end_result(capsys):
    # not much of a test, but it means the function can run
    with raises(SystemExit):
        print_end_result(1,2,3,4,5)
        assert_in_stdout("IN YOUR TEN-YEAR TERM", capsys)

def test_print_intro(capsys):
    instance = Hamurabi()
    instance.print_intro()
    assert_in_stdout("CREATIVE COMPUTING MORRISTOWN", capsys)

class TestQueryBushelsToFeed():
    def test_can_feed_less_than_current_holdings(self):
        hamurabi.input = lambda: 5
        Q = query_bushels_to_feed(10)
        assert Q == 5

    def test_exit_on_negative_input(self):
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            query_bushels_to_feed(10)

    def test_cannot_feed_more_than_current_holdings(self):
        # oops! trying to test this will get us into a loop!
        pass

class TestQueryAcresToBuy():
    def test_can_spend_less_than_current_grain_holdings(self):
        hamurabi.input = lambda: 5
        acres_to_buy = query_acres_to_buy(1, 10)
        assert acres_to_buy == 5

    def test_cannot_buy_negative_acres(self):
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            acres_to_buy = query_acres_to_buy(1, 10)

    def test_cannot_spend_more_than_current_grain_holdings(self):
        # cannot test this now, due to loop
        pass


class TestQueryAcresToSell():
    def test_can_sell_less_than_current_land_holdings(self):
        hamurabi.input = lambda: 5
        acres_to_sell = query_acres_to_sell(10)
        assert acres_to_sell == 5

    def test_cannot_sell_negative_acres(self):
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            acres_to_sell = query_acres_to_sell(10)

    def test_cannot_sell_more_than_current_land_holdings(self):
        # cannot test this now, due to loop
        pass

class TestQueryAcresToSow():
    def test_can_sow_less_than_current_land_holdings(self):
        hamurabi.input = lambda: 5
        acres_to_sow, grain_holdings = query_acres_to_sow(10, 100, 100)
        assert acres_to_sow == 5

    def test_sow_two_acres_per_bushel(self):
        hamurabi.input = lambda: 6
        acres_to_sow, grain_holdings = query_acres_to_sow(10, 3, 100)
        assert grain_holdings == 0

    def test_cannot_sow_without_enough_grain(self):
        # cannot test this now, loop
        pass

    def test_not_enough_population_to_sow(self):
        # cannot test this now, loop
        pass

    def test_cannot_sow_negative_acreage(self):
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            acres_to_sow, grain_holdings = query_acres_to_sow(10, 100, 100)

    def test_can_sow_zero_acres(self):
        user_input = 0
        initial_acreage = 100
        hamurabi.input = lambda: user_input
        result = query_acres_to_sow(initial_acreage, 100, 100)
        assert result == (user_input, initial_acreage)

class TestPrintStatusReport():
    def game_instance(self, **kwargs):
        instance = Hamurabi()

        instance.current_year = 1
        instance.deaths_this_turn = 20
        instance.immigration = 10
        instance.population = 90
        instance.plague_quotient = 1
        instance.acres_owned = 500
        instance.yield_per_acre = 6
        instance.bushels_eaten = 70
        instance.grain_holdings = 1000
        for key, val in kwargs.items():
            setattr(instance, key, val)
        return instance

    def test_year(self, capsys):
        instance = self.game_instance()
        instance.print_status_report()
        assert_in_stdout("IN YEAR 2", capsys)
        assert instance.current_year == 2

    def test_starved(self, capsys):
        instance = self.game_instance()
        instance.print_status_report()
        assert_in_stdout("20 PEOPLE STARVED", capsys)

    def test_immigration(self, capsys):
        instance = self.game_instance()
        instance.print_status_report()
        assert_in_stdout("10 CAME TO THE CITY", capsys)

    def test_plague(self, capsys):
        plague_quotient = 0
        immigration = 10
        old_pop = 100
        instance = self.game_instance(plague_quotient=plague_quotient,
                                      immigration=immigration,
                                      population=old_pop)
        instance.print_status_report()
        assert_in_stdout("A HORRIBLE PLAGUE", capsys)
        assert instance.population == int((old_pop + immigration)/2)

    def test_no_plague(self, capsys):
        instance = self.game_instance()
        instance.print_status_report()
        assert_not_in_stdout("A HORRIBLE PLAGUE", capsys)

    def test_population(self, capsys):
        immigration = 10
        old_pop = 90
        instance = self.game_instance(immigration=immigration, population=old_pop)

        instance.print_status_report()
        expected_new_population = old_pop + immigration
        assert_in_stdout("POPULATION IS NOW {}".format(expected_new_population), capsys)
        assert instance.population == expected_new_population

    def test_acres_owned(self, capsys):
        instance = self.game_instance()
        instance.print_status_report()
        assert_in_stdout("NOW OWNS 500 ACRES", capsys)

    def test_rats_ate(self, capsys):
        instance = self.game_instance()
        instance.print_status_report()
        assert_in_stdout("RATS ATE 70 BUSHELS", capsys)

    def test_bushels_in_store(self, capsys):
        instance = self.game_instance()
        instance.print_status_report()
        assert_in_stdout("NOW HAVE 1000 BUSHELS IN STORE", capsys)

class TestComputeHarvest:
    def test_harvest_no_rats(self):
        hamurabi.random_value = lambda: 3
        sown = 1000
        stored = 100
        harvest, bushels_eaten, grain_holdings, _ = compute_harvest(sown,
                                                                    stored)
        assert harvest == 3000
        assert bushels_eaten == 0
        assert grain_holdings == stored - bushels_eaten + harvest

    def test_harvest_with_rats(self):
        hamurabi.random_value = lambda: 2  # even number means rats
        sown = 1000
        stored = 100
        harvest, bushels_eaten, grain_holdings, _ = compute_harvest(sown, stored)
        assert harvest == 2000
        assert bushels_eaten == 50
        assert grain_holdings == stored - bushels_eaten + harvest

class TestComputeNewPopulation:
    def arguments(self, arg_updates=None):
        argnames = """acres_owned
        grain_holdings
        population
        avg_deaths_per_year
        deaths_this_turn
        cumulative_deaths
        current_year
        bushels_to_feed""".split()

        vals = [1000, 2000, 100, 4, 2, 4, 2, 2000]
        args_dict = dict(zip(argnames, vals))
        if arg_updates:
            args_dict.update(arg_updates)
        return args_dict

    def test_immigration(self):
        hamurabi.random_value = lambda: 2
        immigration = compute_new_population(**self.arguments())[0]
        assert immigration == 5

    def test_plague(self):
        hamurabi.random = lambda: 0.15
        plague_quotient = compute_new_population(**self.arguments())[1]
        assert plague_quotient == 0

    def test_starve(self):
        updated = {"bushels_to_feed": 1900}
        (avg_deaths_per_year,
         deaths_this_turn,
         cumulative_deaths) = compute_new_population(
            **self.arguments(updated))[3:]
        assert deaths_this_turn == 5
        assert cumulative_deaths == 9
        assert avg_deaths_per_year == 4.5

    def test_starve_with_impeachment(self):
        updated = {"bushels_to_feed": 700}
        with raises(SystemExit):
            compute_new_population(**self.arguments(updated))
