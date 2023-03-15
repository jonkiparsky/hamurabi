import hamurabi
from hamurabi import (
    Hamurabi,
    national_fink,
    no_can_do,
    not_enough_acres,
    not_enough_bushels,
    so_long,
    TERM_SUMMARY_INTRO,
    TERM_EVALUATION_LOUSY,
    TERM_EVALUATION_MEDIOCRE,
    TERM_EVALUATION_GREAT,
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

class TestPrintEndResult:
    def test_print_end_result_intro(capsys):
        instance = Hamurabi()
        acres_per_person = instance.acres_owned/instance.population

        with raises(SystemExit):
            instance.print_end_result()
            assert_in_stdout(TERM_SUMMARY_INTRO.format(
                death_rate=instance.avg_death_rate_per_year,
                cumulative_deaths=instance.cumulative_deaths,
                acres_per_person=acres_per_person))

    def test_print_end_result_summary_lousy(capsys):
        instance = Hamurabi()
        instance.avg_death_rate_per_year = 11
        acres_per_person = instance.acres_owned/instance.population

        with raises(SystemExit):
            instance.print_end_result()
            assert_in_stdout(TERM_EVALUATION_LOUSY)

    def test_print_end_result_mediocre(capsys):
        instance = Hamurabi()
        instance.avg_death_rate_per_year = 5
        acres_per_person = instance.acres_owned/instance.population
        random_number = .5
        haters = instance.population * .8 * random_number
        hamurabi.random = lambda: random_number

        with raises(SystemExit):
            instance.print_end_result()
            assert_in_stdout(TERM_EVALUATION_MEDIOCRE.format(haters))

    def test_print_end_result_great(capsys):
        instance = Hamurabi()
        acres_per_person = instance.acres_owned/instance.population
        with raises(SystemExit):
            instance.print_end_result()
            assert_in_stdout(TERM_EVALUATION_GREAT)

def test_print_intro(capsys):
    instance = Hamurabi()
    instance.print_intro()
    assert_in_stdout("CREATIVE COMPUTING MORRISTOWN", capsys)

class TestQueryBushelsToFeed():
    def test_can_feed_less_than_current_holdings(self):
        instance = Hamurabi()
        hamurabi.input = lambda: 5
        bushels_to_feed = instance.query_bushels_to_feed()
        assert bushels_to_feed == 5

    def test_exit_on_negative_input(self):
        instance = Hamurabi()
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            instance.query_bushels_to_feed()

    def test_cannot_feed_more_than_current_holdings(self):
        # oops! trying to test this will get us into a loop!
        pass

class TestQueryAcresToBuy():
    def test_can_spend_less_than_current_grain_holdings(self):
        instance = Hamurabi()
        instance.grain_holdings = 101
        hamurabi.input = lambda: 5
        acres_to_buy = instance.query_acres_to_buy(20)
        assert acres_to_buy == 5

    def test_cannot_buy_negative_acres(self):
        instance = Hamurabi()
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            acres_to_buy = instance.query_acres_to_buy(20)

    def test_cannot_spend_more_than_current_grain_holdings(self):
        # cannot test this now, due to loop
        pass


class TestQueryAcresToSell():
    def test_can_sell_less_than_current_land_holdings(self):
        instance = Hamurabi()
        hamurabi.input = lambda: 5
        acres_to_sell = instance.query_acres_to_sell()
        assert acres_to_sell == 5

    def test_cannot_sell_negative_acres(self):
        instance = Hamurabi()
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            acres_to_sell = instance.query_acres_to_sell()

    def test_cannot_sell_more_than_current_land_holdings(self):
        # cannot test this now, due to loop
        pass

class TestQueryAcresToSow():
    def test_can_sow_less_than_current_land_holdings(self):
        instance = Hamurabi()
        hamurabi.input = lambda: 5
        instance.query_acres_to_sow()
        assert instance.acres_to_sow == 5

    def test_sow_two_acres_per_bushel(self):
        instance = Hamurabi()
        initial_grain = instance.grain_holdings
        sown_acreage = 6
        hamurabi.input = lambda: sown_acreage
        instance.query_acres_to_sow()
        assert instance.grain_holdings == initial_grain - sown_acreage/2

    def test_cannot_sow_without_enough_grain(self):
        # cannot test this now, loop
        pass

    def test_not_enough_population_to_sow(self):
        # cannot test this now, loop
        pass

    def test_cannot_sow_negative_acreage(self):
        instance = Hamurabi()
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            instance.query_acres_to_sow()

    def test_can_sow_zero_acres(self):
        instance = Hamurabi()
        user_input = 0
        initial_acreage = instance.acres_owned
        hamurabi.input = lambda: user_input
        instance.query_acres_to_sow()
        assert instance.acres_owned == initial_acreage


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
        instance.rat_lossage = 70
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
        instance = Hamurabi()
        hamurabi.random_value = lambda: 3  # odd number means no rats
        sown = instance.acres_to_sow = 1000
        stored = instance.grain_holdings = 100
        instance.compute_harvest()
        assert instance.harvest == 3000
        assert instance.rat_lossage == 0
        assert instance.grain_holdings == stored - instance.rat_lossage + instance.harvest

    def test_harvest_with_rats(self):
        instance = Hamurabi()
        hamurabi.random_value = lambda: 2  # even number means rats
        sown = instance.acres_to_sow =1000
        stored = instance.grain_holdings = 100
        instance.compute_harvest()
        assert instance.harvest == 2000
        assert instance.rat_lossage == 50
        assert instance.grain_holdings == stored - instance.rat_lossage + instance.harvest

class TestComputeNewPopulation:
    def game_instance(self, **kwargs):
        instance = Hamurabi()

        instance.current_year = 2
        instance.deaths_this_turn = 2
        instance.immigration = 10
        instance.population = 100
        instance.plague_quotient = 1
        instance.acres_owned = 1000
        instance.yield_per_acre = 6
        instance.rat_lossage = 70
        instance.grain_holdings = 2000
        instance.avg_death_rate_per_year = 4
        instance.cumulative_deaths = 4
        for key, val in kwargs.items():
            setattr(instance, key, val)
        return instance

    def test_immigration(self):
        instance = self.game_instance()
        hamurabi.random_value = lambda: 2
        instance.compute_new_population(2000)
        assert instance.immigration == 5

    def test_plague(self):
        instance = self.game_instance()
        hamurabi.random = lambda: 0.15
        instance.compute_new_population(2000)
        assert instance.plague_quotient == 0

    def test_starve(self):
        instance = self.game_instance()
        instance.compute_new_population(1900)
        assert instance.deaths_this_turn == 5
        assert instance.cumulative_deaths == 9
        assert instance.avg_death_rate_per_year == 4.5

    def test_starve_with_impeachment(self):
        instance = self.game_instance()
        with raises(SystemExit):
            instance.compute_new_population(700)


class TestImpeach:
    def test_should_impeach(self):
        instance = Hamurabi()
        instance.deaths_this_turn = 451
        instance.population = 1000
        assert instance.impeach() is True

    def test_should_impeach(self):
        instance = Hamurabi()
        instance.deaths_this_turn = 449
        instance.population = 1000
        assert instance.impeach() is False


class TestAverageDeathRatePerYear:
    def test_average(self):
        instance = Hamurabi()
        instance.current_year = 5
        instance.avg_death_rate_per_year = 0.25

        instance.deaths_this_turn = 5
        instance.population = 1000
        assert instance.average_death_rate_per_year() == 0.3


class TestImmigration:
    def test_immigration(self):
        instance = Hamurabi()
        hamurabi.random_value = lambda: 2
        instance.compute_immigration()
        assert instance.immigration == 5
