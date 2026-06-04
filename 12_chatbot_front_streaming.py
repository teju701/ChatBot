import streamlit as st
from langgraph11_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG={'configurable':{'thread_id':'threadid-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

#to print old messags:-it loops through all the previos conversation and print it on the display
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])

user_input=st.chat_input('Type here...')
if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.write(user_input)

    with st.chat_message('assistant'):

        ai_message=st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages':[HumanMessage(content=user_input)]},
                config={'configurable':{'thread_id':'threadid-1'}},
                stream_mode='messages'
            )
        )
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})