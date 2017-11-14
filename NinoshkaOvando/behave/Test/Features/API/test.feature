Feature: This a sample feature
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500,
cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.
No sólo sobrevivió 500 años

Scenario: This is the first scenario
Given I have $100 in my account
AND I have $200 in my account
And I have USD currency
When I request a filter account
Then It is not possible to request a filter account with USD currency
Scenario: This is the second scenario
Given A new Lite personal account that has set common public email address (e.g.: gmail, hotmail. outlook)
and non VAT country at registration
When this end user want to upgrade to Paygo
and go to billing/Add credit card form
and Personal Account is selected
and non VAT country is selected(e.g.: Canada)
and USD currency is selected
and fill out all required fields
and send the upgrade to paygo process
Then Upgrade to PayGo Process is sent successfully with USD currency


Scenario: Validate zipcode a(numbers) , county(letter or undercore) and nro habitants(number with thousend)
Given I have the following input data: 456852 zipcode, new_zeland county, 100.000.152 nro habitants
When days process is calculated
Then the correct successfully message include days and data entered


Scenario: test
Give I have "2" and "2"
When I select "sum"
Then my result should be "4"
