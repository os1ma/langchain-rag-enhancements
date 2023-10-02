import langchain
from dotenv import load_dotenv
from langchain.chains import HypotheticalDocumentEmbedder, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

langchain.debug = True

load_dotenv()

base_embeddings = OpenAIEmbeddings()
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
embeddings = HypotheticalDocumentEmbedder.from_llm(chat, base_embeddings, "web_search")

# FAISSに保存されたベクトルを読み込む
db = FAISS.load_local("./tmp/faiss", embeddings)
retriever = db.as_retriever()

# LangChainにおけるRAGの基本である「RetrievalQA」を準備する
qa_chain = RetrievalQA.from_chain_type(
    llm=chat, chain_type="stuff", retriever=retriever
)

# 「クエリに関連する文書を検索 => LLMに回答を生成させる」という流れを実行する
query = "LangChainとは"
result = qa_chain.run(query)
print(result)
