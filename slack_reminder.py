from slacker import Slacker
from datetime import datetime
import argparse

def send_slack(subject, context, channel): 
    token = "Edit your slack token here!!!"
    slack = Slacker(token)
    slack.chat.post_message(channel, context, username=subject)
    return

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--subject", help="subject", required=False)
        parser.add_argument("-c", "--context", help="context", required=False)
        parser.add_argument("-cl", "--channel", help="slack channel", required=False)
        args = parser.parse_args()
        if args.channel:
            channel = args.channel
        else:
            channel = "reminder" # Channel name set in your slack!!!

        if args.subject:
            subject = args.subject
        else:
            subject = "Code Finished!"

        if args.context:
            context = args.context
        else:
            current_time = datetime.now()
            datenow = current_time.strftime("%H:%M:%S")
            context = datenow
        send_slack(subject, context, channel)
    except:
        print("python slack_reminder.py -c <context> -s <subject> -cl <channel>")
        pass

