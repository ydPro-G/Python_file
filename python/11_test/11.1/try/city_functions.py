# 一个函数 两个形参

def country(city,country,population = ''):
    if population:
        stat = country + '-' + city + '-' + str(population)
    else:
        stat = country + '-' + city
    return stat




