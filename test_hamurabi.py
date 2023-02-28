import hamurabi
from hamurabi import (
    national_fink,
    no_can_do,
    not_enough_acres,
    not_enough_bushels,
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
        acres_to_sell = query_acres_to_sell(1, 10)
        assert acres_to_sell == 5

    def test_cannot_sell_negative_acres(self):
        with raises(SystemExit):
            hamurabi.input = lambda: -5
            acres_to_sell = query_acres_to_sell(1, 10)

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
