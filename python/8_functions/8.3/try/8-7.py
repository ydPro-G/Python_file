def make_album(singer_name,album_name):
    """歌手名，专辑名"""
    singer = ('name': singer_name,'album': album_name)
    return singer.title()

singer_a = ('周杰伦' + '牛仔很忙')
print(singer_a)