import yaml
global generic_data
generic_data = yaml.load(open('configuration/config.yml'))
print(generic_data)
#generic_data['app']['host']
def before_all(context):
    print("**************Before all ***********")

    context.host=generic_data['app']['host']
    print(context.host)
    context.root_path = generic_data['app']['root_path']
    context.admin_token = generic_data['users']['admin_token']
    context.token_other_user = generic_data['users']['token_other_user']

