import os
os.system('python download.py')
os.system('streamlit run app-rag-with-chroma.py --server.address=0.0.0.0 --server.port 7860')