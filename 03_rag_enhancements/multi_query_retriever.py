import langchain
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.vectorstores import FAISS

langchain.debug = True

load_dotenv()

# FAISSに保存されたベクトルを読み込む
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("./tmp/faiss", embeddings)
base_retriever = db.as_retriever()

# MultiQueryRetrieverを準備
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
retriever = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=chat)

qa_chain = RetrievalQA.from_chain_type(
    llm=chat, chain_type="stuff", retriever=retriever
)

query = "LangChainとは"
result = qa_chain.run(query)
print(result)
