def city_country(name,country):
    """城市，国家"""
    ct_cy = name + ', ' + country
    return ct_cy.title()

message_a = city_country('Beijing',country='China')
message_b = city_country('ShangHai','China')
message_c = city_country('XiangGang','China')
print(message_a)
print(message_b)
print(message_c)




print("\n")

def cs_gj(n,c='riben'):
    print(n + ', ' + c)

cs_gj('dongjing')
cs_gj('qianye','riben')
cs_gj('buzhidao')

