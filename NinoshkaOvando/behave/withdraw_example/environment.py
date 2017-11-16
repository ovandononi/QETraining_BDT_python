import yaml
global generic_data
generic_data = yaml.load(open('configuration/config1.yml'))


#generic_data['app']['host']
def before_all(context):
    print("**************Before all ***********")
    context.host=generic_data['app']['host']
    print("Host: ", context.host)
    context.method = generic_data['app']['method']
    context.code = generic_data['app']['code']

def after_all(context):
    print("**************after all ***********")

def before_feature(context, feature):
	if 'CRUD' in feature.tags:
		print("-----------------feature of CRUD------------------------")

def before_scenario(context, scenario):
    if 'scenario_send' in scenario.tags:
        print("----------------------scenario of scenario_send-------")
    else:
        print("----------------------not scenario of scenario_send-------")

def after_scenario(context, scenario):
    if 'withdraw fixed amount' in scenario.name:
        print("----------------------scenario name is  withdraw fixed amount-------")





