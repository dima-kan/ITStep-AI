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

# Завдання 1
# Напишіть модель для рекомендації книг з двох ланцюгів:
#  Перший ланцюг отримує назву книги та визначає її
# жанр



#
# class GenreBooks(BaseModel):
#     genre: str = Field(description="Жанр книги")
#
#
# parser = PydanticOutputParser(pydantic_object=GenreBooks)
#
# instructions = parser.get_format_instructions()
#
# prompt_genre = PromptTemplate.from_template(
#     """
#     Ти -- чатбот-бібліотека
#     Твоя задача дати визначити  жанр книги.
#
#
#     ###ІНСТРУКЦІЇ###
#     Відповідь має бути до 4 слів.
#
#     ###ФОРМАТ ВІДПОВІДІ###
#     {format_instructions}
#
#     ###ВХІДНІ ДАНІ###
#     {book}
#
#
#     """,partial_variables={
#         "format_instructions": instructions,
#     }
# )
#
# chain1 = prompt_genre | llm | parser
#
#
# book_name = "Harry Potter"
#
#
# data_book = {
#     "book": book_name,
# }
#
# response = chain1.invoke(data_book)
#
#
# print(response.genre)
#
#
# #  Другий отримує назву книги, жанр та повертає список
# # схожих книг(того ж самого жанру та іншого)
#
# class  Recommendations(BaseModel):
#     same_genre: list[str] = Field(description="Список книг того самого жанру")
#     other_genre: list[str] = Field(description="Список схожих книг інших жанрів")
#
#
# parser_books = PydanticOutputParser(pydantic_object= Recommendations)
#
# instructions_books = parser_books.get_format_instructions()
#
# prompt_books = PromptTemplate.from_template(
#     """
#     Ти — чатбот-бібліотека.
#
#     Твоя задача — рекомендувати книги, схожі на задану книгу.
#
#     ### ІНСТРУКЦІЇ ###
#     1. Врахуй назву книги та її жанр.
#     2. Поверни 5 книг того самого жанру.
#     3. Поверни 5 схожих книг, але іншого жанру.
#     4. Не рекомендуй саму задану книгу.
#
#     ### ФОРМАТ ВІДПОВІДІ ###
#
#     {format_instructions}
#
#     ###ВХІДНІ ДАНІ###
#     {book}
#     {genre}
#     """,partial_variables=
#     {
#         "format_instructions": instructions_books,
#     }
# )
#
#
# chain2 = prompt_books | llm | parser_books
#
#
# book_name = "Harry Potter"
#
# data ={
#     "book": book_name
# }
#
# response1 = chain1.invoke(data)
#
# print(response1.genre)
#
#
# data1 = {
#     "book": book_name,
#     "genre": response1.genre
# }
#
# response2 = chain2.invoke(data1)
#
# print(response2)




# Завдання 3
# Напишіть модель для генерації резюме:
#  Перший ланцюг отримує опис вакансії та повертає
# основні навички, які необхідні
#  Другий ланцюг отримує основні навички та опис
# кандидата і генерує резюме


class Skills(BaseModel):
    experience: float = Field(description="Досвід роботи в роках")
    english_level: str = Field(description="Рівень англійської мови")
    frameworks: list[str] = Field(description="Список бібліотек")
    technologies: list[str] = Field(description="Список технологій")
    language_programing : str = Field(description="Мова програмування")


parser = PydanticOutputParser(pydantic_object=Skills)

instrustions = parser.get_format_instructions()


prompt = PromptTemplate.from_template(
    """
    Ти - досвідчений рекрутер.
    Потрібно повернути основні навички з опису вакансії.
    
    
    ### ФОРМАТ ВІДПОВІДІ ###
    {instrustions}

    ###ВХІДНІ ДАНІ###
     Опис вакансії: {vacancy_description}
    

    """,partial_variables={"instrustions":instrustions}
)



chain = prompt | llm | parser


vacancy = """
    Are you a Data Scientist with a love of LLMs, generative AI?
 
We are looking for a passionate Data Scientist to implement AI solutions aimed at achieving business goals.
 
This role offers the opportunity to work on cutting-edge AI adoption projects that helps to improve current business processes.
 
     You'll be a great fit if you have:
 Strong Python Experience (2 year +);
Experience with LLM , Diffusion models;
Knowledge of Prompt engineering;
Experience with Gen AI-related technologies such as LangChain and RAG;
Experience with Neural Networks (Optional) ;
Experience with NLP , Predictive analytics and Machine learning;
Experience with Pandas;
Experience with SQL, including experience with large datasets;
Strong experience in statistics;
Bachelor's degree in Computer Science or a related field.
What you'll do:
Develop AI agents that utilize LLM, RAG and langchain approach;
Implement LLM and Diffusion models to boost business productivity;
Utilize LLM (LLM Vision) to improve object detection, text classification and extraction;
Create forecasting, recommendation, and classification models;
Transform business challenges to AI applications.

     We ensure your growth with:
Competitive salary fixed in USD;
Flexible working schedule and fully remote work format;
Paid vacation days and sick leave days ;
Personal and professional development opportunities;
Participation in building innovative projects from scratch using modern technologies;
Team-building activities and corporate events;
English classes and educational events.
 
"""


data = {
    "vacancy_description": vacancy,
}

response = chain.invoke(data)
print(response)