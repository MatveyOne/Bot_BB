import json


class Anketa:
    def __init__(self, questions):
        self.questions = questions
        #self.scales = scales
        self.answers = {}
        self.score = 0
        self.world = ""
        self.photo = ""
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
            self.world = "Ждун"
        elif 3 <= self.score <= 4:
            self.world = "почти  Ждун"                                             #Определение какой ждун
        elif 1 <= self.score <= 2:
            self.world = "не Ждун"
        else:
            self.world = "Крутой"

        return self.world

    def get_photo(self):                                                          #фото
        if self.score == 5:
            self.photo = open("ждун.jpg", "rb")
        elif 3 <= self.score <= 4:
            self.photo = open("ждун.jpg", "rb")
        elif 1 <= self.score <= 2:
            self.photo = open("ждун.jpg", "rb")
        else:
            self.photo = open("ждун.jpg", "rb")
        return self.photo

    def get_gif(self):
        return "C:\\Users\\user\\PycharmProjects\\bot_anketalast\\beavis-and-butthead-bunghole.gif"



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
    return ("Приветствую, Вас! Это бот-анкета,чтобы понять на сколько ты ленив.\n"
            "В анкете будут предложены 5 вопросов, на которые нужно будет ответить Да или Нет\n"
            "После овтетов на все вопросы, Вы получете сообщение с результатом теста в виде сообщения и картинки.\n"
            "Можете ознакомиться с доступными командами (/help).\n"
            "Для начала анкеты нажми (/Lets_go)")


def is_yes_or_no(answer):
    return answer.lower() in ['да', 'нет']