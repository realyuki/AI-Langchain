from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI
import os
import streamlit as st

# 환경 변수 로드
load_dotenv()

# OpenAI API 키를 환경 변수에서 가져오기
openai_api_key = os.getenv("OPENAI_API_KEY")

# OpenAI LLM 및 ChatOpenAI 모델 생성
llm = OpenAI(openai_api_key=openai_api_key)
chat_model = ChatOpenAI(openai_api_key=openai_api_key)

# 요청할 내용
content = st.text_input('시의 주제를 제시해 주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성중...'):
      result = chat_model.invoke(content + "에 대한 시를 써줘")
      st.write(result.content)