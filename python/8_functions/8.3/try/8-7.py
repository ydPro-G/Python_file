def make_ablum(singer_name,ablum_name,singer_number=''):
    message = {'singer name: ': singer_name,'album name: ': ablum_name}
    if singer_number:  # 该形参不为空时才执行，如果为空就不执行
        message['singernum'] = singer_number  # 即使在这里，键也要用单引号引起来
    # 返回歌手名加专辑名
    return message

a = make_ablum('Lisa','WORLD')
b = make_ablum('周杰伦','牛仔很忙','11')
c = make_ablum('周华健','刀剑如梦')

print(a,b,c,sep='\n')