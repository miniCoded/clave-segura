Feature: Password Generation
  As a user
  I want to generate a secure password from a word
  So that I can have a strong password that's based on something I can remember

  Scenario: Generate secure password from word "sunshine"
    Given I enter the word "sunshine"
    When I request password generation
    Then a password should be generated
    And the password should be at least 16 characters long
    And the password should contain uppercase letters
    And the password should contain lowercase letters
    And the password should contain numbers
    And the password should contain symbols
    And the password should not contain obvious patterns

  Scenario: Generate password from word "password" (should avoid pattern)
    Given I enter the word "password"
    When I request password generation
    Then a password should be generated
    And the password should be at least 16 characters long
    And the password should not contain the word "password"

  Scenario: Generate password from word "admin"
    Given I enter the word "admin"
    When I request password generation
    Then a password should be generated
    And the password should be at least 16 characters long
    And the password should contain numbers and symbols

  Scenario: Generate password from empty word
    Given I enter an empty word
    When I request password generation
    Then no password should be generated
    And an error message should be displayed

  Scenario: Generate password from word "dragon"
    Given I enter the word "dragon"
    When I request password generation
    Then a password should be generated
    And the password should contain leet-speak substitutions like "9" for "g"

  Scenario: Generate password from word "trinity"
    Given I enter the word "trinity"
    When I request password generation
    Then a password should be generated
    And the password should be cryptographically secure
    And the password should have mixed case letters

  Scenario: Generate password from word "security"
    Given I enter the word "security"
    When I request password generation
    Then a password should be generated
    And the password should contain at least 3 numbers
    And the password should contain at least 2 symbols

  Scenario: Generate password from word "waterfall"
    Given I enter the word "waterfall"
    When I request password generation
    Then a password should be generated
    And the password should be shuffled and randomized
    And the password should be at least 16 characters long
