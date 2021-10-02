import bottle
from bottle import run, static_file, route, get, redirect, template
from storage import *
from mail import *
import threading
import datetime
from copy import deepcopy
bottle.TEMPLATE_PATH.append('./static/template')

@get('/static/<filepath:path>')
def get_static(filepath):
    return static_file(filepath, root='static')

@get('/')
@get('/index.htm')
@get('/index.html')
def redirect_to_main():
    redirect('/addresses')

def human_readable_date(date_obj):
    delta = datetime.datetime.now() - date_obj
    if delta.days > 0:
        return str(delta.days) + '天前'
    else:
        remain_seconds = delta.seconds
        hours = remain_seconds // 3600
        remain_seconds %= 3600
        minutes = remain_seconds // 60
        seconds = remain_seconds % 60
        return (str(hours) + '小时' if hours > 0 else '') + \
               (str(minutes) + '分钟' if minutes > 0 else '') + \
               (str(seconds) + '秒' if seconds > 0 else '') + \
                '之前'

@get('/addresses')
@get('/addresses/')
def read_latest_addresses():
    latest_addresses = get_latest_updated_emails()

    if len(latest_addresses) == 0:
        return '<p>No email is received, please try to send one to any address</p>'

    address_sorted_by_received = deepcopy(
        sorted(latest_addresses.items(), key=lambda item: item[1]['received'], reverse=True)
    )

    # html = '<table><thead><tr><th>Received Time</th><th>Email Address</th></tr></thead><tbody align=left>'
    # for item in address_sorted_by_received:
    #     html += f'<tr><th align=left>{item[1]}</th><td><a href="/addresses/{item[0]}/messages/">{item[0]}</a></td></tr>'
    # html += '</tbody></table>'
    # return html

    for key, value in address_sorted_by_received:
        value['received'] = human_readable_date(value['received'])

    return template('mail_list', mailItems = address_sorted_by_received)

@get('/addresses/<email>/messages')
@get('/addresses/<email>/messages/')
def read_messages(email):
    message_list = get_email_messages(email)
    if message_list and len(message_list) > 0:
        message_list.sort(key=lambda msg:msg['received'], reverse=True)
        # html = '<ui>'
        # for message in message_list:
        #     html += f'<li><a href="/addresses/{email}/messages/{message["id"]}">{message["subject"]}</a> - {message["received"]}</li>'
        # html += '</ui>'
        return template('message_list', inboxName=email, messageItems = message_list)
    else:
        html = f'<p>No message for {email}</p>'
    return html

@get('/addresses/<email>/messages/<id>')
@get('/addresses/<email>/messages/<id>/')
def read_message(email, id):
    message = get_email(email, id)
    if message is not None:
        html = '<table><tbody style="text-align:left;vertical-align:top">'
        tags = re.compile(r'<[^<>]*?>')
        for key, value in message.items():
            html += f'<tr><th>{tags.sub("", key)}</th><td>{"<br>".join([tags.sub("", str(val)) for val in value]) if isinstance(value, list) else tags.sub("", str(value))}</pre></td></tr>'
        html += '</tbody></table>'
    else:
        html = f'<p>No message for {email} with id {id}</p>'
    return html

@get('/clear')
@get('/clear/')
def clear_old_mails():
    try:
        clear_older_than_seven_days()
        html = f'<p>Done</p>'
    except Exception as ex:
        html = f'<p>Error: {str(ex)}</p>'
    return html

if __name__ == '__main__':
    mail_server = threading.Thread(target=start_mail)
    mail_server.start()

    run(host='0.0.0.0', port=8080)
