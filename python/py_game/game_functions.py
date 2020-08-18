#   包含一系列函数，函数chech_events检测相关事件，如按键和松开
#   使用辅助函数check_keydown_events()和check_keyup_events来处理这些事件
#   函数update_screen()，每次执行主循环都重绘屏幕
import sys
import pygame
from bullet import Bullet  # 导入子弹类
from alien import Alien  # 导入外星人类
from time import sleep

# 重构函数，一个响应KEYDOWN事件，一个响应KEYUP事件
# 编组传递给了check_keydown_events
def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """按下键盘触发KEYDOWN事件,true,开始移动"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 子弹设置
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)  # 只包含玩家按空格键时用于发射子弹的代码
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:  # 按空格时检测bullets长度，如果小于3，创建新子弹
        new_bullet = Bullet(ai_settings, screen, ship)  # 玩家按空格时创建一个新的子弹实例
        bullets.add(new_bullet)  # 使用add()将实例添加到编组中


def check_keyup_events(event, ship):
    """松开键盘触发KEYUP事件,flase，结束移动"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

 # 包含形参ship，用来接收实参


def check_events(ai_settings, screen, ship, bullets):  # 添加形参bullets
    """响应按键与鼠标事件"""
    for event in pygame.event.get():  # 通过pygame.event.get()方法获取事件，促使for循环运行
        if event.type == pygame.QUIT:
            sys.exit()

        # 判断:如果是KEYDOWN就调用keydown函数
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        # 判断:如果是KEYUP调用keyup函数
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)




# 将 删除已经消失的子弹
def update_bullets(bullets,aliens,ai_settings,ship,screen):
    """更新子弹位置，删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():  # 不要从列表或编组中删除条目！！遍历编组的副本，使用copy来设置for循环，这样能使我们在循环中修改bullets
        if bullet.rect.bottom <= 0:  # 检查这个编组中每颗子弹，看看是否已在屏幕顶端消失
            bullets.remove(bullet)  # 消失就在编组中删掉这个子弹
    
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
      #   遍历所有子弹，遍历所有外星人，当子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个键值对
      #   两个True告诉pygame删除发生碰撞的子弹和外星人
      # 要模拟高能子弹，将第一个布尔实参设置为False，第二个为True，子弹与外星人碰撞就不会消失，外星人会消失
    
    # 生成新的外星人
    if len(aliens) == 0:
        # 删除现有子弹新建外星人
        bullets.empty() # 删除子弹
        create_fleet(ai_settings,screen,ship,aliens) # 调用create_fleet新建外星人群



def update_screen(ai_settings, screen, ship, aliens, bullets):  # 添加形参bullets
    """更新屏幕上的图像，并切换到新屏幕"""

    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():  # 方法bullets.sprites返回一个列表，其中包含了bullets中的所有元素
        bullet.draw_bullet()
    ship.blitme()  # 将飞船绘制到屏幕上
    aliens.draw(screen)  # 在屏幕上绘制编组中的每个外星人

    # # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见，移动游戏元素时，flip将不断更新屏幕，在原来位置隐藏元素
    pygame.display.flip()


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 计算外星人之间的宽度
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 计算外星人可容纳数量
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 *
                                                      alien_height) - ship_height)  # 剩余y空间为整体高度-3行外星人高度-飞船高度
    number_rows = int(available_space_y / (2 * alien_height)
                      )  # 可容纳行数就是用剩余的高度 / 2行外星人的高度
    return number_rows  # 返回可容纳行数


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)  # 外星人
    alien_width = alien.rect.width  # 使用刚创建的外星人获取外星人宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人并计算每行可容纳多少外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


# 边缘
def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites(): # 遍历外星人群组
        if alien.check_edges(): # check_edges返回True，位于屏幕边缘
            change_fleet_direction(ai_settings, aliens) # 调用direction改变方向
            break # 退出

# 方向


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites(): # 遍历所有外星人
        alien.rect.y += ai_settings.fleet_drop_speed # 每个外星人人下移的速递为10，在settings中设置了
    ai_settings.fleet_direction *= -1 # 修改为当前值与-1的乘积

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """响应被外星人撞到的飞船，飞船数量-1，清空子弹和外星人，新建外星人，新建飞船，暂停"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕地段中央
        create_fleet(ai_settings,screen,ship,aliens) # 创建外星人群
        ship.center_ship() # 屏幕低端中央

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False # 没有飞船就game over了

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """检查是否有外星人到达了屏幕底端"""
    scren_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= scren_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break


def update_aliens(ai_settings,aliens,ship,stats,screen,bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens) # 调用check_fleet_edges来确定是有外星人位于屏幕边缘
    aliens.update()  # 对外星人编组aliens调用方法update，将自动对每个外星人调用方法update()

    # 检测外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens): # 方法spritecollideany()接受两个实参，一个精灵一个编组，如果两者有碰撞，就停止遍历编组
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets) # 碰撞发生的变化

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
    