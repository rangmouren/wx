# -*- coding: utf-8 -*-

from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue
import threading

logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()


def on_message(message):
    queue_recved_message.put(message)


# 消息处理示例 仅供参考
def thread_handle_message(wx_inst):
    ids = []
    while True:
        message = queue_recved_message.get()
        id = message['data'].get('wx_id')
        wx_nickname = message['data'].get('wx_nickname')
        if id:
            ids.append({wx_nickname: id})
        if message['data'].get('unread_number'):
            break
    return ids
    # if 'msg' in message.get('type'):
    #     # 这里是判断收到的是消息 不是别的响应
    #     msg_content = message.get('data', {}).get('msg', '')
    #     send_or_recv = message.get('data', {}).get('send_or_recv', '')
    #     if send_or_recv[0] == '0':
    #         # 0是收到的消息 1是发出的 对于1不要再回复了 不然会无限循环回复
    #         wx_inst.send_text('filehelper', '收到消息:{}'.format(msg_content))


def main():
    wx_inst = WechatPCAPI(on_message=on_message, log=logging)
    wx_inst.start_wechat(block=True)

    while not wx_inst.get_myself():
        time.sleep(5)

    print('登陆成功')
    print(wx_inst.get_myself())

    friends = thread_handle_message(wx_inst)
    for i in friends:
        print(i)
    # time.sleep(10)
    # wx_inst.send_text(to_user='filehelper', msg='777888999')
    wx_inst.send_text(to_user='wxid_wjd8tpo2w2tu22', msg='777888999')

    # time.sleep(1)
    # wx_inst.send_link_card(
    #     to_user='filehelper',
    #     title='博客',
    #     desc='我的博客，红领巾技术分享网站',
    #     target_url='http://www.honglingjin.online/',
    #     img_url='http://honglingjin.online/wp-content/uploads/2019/07/0-1562117907.jpeg'
    # )
    # time.sleep(1)
    #
    # wx_inst.send_img(to_user='filehelper', img_abspath=r'C:\Users\Leon\Pictures\1.jpg')
    # time.sleep(1)
    #
    # wx_inst.send_file(to_user='filehelper', file_abspath=r'C:\Users\Leon\Desktop\1.txt')
    # time.sleep(1)
    #
    # wx_inst.send_gif(to_user='filehelper', gif_abspath=r'C:\Users\Leon\Desktop\08.gif')
    # time.sleep(1)
    #
    # wx_inst.send_card(to_user='filehelper', wx_id='gh_6ced1cafca19')

    # 这个是获取群具体成员信息的，成员结果信息也从上面的回调返回
    # wx_inst.get_member_of_chatroom('22941059407@chatroom')

    # 新增@群里的某人的功能
    # wx_inst.send_text(to_user='22941059407@chatroom', msg='test for at someone', at_someone='wxid_6ij99jtd6s4722')

    # 这个是更新所有好友、群、公众号信息的，结果信息也从上面的回调返回
    # wx_inst.update_frinds()


if __name__ == '__main__':
    main()
