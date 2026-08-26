import dotenv
import os

import langchain
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser


dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# # модель
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",   # назва моделі
    api_key=api_key    # ключ до сервера з моделлю
)



# Напишіть модель для генерації персонального плану
# тренувань з двох ланцюгів:
#  Перший ланцюг отримує мету тренування(схуднення,
# набір м’язів, тощо) та повертає список вправ
#  Другий ланцюг отримує список вправ, рівень
# підготовки користувача(низький, середній,
# професіонал) та кількість часу на тиждень(в годинах)
# і повертає план тренувань



class Exercises(BaseModel):
    exercises: list[str] = Field(description="Список вправ для досягнення мети тренування")


parser = PydanticOutputParser(pydantic_object=Exercises)
instructions = parser.get_format_instructions()


prompt1 = PromptTemplate.from_template(
    """
    Ти професійний тренер.

    Потрібно підібрати вправи відповідно до мети тренування.

    ### ФОРМАТ ВІДПОВІДІ ###
    {instructions}

    ### ВХІДНІ ДАНІ ###
    Мета тренування: {goal}
    """,
    partial_variables={"instructions": instructions}
)

chain1 = prompt1 | llm | parser

class TrainingPlan(BaseModel):
    plan: list[str] = Field(description="План тренувань на тиждень")

parser2 = PydanticOutputParser(pydantic_object=TrainingPlan)

instructions = parser2.get_format_instructions()


prompt2 = PromptTemplate.from_template(
    """
    Ти професійний тренер.
    Створи персональний план тренувань на тиждень.
    Для кожного тренування вкажи день,
    вправи, кількість підходів, повторень
    та час відпочинку.

    ### ФОРМАТ ВІДПОВІДІ ###
    {instructions}

    ### ВХІДНІ ДАНІ ###
    {exercises}
    {level}
    {hours}
    """,
    partial_variables={"instructions": instructions}
)

chain2 = prompt2 | llm | parser2


goal = "схуднення"

level = "низький"

hours = 3


data= {
    "goal": goal
}
exercises = chain1.invoke(data)


data1 = {
    "exercises": exercises.exercises,
    "level": level,
    "hours": hours
}

plan = chain2.invoke(data1)

print(plan)