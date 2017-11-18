from compare import expect
from utils/utils.api_request import *

@given(u'I have host_path as "{host}"')
def step_impl(context, host):
    print(context.host)
    expect(context.host).to_equal(host)

@given(u'I have rootPath as "{root_path}"')
def step_impl(context, root_path):
    expect(context.root_path).to_equal(root_path)

@given(u'I have addmin user token {admin_token}')
def step_impl(context, admin_token):
    expect(context.admin_token).to_equal(admin_token)

@given(u'I have other user token {token_other_user}')
def step_impl(context, token_other_user):
    expect(context.token_other_user).to_equal(token_other_user)

@when(u'I get the true')
def step_impl(context):
    print("other test case")
