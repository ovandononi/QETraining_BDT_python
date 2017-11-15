before_feature
@CRUD
Feature: Withdraw fixed amount
the "Withdraw cash" menu contains several fixed amounts to speed up transactions for users.

Scenario: withdraw fixed amount of $500
    Given I have $500 in my account
    When I choose to Withdraw the fixed amount of $50
    then i should receive $50 cash
        And the balance of my account should be $450

Scenario: withdraw fixed amount of $100
    Given I have $500 in my account
    When I choose to Withdraw the fixed amount of $100
    then i should receive $100 cash
        And the balance of my account should be $400

Scenario: withdraw fixed amount of $10
    Given I have $100 in my account
    When I choose to Withdraw the fixed amount of $10
    then i should receive $10 cash
        And the balance of my account should be $90

Scenario: withdraw fixed amount of $80
    Given I have $200 in my account
    When I choose to Withdraw the fixed amount of $80
    then i should receive $80 cash
        And the balance of my account should be $120