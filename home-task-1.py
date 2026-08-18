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


with open("data/lesson9/return_policy.txt","r",encoding="utf-8") as f:
    rules = f.read()


history = []


while True:
    question = input("question: ")
    if question == "":
        break

    history.append(f"Human: {question}")
    history_text = "\n".join(history)

    prompt = f"""
       Ти консультант з питань повернення товару. Відповідай на запитання клієнтів на основі правил нижче.

       Правила:
       {rules}

       Історія діалогу:
       {history_text}

       Інструкція
       Відповідай тільки на ті положення, що є в правилах.
       Якщо відповіді немає в правилах, скажи, що не знаєш відповіді.
       Відповідь повинна бути короткою та чіткою.

       Ось питання користувача: {question}
       """

    response = llm.invoke(prompt)
    history.append(f"AI: {response}")
    print(f"Відповідь {response}")



