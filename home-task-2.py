import dotenv
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


llm = GoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    api_key=api_key,
    temperature=0.1,
)



prompt = PromptTemplate.from_template(
    """
     Ти — досвідчений методист і розробник навчальних курсів. 
     Створи  план навчального курсу на задану тему з особливостями цільової аудиторії.
    
    
    ###ПРАВИЛА###
    1.Створи логічний та структурований план навчального курсу.
    2.Загальна тривалість курсу (в годинах/тижнях) та рекомендована частота занять.
    3.Використовуй чітку та зрозумілу структуру.
    4.Виведи результат українською мовою.
    
    
    ###ПРИКЛАДИ###
    Тема: Python
    Цільова аудиторія: Початківці.
    Результат: Курс складається з основ Python, змінних, умов, циклів та функцій. Практика: створення простої консольної програми.
    
    
    ###ВХІДНИЙ ПАРАМЕТР###
    Тема курсу:{topic}
    Цільова аудиторія :{inventory}
    """
)

input_text = "Англійська мова"
inventory = "Діти 10-12 років."

data = {
    "topic": input_text,
    "inventory": inventory,
}

text = prompt.invoke(data)

response = llm.invoke(text)
print(response)
