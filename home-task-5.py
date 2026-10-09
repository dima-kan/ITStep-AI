import dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.messages import HumanMessage, SystemMessage

dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api_key
)

serper_places = GoogleSerperAPIWrapper(
    serper_api_key=serper_key,
    type="places"
)


@tool
def find_restaurants(query: str):
    """
    Пошук ресторанів за запитом

    :param query: str -- запит, наприклад "піца Київ"
    :return: список ресторанів
    """
    result = serper_places.results(query)
    return result["places"]


agent = create_agent(
    model=llm,
    tools=[find_restaurants]
)

messages = [
    SystemMessage("""
    Ти -- ввічливий чат бот, який рекомендує ресторани.
    Для пошуку ресторанів використовуй інструмент find_restaurants.
    Для кожного ресторану вказуй назву, посилання на сайт (якщо є) та рейтинг.
    """)
]

while True:
    query = input("Ви: ")

    if query == "":
        break

    user_message = HumanMessage(query)

    messages.append(user_message)

    data = {
        "messages": messages
    }

    data = agent.invoke(data)

    messages = data["messages"]

    response = messages[-1]

    print(response.text)