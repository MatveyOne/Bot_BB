import json


class Anketa:
    def __init__(self, questions):
        self.questions = questions
        self.answers = {}
        self.score = 0
        self.world = ""
        self.gif = ""

    def reset(self):
        self.answers = {}
        self.score = 0
        self.world = ""
        self.gif = ""
    def get_question(self, user_id):
        if user_id not in self.answers:
            self.answers[user_id] = []

        answered_questions = len(self.answers[user_id])
        if answered_questions < len(self.questions):
            return self.questions[answered_questions]
        else:
            return None

    def process_answer(self, user_id, answer):
        if user_id not in self.answers:
            self.answers[user_id] = []
        self.answers[user_id].append(answer)
        if answer == "Да":
            self.score += 1
        elif answer == "Нет":                                             #Определение баллов
            self.score += 0
        else:
            self.score = None

    def get_score(self):

        if self.score == 5:
            self.world = "'Король Лени': Ты достиг высшего уровня лени и заслуживаешь титул 'Короля Лени'. Бивис и Баттхед гордятся тобой!"
            self.gif = "gif1"
        elif 3 <= self.score <= 4:
            self.world = "'Ленивый Мастер': Ты не просто ленив, ты мастер этого искусства. Перед тобой даже Бивис и Баттхед выглядят активными!"
            self.gif = "gif2"                                                             #Определение какой ты ленивый и вывод gif
        elif 1 <= self.score <= 2:
            self.world = "'Беззаботный Бивис': Ты вписываешься в стиль Бивиса - беззаботного и ленивого. Ты знаешь толк в правильном отдыхе!"
            self.gif = "gif3"
        elif  self.score == 0:
            self.world = "'Крутой Бивис': Ты не так уж ленив, по крайней мере, как Бивис. Поздравляю, ты крут!"
            self.gif = "gif4"
        return self.world

    def get_gif(self):
        gif_paths = {
            "gif1": "./beavis-and-butthead-bunghole.gif",
            "gif2": "./work-sucks-butt-head.gif",
            "gif3": "./water-slide-beavis.gif",                # TODO Поставить запятую и еще gif
            "gif4": "./cool-butt-head.gif",
        }
        gif_path = gif_paths.get(self.gif, None)
        return gif_path

    def get_gif_description(self):
        gif_descriptions = {
            "gif1": "Мозг – это такая штука, которая бывает у людей. А у меня есть кукуруза.",
            "gif2": "Огонь! Огонь! Огонь!.. Эмм, а чё мы смеемся?",
            "gif3": "Ня, ня, ня! Умный человек сказал бы что-то умное, но это не я.",
            "gif4": "Лучший способ решить проблему – представить, что её нет.",
        }
        gif_description = gif_descriptions.get(self.gif, None)
        return gif_description
    def save_progress(self, file):
        with open(file, "w") as f:
            json.dump(self.answers, f)

    def load_progress(self, file):
        try:
            with open(file) as f:
                self.answers = json.load(f)
        except FileNotFoundError:
            pass  # файл не существует, просто игнорируем


def get_help():                                                              #Команда помощь
    return ("Команда (/Lets_go) начинает  анкету.\n"
            "Команда (/restart) перезапускает и обнуляет анкету.\n")




def get_start():                                                                                                                         #Команда старт
    return ("Приветствую, Вас! Это бот-анкета,чтобы понять на сколько ты ленив в стиле Бивиса и Баттхета.🤟\n"
            "В анкете будут предложены 5 вопросов, на которые нужно будет ответить Да или Нет\n"
            "После овтетов на все вопросы, Вы получете сообщение с результатом теста в виде сообщения и картинки.\n"
            "Можете ознакомиться с доступными командами (/help).\n"
            "Для начала анкеты нажми (/Lets_go)")


def is_yes_or_no(answer):
    return answer.lower() in ['да', 'нет']