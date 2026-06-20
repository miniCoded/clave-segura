Feature: Password Security Rating
  As a user
  I want to rate the security of my password
  So that I can create secure passwords

  Scenario: Password is secure with exactly 12 characters and all requirements
    Given I enter a password "MyStr0ng@Pw9"
    When I submit the password
    Then the password should be rated as "secure"
    And the textbox should be colored "green"
    And the feedback should show all requirements met

  Scenario: Password is half-secure with 7-11 characters and all requirements
    Given I enter a password "MyP@ss99"
    When I submit the password
    Then the password should be rated as "half-secure"
    And the textbox should be colored "amber"
    And the feedback should indicate 7-11 characters

  Scenario: Password is unsafe with less than 7 characters
    Given I enter a password "Pass1!"
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"
    And the feedback should indicate too short

  Scenario: Password is unsafe without uppercase letters
    Given I enter a password "myp@ssw0rd1234"
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"

  Scenario: Password is unsafe without lowercase letters
    Given I enter a password "MYP@SSW0RD1234"
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"

  Scenario: Password is unsafe without numbers
    Given I enter a password "MyP@ssword"
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"

  Scenario: Password is unsafe without symbols
    Given I enter a password "MyPassword0123"
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"

  Scenario: Password is unsafe with obvious pattern
    Given I enter a password "Password123!abc"
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"
    And the feedback should indicate obvious patterns detected

  Scenario: Password is secure with mixed case, numbers, and symbols
    Given I enter a password "Tr0pic@lSunset!"
    When I submit the password
    Then the password should be rated as "secure"
    And the textbox should be colored "green"

  Scenario: Empty password is unsafe
    Given I enter an empty password
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"

  Scenario: Password with common pattern "123" is unsafe
    Given I enter a password "MyP@ss123word"
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"
    And the feedback should indicate obvious patterns detected

  Scenario: Password with common pattern "qwerty" is unsafe
    Given I enter a password "Qwerty@123abc"
    When I submit the password
    Then the password should be rated as "unsafe"
    And the textbox should be colored "red"
