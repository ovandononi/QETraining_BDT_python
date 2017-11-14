Feature: Withdraw fixed amount
the "Withdraw cash" menu contains several fixed amounts to speed up transactions for users.

Scenario: withdraw fixed amount of $500
    Given I have $500 in my account
    When I choose to Withdraw the fixed amount of $50
    then i should receive $50 cash
        And the balance of my account should be $450
