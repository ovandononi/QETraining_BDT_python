Feature: user management
Background: Go to my profile
    Given I login application
    When I click on user icon
    Then I see my profile

Scenario: Change user picture
    Given I select change picture
    When I select a new image from my pc
    Then I see new picture loaded

Scenario: Change password
    Given I select change password
    When I select  new password
        And I fill out the old password
        And I fill out the new password
    Then I see confirmation message that password was updated