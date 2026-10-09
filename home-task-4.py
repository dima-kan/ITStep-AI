import dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api_key
)

summary_llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api_key,
    temperature=0
)

system_message = SystemMessage("""
    Ти -- ввічливий чатбот.
    Твоя задача підтримувати спілкування з користувачем.

    ###ІНСТРУКЦІЇ###
    1. Відповіді мають бути короткими (до 2 речень)
    2. Враховуй підсумок попередньої розмови, якщо він є
    """)

history = []

while True:
    user_text = input("Ви: ")

    if user_text == "":
        break

    history.append(HumanMessage(content=user_text))

    response = llm.invoke([system_message] + history)

    print(f"AI: {response.text}")

    history.append(response)

    if len(history) > 4:
        summary_request = HumanMessage("""
        Підсумуй усю розмову вище в декілька речень.
        Збережи якомога більше деталей: імена, числа, факти про користувача,
        його вподобання та теми, які обговорювались.
        Якщо в розмові є підсумок попередньої розмови, включи його зміст.
        Напиши лише сам підсумок, без вступів.
        """)

        summary = summary_llm.invoke(history + [summary_request]).text

        print(f"[Підсумок]: {summary}")

        history = [
            HumanMessage(content=f"Підсумок попередньої розмови: {summary}"),
        ]