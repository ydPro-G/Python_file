
import time
import websocket
import threading
import random
 
 
def wsCliet(msg):
    """
    websocket发送数据
    :param msg:
    :return:
    """
    ws = websocket.create_connection("ws://http://60.213.12.154/:8282")
    try:
        while True:
            ws.send(bytes(msg, encoding='utf-8'))
            result = ws.recv()
            if result:
            #    print("响应数据：", result)
                time.sleep(random.randint(5,20))
            else:
                print("失败！没获取到响应数据！")
                ws.close()
                break
#        ws.close()
    except Exception as e:
        print("连接失败：%s" % e)
 
 
def run_thread(num):
    """
    多线程创建websocket连接
    :param num:
    :return:
    """
    for i in range(int(num)):
        if(i%200)==1:
            sleep_s = 0.001*i
            if sleep_s > 5 :
                sleep_s = 5
            time.sleep(sleep_s)
        t = threading.Thread(target=wsCliet, args=('测试数据', ))
        t.start()
 
    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为：%d' % length)
        time.sleep(2)
#        if length <= num:
#            break
 
run_thread(1)
