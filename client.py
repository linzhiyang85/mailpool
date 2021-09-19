from smtplib import SMTP as Client

client = Client('127.0.0.1', '8025')
names = ['apple', 'banana']

for name in names:
    r = client.sendmail('a@example.com', [name+ '@mailpool.xyz'], f"""\
    From: Any Person <any@example.com>
    To: Yoyo <yoyo@mailpool.xyz>
    Subject: A test from {name}
    Message-ID: <ant>
    
    Hi there, this is nobody.
    <script>eval code</script>
    """)