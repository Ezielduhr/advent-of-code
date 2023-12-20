import pytest
from advent_of_code.twenty_three.if_you_give_a_seed_a_fertilizer import MapOMatic


@pytest.fixture
def mapper():
    test_input = """seeds: 1 2 3 10 101 1001

seed-to-soil map:
2 52 2
4 54 8
99 990 1000

soil-to-fertilizer map:
1  51 1
51 11 10 
990 100 1000"""
    mapper = MapOMatic().generate_maps(test_input)
    yield mapper
    del mapper


def test_mapping(mapper):
    assert mapper.entire_chain == "seed-soil-fertilizer"


def test_no_map(mapper):
    assert mapper.lookup_seed("1") == 51


def test_simple_map(mapper):
    assert mapper.lookup_seed("3") == 13


def test_lowest_location(mapper):
    assert mapper.find_lowest_location() == 12
