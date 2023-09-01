import telegram
import os


def post_image(filename, chat_id):

    token = os.environ['TELEGRAM_TOKEN']

    bot = telegram.Bot(token=token)

    bot.send_document(
        chat_id=chat_id,
        document=open(f'images/{filename}', 'rb')
    )
