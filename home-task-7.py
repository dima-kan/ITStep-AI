import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)


st.title("Наш чатбот")

api_key = st.secrets["GEMINI_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api_key
)





if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(
            content=
            f"""
        Ти помічник для вивчення англійської мови. Спілкуйся українською, допомагай вчити англійську. Відповідай коротко і просто.
        Якщо користувач просить перекласти слово або фразу, дай переклад українською, 1 приклад речення англійською і переклад цього речення українською.
        Якщо користувач просить перекласти речення, дай переклад українською і поясни граматику простими словами одним реченням (наприклад: there is/are, пасивний стан, часи тощо).
        Якщо питання не про англійську, ввічливо скажи, що допомагаєш тільки з вивченням англійської.
        Відповідай дружньо, без складних термінів.
        """
        )
    ]

user_query = st.chat_input("Питання")


for message in st.session_state.history:
    if isinstance(message, SystemMessage):
        continue

    role = ""
    if isinstance(message, HumanMessage):
        role = "user"
    else:
        role = "AI"

if user_query:

    human_message = HumanMessage(content=user_query)

    st.session_state.history.append(human_message)

    with st.chat_message("user"):
        st.markdown(user_query)

    response = llm.invoke(st.session_state.history)

    st.session_state.history.append(response)

    with st.chat_message("assistant"):
        st.markdown(response.text)
