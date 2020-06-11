import eight
eight.one(15,'老虎','狮子') # 模块.函数

from eight import one
one(20,'大象')

from eight import one as o 
o(25,'恐龙')

import eight as e 
e.one(30,'霸王龙')

from eight import *
one(35,'蓝鲸')