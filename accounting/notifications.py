import subprocess
import json
import time
import requests


notifications = json.loads(subprocess.check_output(['termux-notification-list']).decode('utf-8'))

for notif in notifications:
    if notif.get('title') == '983 000 9419':
        text = notif['content']
        lines = text.split('\n')
        if len(lines)> 1:
            second_line = lines[1]
            second_line = second_line.split(":")[1]
            second_line = second_line.replace(',', "")

            if second_line.endswith('+'):
                second_line=second_line.replace('+', '')
                is_cost = False
                title = 'دریافتی'

            else:
                second_line=second_line.replace('-', '')
                is_cost = True
                title = 'هزینه'
        req = requests.post('127.0.0.1:8000/transaction/auto/', {'title':title,
            'price':second_line,
            'extra_data':text
            })


    
    