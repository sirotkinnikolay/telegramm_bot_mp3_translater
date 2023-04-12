import logging
from loader import bot
from src import start_bot


while True:
    try:
        if __name__ == '__main__':
            bot.polling(none_stop=True, interval=0)
    except Exception as problem:
        logging.error(problem)
