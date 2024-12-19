import streamlit as st
from langchain_openai import OpenAI
from langchain import PromptTemplate

st.set_page_config(
    page_title = "DadBot"
)

st.title("DadBot 0.1")

openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type = "password"
)

def generate_response(topic):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    As a loving father, your priorities are in order:
    1. Your children's happiness
    2. Peace and unity in the family
    3. Safety for current and future generations
    4. Propagation of the family with grandchildren raised in loving homes

    Based on principles of wisdom, harmony, and virtue, consider the most important points about {topic}. 
    Then generate a 400-word blog post for your children in a style that is reflective, insightful, and warm.
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    """
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )
    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    return st.write(response)


topic_text = st.text_input("Enter topic: ")
if not openai_api_key.startswith("sk-"):
    st.warning("Enter OpenAI API Key")
if openai_api_key.startswith("sk-"):
    generate_response(topic_text)
        
