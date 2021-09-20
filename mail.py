import asyncio
from uuid import uuid4
import datetime
from aiosmtpd.controller import Controller
from storage import add_message

class SmtpHandler:
    # async def handle_AUTH(server, session, envelope, args):
    #     pass



    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        if not address.endswith('@mailpool.xyz'):
            return '550 not relaying to that domain, only domain @mailpool.xyz is accepted'
        envelope.rcpt_tos.append(address)

        return '250 OK'

    def process_envelope(self, envelope):
        enve_dict = {
            'id': str(uuid4()),
            'from': envelope.mail_from,
            'to': envelope.rcpt_tos,
            'received': datetime.datetime.now(),
            'subject': '',
            'body': ''
        }
        content = envelope.content.decode('utf8', errors='replace').splitlines()
        enve_dict['body'] = content
        for line in content:
            try:
                segments =line.split(sep=':', maxsplit=1)
                if len(segments) == 2:
                    if segments[0].strip().lower() == 'subject':
                        enve_dict['subject'] = segments[1].lstrip()
            except Exception as ex:
                print(str(ex))

        return enve_dict

    async def handle_DATA(self, server, session, envelope):
        print('Message from %s' % envelope.mail_from)
        print('Message for %s' % envelope.rcpt_tos)
        print('Message data:\n')
        for ln in envelope.content.decode('utf8', errors='replace').splitlines():
            print(f'> {ln}'.strip())
        print()
        print('End of message')
        message_object = self.process_envelope(envelope)
        for address in message_object['to']:
            add_message(address, message_object)

        return '250 Message accepted for delivery'

    # async def handle_EHLO(self, server, session, envelope, hostname, responses):
    #     pass

    # async def handle_HELO(self, server, session, envelope, hostname):
    #     pass

    # async def handle_MAIL(self, server, session, envelope, address, mail_options):
    #     pass

    
def start_mail():

    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    loop = asyncio.get_event_loop()

    handler = SmtpHandler()
    controller = Controller(handler, hostname='0.0.0.0', port='8025', ready_timeout=30)
    controller.start()

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()
        loop.stop()

if __name__ == '__main__':
    start_mail()
