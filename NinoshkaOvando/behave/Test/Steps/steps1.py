
@given(u'I have the following input data: {x:d} zipcode, {y:w} county, {z:n} nro habitants')
def step_impl(context, x, y, z):
    a =x



@when(u'days process is calculated')
def step_impl(context):
    raise NotImplementedError(u'STEP: When days process is calculated')

@then(u'the correct successfully message include days and data entered')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the correct successfully message include days and data entered')
### other given


@given(u'I have ${amount:d} in my account')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: Given I have ${amount:d} in my account')

#@given(u'I have $200 in my account')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Given I have $200 in my account')

@given(u'I have USD currency')
def step_impl(context):

    raise NotImplementedError(u'STEP: Given I have USD currency')

@when(u'I request a filter account')
def step_impl(context):

    raise NotImplementedError(u'STEP: When I request a filter account')

@then(u'It is not possible to request a filter account with USD currency')
def step_impl(context):

    raise NotImplementedError(u'STEP: Then It is not possible to request a filter account with USD currency')

@given(u'A new Lite personal account that has set common public email address (e.g.: gmail, hotmail. outlook)')
def step_impl(context):

    raise NotImplementedError(u'STEP: Given A new Lite personal account that has set common public email address (e.g.: gmail, hotmail. outlook)')

@given(u'non VAT country at registration')
def step_impl(context):

    raise NotImplementedError(u'STEP: Given non VAT country at registration')

@when(u'this end user want to upgrade to Paygo')
def step_impl(context):

    raise NotImplementedError(u'STEP: When this end user want to upgrade to Paygo')

@when(u'go to billing/Add credit card form')
def step_impl(context):

    raise NotImplementedError(u'STEP: When go to billing/Add credit card form')

@when(u'Personal Account is selected')
def step_impl(context):

    raise NotImplementedError(u'STEP: When Personal Account is selected')

@when(u'non VAT country is selected(e.g.: Canada)')
def step_impl(context):

    raise NotImplementedError(u'STEP: When non VAT country is selected(e.g.: Canada)')

@when(u'USD currency is selected')
def step_impl(context):

    raise NotImplementedError(u'STEP: When USD currency is selected')

@when(u'fill out all required fields')
def step_impl(context):

    raise NotImplementedError(u'STEP: When fill out all required fields')

@when(u'send the upgrade to paygo process')
def step_impl(context):

    raise NotImplementedError(u'STEP: When send the upgrade to paygo process')

@then(u'Upgrade to PayGo Process is sent successfully with USD currency')
def step_impl(context):

    raise NotImplementedError(u'STEP: Then Upgrade to PayGo Process is sent successfully with USD currency')

