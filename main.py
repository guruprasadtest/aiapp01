import streamlit as st
st.title("Tweet Generator")
st.subheader("Using GPT model to generate tweets")
topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)
button = st.button("Generate")


from langchain_openai import ChatOpenAI
import os
os.environ['OPENAI_API_KEY'] = "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"
gpt3 = ChatOpenAI(model = "gpt-3.5-turbo")

from langchain import PromptTemplate

tweet_template = """
Give me {number} tweets on {topic}, be bold, say
"""

tweet_prompt = PromptTemplate(template=tweet_template, input_variables = ['number', 'topic'])

from langchain import LLMChain

tweet_chain = LLMChain(
    prompt=tweet_prompt,
    llm=gpt3
)

if button:
    output = tweet_chain.run(number=number, topic=topic)
    st.write(output)
