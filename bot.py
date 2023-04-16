import telebot
import processing

TOKEN = "-"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}. "
                                      f"Вы можете использовать /help для вывода списка вопросов.")

@bot.message_handler(commands=["help"])
def send_qlist(message):
    bot.send_message(message.chat.id, "Список вопросов:\n"
                    "1. Зачем нужен студенческий билет?\n"
                    "2. Какая неделя четная, а какая нечетная?\n"
                    "3. Что такое коллоквиум?\n"
                    "4. Можно ли не ходить на физкультуру?\n"
                    "5. Какие есть направления физической подготовки?\n\n"
                    "Укажите номер интересующего вас вопроса.")

@bot.message_handler(content_types=["text"])
def send_answer(message):
    bot.send_message(message.chat.id, processing.question_processing(message.text))

if __name__ == "__main__":
    bot.infinity_polling()
