from bottle import run, route, redirect, template
from storage import *
from mail import *
import threading


@route('/')
@route('/index.htm')
@route('/index.html')
def redirect_to_main():
    redirect('/addresses')


@route('/addresses')
@route('/addresses/')
def read_latest_addresses():
    latest_addresses = get_latest_updated_emails()

    if len(latest_addresses) == 0:
        return '<p>No email is received, please try to send one to any address</p>'

    address_sorted_by_received = sorted(latest_addresses.items(), key=lambda item: item[1], reverse=True)
    html = '<table><thead><tr><th>Received Time</th><th>Email Address</th></tr></thead><tbody align=left>'
    for item in address_sorted_by_received:
        html += f'<tr><th align=left>{item[1]}</th><td><a href="/addresses/{item[0]}/messages/">{item[0]}</a></td></tr>'
    html += '</tbody></table>'
    return html

@route('/addresses/<email>/messages')
@route('/addresses/<email>/messages/')
def read_messages(email):
    message_list = get_email_subjects(email)
    if message_list and len(message_list) > 0:
        message_list.sort(key=lambda msg:msg['received'], reverse=True)
        html = '<ui>'
        for message in message_list:
            html += f'<li><a href="/addresses/{email}/messages/{message["id"]}">{message["subject"]}</a> - {message["received"]}</li>'
        html += '</ui>'
    else:
        html = f'<p>No message for {email}</p>'
    return html

@route('/addresses/<email>/messages/<id>')
@route('/addresses/<email>/messages/<id>/')
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


if __name__ == '__main__':
    mail_server = threading.Thread(target=start_mail)
    mail_server.start()

    run(host='127.0.0.1', port=8080)