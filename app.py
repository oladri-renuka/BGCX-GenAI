#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
from PIL import Image

logo = Image.open("BCGX.jpg")

col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    st.write("")

with col2:
    st.image(logo, use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>BCG GenAI Predefined Chatbot</h1>", unsafe_allow_html=True)

with col3:
    st.write("")

def simple_chatbot(user_query):
    if user_query == "What is the average revenue growth for Apple?":
        return "Apple's average revenue growth was approximately 7.8% in 2021 and 2022. However, it decreased to -2.8% in 2023."
    elif user_query == "How has Tesla's net income changed in 2023?":
        return "Tesla's net income growth decreased to 19.3% in 2023 from 127.5% in 2021 and 2022. This shows a significant decline in growth."
    elif user_query == "What was Microsoft's cash flow growth in 2021?":
        return "Microsoft's cash flow from operating activities grew by approximately 16% in 2021."
    elif user_query == "How did Apple's assets change in 2023?":
        return "Apple's total assets saw a slight decrease of 0.05% in 2023."
    elif user_query == "What is the liability growth for Tesla in 2022?":
        return "Tesla's total liabilities grew by 19.3% in 2022."
    elif user_query == "What is the total revenue for Microsoft in 2022?":
        return "Microsoft's total revenue for 2022 was approximately 17.96% higher than the previous year."
    elif user_query == "How did the net income of Apple change from 2021 to 2023?":
        return "Apple's net income grew by 5.41% in 2021 and 2022 but declined by 2.81% in 2023."
    elif user_query == "What is the average growth of total assets for Tesla over the years?":
        return "Tesla's average growth of total assets was approximately 32.52% in 2021 and 2022, and it slightly decreased to 29.49% in 2023."
    elif user_query == "How did cash flow from operating activities change for Microsoft in 2023?":
        return "Microsoft's cash flow from operating activities decreased by 1.63% in 2023 compared to the previous year."
    elif user_query == "What was the average growth of total liabilities for Apple over the years?":
        return "Apple's average growth of total liabilities was around 4.92% in 2021 and 2022 but saw a decrease in 2023."
    elif user_query == "How did the net income of Tesla change from 2021 to 2023?":
        return "Tesla's net income growth was very high at 127.5% in 2021 and 2022, but it dropped to 19.26% in 2023."
    elif user_query == "What was the revenue growth for Microsoft in 2021 and 2022?":
        return "Microsoft's revenue growth was 17.96% in both 2021 and 2022."
    elif user_query == "How did the assets of Microsoft change in 2023?":
        return "Microsoft's total assets grew by approximately 12.92% in 2023."
    elif user_query == "What was the growth rate of cash flow from operating activities for Tesla in 2022?":
        return "Tesla's cash flow from operating activities had a growth rate of 28.07% in 2022."
    else:
        return "Sorry, I can only provide information on predefined queries."

st.write("Select a question about the financial data of Apple, Microsoft, or Tesla:")

user_query = st.selectbox(
    "Choose a query",
    [
        "What is the average revenue growth for Apple?",
        "How has Tesla's net income changed in 2023?",
        "What was Microsoft's cash flow growth in 2021?",
        "How did Apple's assets change in 2023?",
        "What is the liability growth for Tesla in 2022?",
        "What is the total revenue for Microsoft in 2022?",
        "How did the net income of Apple change from 2021 to 2023?",
        "What is the average growth of total assets for Tesla over the years?",
        "How did cash flow from operating activities change for Microsoft in 2023?",
        "What was the average growth of total liabilities for Apple over the years?",
        "How did the net income of Tesla change from 2021 to 2023?",
        "What was the revenue growth for Microsoft in 2021 and 2022?",
        "How did the assets of Microsoft change in 2023?",
        "What was the growth rate of cash flow from operating activities for Tesla in 2022?"
    ]
)

if st.button("Submit"):
    response = simple_chatbot(user_query)
    st.write(response)


# In[ ]:




