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


# Вибір відомої людини
person = st.text_input("З ким хочеш спілкуватися?")


# Створюємо історію після вибору людини
if person:

    if "history" not in st.session_state:
        st.session_state.history = [
            SystemMessage(
                content=f"""
                Ти -- {person}.
                Твоя задача давати відповіді на питання у стилі {person}.
                Не стверджуй, що ти справжня людина.
                """
            )
        ]

    user_query = st.chat_input("Питання")

    # Виводимо попередню історію
    for message in st.session_state.history:
        # не показувати SystemMessage
        if isinstance(message, SystemMessage):
            continue

        # отримуємо тип повідомлення
        role = ""
        if isinstance(message, HumanMessage):
            role = "user"
        else:
            role = "AI"

    if user_query:

        # Повідомлення користувача
        human_message = HumanMessage(content=user_query)

        st.session_state.history.append(human_message)

        with st.chat_message("user"):
            st.markdown(user_query)

        # Отримуємо відповідь
        response = llm.invoke(st.session_state.history)

        # Додаємо відповідь до історії
        st.session_state.history.append(response)

        # Виводимо відповідь
        with st.chat_message("assistant"):
            st.markdown(response.text)

else:
    st.info("Спочатку введи ім'я відомої людини.")