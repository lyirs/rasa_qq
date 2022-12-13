from receive import rev_msg
from send_msg import send_msg
import socket
import random
import urllib.request
import json
import requests

# http://127.0.0.1:5700/send_private_msg?user_id=user&message=hello
# conda activate py38_rasa

url = "http://localhost:5005/webhooks/myio/webhook"
while True:
    try:
        rev = rev_msg()
        print(rev)
        if rev == None:
            continue
    except:
        continue

    if rev["post_type"] == "message":
        if rev["message_type"] == "private":  # 私聊
            data = {
                "sender": str(rev['sender']['user_id']),
                "message": rev['raw_message']
            }
            data_json = json.dumps(data)
            r =requests.post(url,data_json)
            msg = r.json()[0]['text']

            qq = rev['sender']['user_id']  # 获取消息发出者的qq号
            send_msg({'msg_type': 'private','number': qq, 'msg': msg})  # 发送

            # if '在吗' in rev['raw_message']:
            #     qq = rev['sender']['user_id']  # 获取消息发出者的qq号
            #     send_msg({'msg_type': 'private',
            #              'number': qq, 'msg': '我在'})  # 发送

        elif rev["message_type"] == "group":  # 群聊
            group = rev['group_id']
            if "[CQ:at,qq=112244080]" in rev["raw_message"]:
                if rev["raw_message"].split(" ")[1] == "在吗":
                    qq = rev["sender"]["user_id"]
                    send_msg({"msg_type": "group", "number": group,
                             "msg": "[CQ:poke,qq={}]".format(qq)})
            # if '在吗' in rev['raw_message']:
            #     qq = rev['sender']['user_id']
            #     send_msg({'msg_type': 'group', 'number': group, 'msg': '我在呢'})

        else:
            continue
    else:  # rev["post_type"]=="meta_event":
        continue
