import hamurabi
from hamurabi import (
    national_fink,
    no_can_do,
    not_enough_acres,
    not_enough_bushels,
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
