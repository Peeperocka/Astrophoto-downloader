import telegram
import os

from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()

    token = os.environ['TOKEN']
    chat_id = os.environ['CHAT_ID']

    bot = telegram.Bot(token=token)

    bot.send_document(chat_id=chat_id, document=open('images/nasa_apod_0.jpg', 'rb'))
