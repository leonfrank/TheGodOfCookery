# 导入必要的库
import os
from langchain_community.llms.tongyi import Tongyi
from interface import load_vector_db, load_retriever, load_chain


def pretty_print_docs(docs):
    print(f"\n{'-' * 100}\n".join([f"Document {i + 1}:  " + d.page_content for i, d in enumerate(docs)]))


def test_retriever():
    # 加载检索器
    retriever = load_retriever()

    while True:
        question = input("请输入问题：")
        if question == "exit":
            break
        # docs = vectordb.similarity_search_with_score(question)
        # print(docs)
        docs = retriever.get_relevant_documents(question)
        pretty_print_docs(docs)


def test_vector_db():
    # 加载检索器
    vectordb = load_vector_db()
    while True:
        question = input("请输入问题：")
        if question == "exit":
            break
        docs = vectordb.similarity_search_with_score(question)
        print(docs)


def run_terminal(llm, verbose=True):
    qa_chain = load_chain(llm, verbose=verbose)
    while True:
        question = input("请输入问题：")
        if question == "exit":
            break
        predict = qa_chain({"question": question})
        print(predict["answer"])


if __name__ == '__main__':
    TONGYI_API_KEY = open(os.environ.get('HOME') + "/BCE_model/TONGYI_API_KEY.txt", "r").read().strip()
    verbose = True

    # 加载通义千问大语言模型
    llm = Tongyi(dashscope_api_key=TONGYI_API_KEY, temperature=0, model_name="qwen-turbo")
    # test_vector_db()
    test_retriever()
    # run_terminal(llm)
