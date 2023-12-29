Feature: MapOMatic
  Maps locations based on ranges of numbers e.g. from seed to fertilizer

  Background: Providing input for MapOMatic
    Given mapping input is:
      | seed-to-soil |
      | 2 52 2 |
      | 4 54 8 |
      | 99 990 1000 |
      | soil-to-fertilizer |
      | 1  51 1 |
      | 51 11 10 |
      | 990 100 1000 |

  Scenario: Find lowest seed
    Given the seed numbers are:
      | 1 2 3 10 101 1001 |
    When looking up lowest location
    Then the lowest location is 12
