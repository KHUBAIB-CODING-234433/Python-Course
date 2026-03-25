from twilio.rest import Client
from datetime import datetime,timedelta
import time

client = Client(account_id,oath_tokan)

def send_msg(recipient_number,message_body):
    try:
        message = client.messages.create(
        from_ = 'whatsapp:+14155238886',
        body = message_body,
        to=f'whatsapp:{recipient_number}'
        )
        print(f'message send successfully! Message sid {message.sid}')
    except Exception as e:
        print(f"an error accured {e}")
name = input("Enter the name of the recipient")
recipient_number=input("Enter the recipient number with the country code")
message_body = input(f"Enter the message you want to send {name}: ")

date_str = input("Enter the time to send the message (yyyy--mm--dd)")
time_str = input("Enter the time on send the message (hh:mm in 24hours format)")

shedule_datetime = datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
currentdatetime = datetime.now()
time_difference = shedule_datetime - currentdatetime
delay_time = time_difference
delay_second =time_difference.total_seconds()
if delay_second<=0:
    print("The specifice time is past please enter the future  time")
else:
    print(f"Message shedule to be send to {name} at {shedule_datetime}")
    time.sleep(delay_second)

    send_msg(recipient_number,message_body)


