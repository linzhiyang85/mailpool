import re
big_dict = {}
latest_addresses = {}

def is_valid_address(address):
    if address and isinstance(address, str) and re.match('^[^@]+@[^@]+.[^@]+$', address):
        return True
    else:
        return False

def get_email_subjects(address):
    global big_dict
    if is_valid_address(address) and address in big_dict:
        messages = big_dict.get(address)
        messages.sort(key=lambda mail:mail['received'])
        return [{'id':message['id'], 'received': message['received'], 'subject':message['subject']}\
                    for message in messages]
    else:
        return []

def get_email(address, id):
    global big_dict
    if is_valid_address(address) and address in big_dict:
        messages = list(filter(lambda message:message['id']==id, big_dict.get(address)))
        if len(messages) > 0:
            return messages[0]
        else:
            return None
    else:
        return None

def add_message(address, message):
    global big_dict, latest_addresses

    if is_valid_address(address):
        if address not in big_dict:
            big_dict[address] = []
        message_list = big_dict[address]
        message_list.insert(0, message)
        big_dict[address] = big_dict[address][:50] # each mail address can contain maximum the latest 50 messages
        if address in latest_addresses:
            latest_addresses[address] = message['received']
        else:
            if len(latest_addresses) >= 30:
                earliest_received = None
                earliest_address = None
                for address, received in latest_addresses.items():
                    if earliest_received is None:
                        earliest_received = received
                        earliest_address = address
                    else:
                        if earliest_received > received:
                            earliest_received = received
                            earliest_address = address
                latest_addresses.pop(earliest_address)
            latest_addresses[address] = message['received']

def get_latest_updated_emails():
    global latest_addresses
    return latest_addresses
