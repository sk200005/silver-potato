from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()



url = 'https://www.thehindu.com/news/national/pradhan-discusses-cbse-payment-gateway-overhaul-with-four-public-sector-banks/article71025082.ece'
loader = WebBaseLoader(url)

prompt = PromptTemplate(
    template='Answer the question - \n {question} from the following text - \n {text}',
    input_variables= ['question', 'text']
)

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

parser = StrOutputParser()

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    'question': 'summarise this news in short',
    'text': docs[0].page_content
})

print (result)