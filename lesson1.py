# Підключіть модель LLM за допомогою свого API key.
# Попросіть модель згенерувати:
# ● відповідь на питання у вигляді одного
# слова(наприклад яка столиця Франції?)
# ● код python
# ● коротку історію
# Підберіть параметри креативності та довжини


import dotenv
import os
from langchain_google_genai import GoogleGenerativeAI


dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


llm = GoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    api_key=api_key,
    temperature=0.1,
)

# response = llm.invoke("яка столиця Франції? (1 слово)")
# response = llm.invoke("напиши код на пайтоні: функцію суми елементів списку(без пояснень тільки код) ")
# response = llm.invoke("напиши історію про програміста(до 4 речень )")
# print(response)


# Завдання 2
# Прочитайте файл data\lesson9\rules.txt з правилами
# користування атракціону. Напишіть програму яка отримує
# від користувачі питання та дає відповідь на нього виходячи
# з текстового файлу.
# Для цього об’єднайте правила користування з питанням
# користувача.
# Користувач задає питання поки не введе порожній рядок.
# Змініть файл rules.txt, щоб переконатись що модель
# дійсно його читає


# with open("data/lesson9/rules.txt","r",encoding="utf-8") as f:
#     rules = f.read()
#
# while True:
#     question = input("question: ")
#     response = llm.invoke(f"""
#     Ти консультант атракціону відповідай на запитання клієнтів на основі правил{rules}
#     Відповідай тільки на ті положення що є в правилах, якщо нема у правилах відповідей що ти не знаєш відповіді
#     Відповідь повинна бути короткою
#     Ось питання користувача {question}""")
#     print(f"Відповідь {response}")


# Завдання 3
# Створіть найпростіший чат бот. Напишіть моделі якого
# персонажа вона повинна вдавати(відомий актор, персонаж
# кіно\книги, тощо).
# Реалізуйте двома способами:
# 1. Модель отримує інструкцію в якому стилі відповідати
# та нове повідомлення.
# 2. Модель отримує інструкцію та історію попередніх
# повідомлень як від користувача, так і її власні відповіді у
# форматі
# Instruction: ….
# Human: massage1
# AI: message2
# Human: massage3
# AI: message4
# Human: massage5
# AI:

with open("data/lesson9/rules.txt","r",encoding="utf-8") as f:
    rules = f.read()

questions = []
responses = []
while True:
    question = input("question: ")

    questions.append(question)
    history = ""

    for old_question , old_response in zip(questions, responses):
        history += f"\nUser: {old_question}"
        history += f"\nModel: {old_response}"

