import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from info import *
from parol import token
from telebot.types import InputFile


TOKEN = token  # Замените на свой токен
bot = telebot.TeleBot(TOKEN)


filename = "user_data.json"
anketa_file = "anketa_progress.json"

anketa_questions = ["Откладывали ли вы подъем на 5 минут, а затем еще на 5, и так далее, чтобы 'случайно' проспать?",
                    "Приходилось ли вам использовать палку или другие предметы, чтобы достать что-то, вместо того чтобы встать и взять это?",
                    "Вы часто выбираете программы на телевизоре, которые уже идут, чтобы избежать поиска пульта?🦭",
                    "Бывало ли, что вы откладывали важные дела, чтобы посмотреть еще одну серию любимого сериала?",
                    "Предпочли бы вы заказать еду доставкой, даже если у вас есть все необходимые продукты для готовки, потому что лень готовить?"]
anketa = Anketa(anketa_questions)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton("Да"))
markup.add(KeyboardButton("Нет"))

restart_markup = ReplyKeyboardMarkup(resize_keyboard=True)
restart_markup.add(KeyboardButton("/restart"))

def is_yes_or_no(answer):
    return answer.lower() in ['да', 'нет']

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, get_help())

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, get_start())


@bot.message_handler(commands=['Lets_go'])
def handle_Lets_go(message):
    bot.send_message(message.chat.id, anketa.get_question(message.from_user.id), reply_markup=markup)


@bot.message_handler(commands=['restart'])
def handle_restart(message):
    anketa.load_progress(anketa_file)
    bot.send_message(message.chat.id, "Анкета сброшена. Начнем заново.")
    handle_start(message)



@bot.message_handler()
def handle_answer(message):
    current_question = anketa.get_question(message.from_user.id)
    if current_question is not None:
        if is_yes_or_no(message.text):
            anketa.process_answer(message.from_user.id, message.text)
            next_question = anketa.get_question(message.from_user.id)
            if next_question:
                bot.send_message(message.chat.id, next_question, reply_markup=markup)
            else:
                world = anketa.get_score()
                bot.send_message(message.chat.id, f"Результат: {world}. \nИспользуйте /restart, чтобы начать заново", reply_markup=restart_markup)
                anketa.save_progress(anketa_file)
                gif_path = anketa.get_gif()
                gif_description = anketa.get_gif_description()
                if gif_path:
                    with open(gif_path, "rb") as gif_file:
                        bot.send_document(message.chat.id, InputFile(gif_file, 'file.gif'), caption = f"<b>{gif_description}</b>", parse_mode="HTML")
                else:
                    bot.send_message(message.chat.id, "Не удалось найти GIF-изображение.")
                anketa.reset()  # Добавим сброс после отправки результата
        else:
            bot.send_message(message.chat.id, "Ваш ответ не распознан. Напишите 'Да' или 'Нет'. Используйте /restart, чтобы начать заново", reply_markup=restart_markup)





if __name__ == '__main__':
    bot.polling()