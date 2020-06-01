def describe_city(name,country='中国'):
    """城市名字，城市所属国家"""
    print(name.title() + " is in " + country.title() + ".")

describe_city('北京')
describe_city('上海')
describe_city('东京',country='日本')