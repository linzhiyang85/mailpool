from smtplib import SMTP as Client
import faker
import time

client = Client('127.0.0.1', '8025')
faker = faker.Faker()
for _ in range(3):
    name = faker.name()
    r = client.sendmail(faker.name().replace(' ', '.') + '@source.com', [name.replace(' ', '.') + '@mailpool.xyz'], f"""\
    From: Any Person <any@example.com>
    To: Yoyo <yoyo@mailpool.xyz>
    Subject: A test from {name}
    Message-ID: <ant>

    Hi there, this is {name}.
    <script>evil code</script>
    """)

    time.sleep(2)
