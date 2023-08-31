import telegram
import os

from dotenv import load_dotenv


def post_image(filename):
    load_dotenv()

    token = os.environ['TOKEN']
    chat_id = os.environ['CHAT_ID']

    bot = telegram.Bot(token=token)

    bot.send_document(
        chat_id=chat_id,
        document=open(f'images/{filename}', 'rb')
    )
