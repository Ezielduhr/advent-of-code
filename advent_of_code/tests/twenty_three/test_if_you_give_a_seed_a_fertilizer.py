from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from advent_of_code.settings import repo_root
from advent_of_code.twenty_three.if_you_give_a_seed_a_fertilizer import MapOMatic

feature_path = f"{repo_root}/features/twenty_three/if_you_give_a_seed_a_fertilizer.feature"


scenarios(feature_path)


@given(parsers.parse("mapping input is: {test_input}"), target_fixture='mapper')
def setup_soil_to_fertilizer_map(test_input):
    mapper = MapOMatic().generate_maps(test_input)

    yield mapper
    del mapper


@when(parsers.parse("looking up the seed numbers are: {lookup_input}"))
def lookup_seeds(mapper, lookup_input):
    mapper.lookup_seeds(lookup_input)


@then("the lowest location is 12")
def lookup_lowest_location():
    pass


def test_mapping(mapper):
    assert mapper.entire_chain == "seed-soil-fertilizer"


def test_no_map(mapper):
    assert mapper.lookup_seed("1") == 51


def test_simple_map(mapper):
    assert mapper.lookup_seed("3") == 13


def test_lowest_location(mapper):
    assert mapper.find_lowest_location() == 12
