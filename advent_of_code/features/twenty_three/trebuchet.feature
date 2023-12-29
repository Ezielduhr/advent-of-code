Feature:  TrebuchetCalibrator
  Somehow calibrates a trebuchet based on the first and last digit in a string

  Background: Setting up calibration tool
    Given calibration tool with the following input:
      | eightqrssm9httwogqshfxninepnfrppfzhsc |
      | one111jxlmc7tvklrmhdpsix              |
      | bptwone4sixzzppg                      |
      | ninezfzseveneight5kjrjvtfjqt5nineone  |
      |                                       |
      | 5b32                                  |
      | 1dtwone                               |
      | six7two7sixtwo78                      |
      | mvhsixpptztjh13sixthree2              |
      | six1bqqvrxndt                         |

  Scenario Outline: Finding first and last digit
    Given calibration tool is properly setup
    When running trebuchet calibration tool for <line>
    Then the first digit found is <first_digit>
    And the last digit found is <last_digit>
    And adding these two together creates <number>

    Examples:
      | line | first_digit | last_digit | number |
      | 1    | 9           | 9          | 99     |
      | 2    | 1           | 7          | 17     |
      | 3    | 4           | 4          | 44     |
      | 10   | 1           | 1          | 11     |

  Scenario: adding all found numbers together
    Given calibration tool is properly setup
    When summing all numbers together
    Then the outcome should be 379

  Scenario Outline: Finding first and last digit improved
    Given calibration tool is properly setup
    And calibration tool is set to improved version
    When running trebuchet calibration tool for <line>
    Then the first digit found is <first_digit>
    And the last digit found is <last_digit>
    And adding these two together creates <number>

    Examples:
      | line | first_digit | last_digit | number |
      | 1    | 8           | 9          | 89     |
      | 2    | 1           | 6          | 16     |
      | 3    | 2           | 6          | 26     |

  Scenario: adding all found numbers together improved
    Given calibration tool is properly setup
    And calibration tool is set to improved version
    When summing all numbers together
    Then the outcome should be 476