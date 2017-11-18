Feature: API
Scenario:
    Given I have host_path as "https://www.pivotaltracker.com"
        And  I have rootPath as "/services/v5"
        And I have addmin user token 2a6118f239fa9083cf56206082f3eefe
        And I have other user token 99d8d265cef8087a9d5f6a24df672713
    When I get the true

