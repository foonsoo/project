from imap_tools import MailBox
import os

mail_box = 'INBOX'
mail_add = os.environ['mail_add']
mail_id = os.environ['mail_id']
mail_pass = os.environ['mail_pass']
down_path = '/data/mail/' ## k8s pvc 경로 지정

def main():
    with MailBox(mail_add).login(mail_id, mail_pass, mail_box) as mailbox:
        for msg in mailbox.fetch():
            for att in msg.attachments:
                print(att.filename, att.content_type)
                with open(down_path+'{}'.format(att.filename), 'wb') as f:
                    f.write(att.payload)
                    
if __name__ == "__main__":
    main()