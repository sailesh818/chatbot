import os
import streamlit as st
from groq import Groq


groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"system", "content":"You are a helpful assistant. You help with users' queries."}
    ]
    
st.title("Chat with bot")

# chat display here code
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
if prompt := st.chat_input("Ask anything...."):
    st.session_state.messages.append({"role":"user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        with st.spinner("Thinking.."):
            response = groq_client.chat.completions.create(
                model="llama3-70b-8192",
                messages=st.session_state.messages,
                max_tokens=500,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
            
    st.session_state.messages.append({"role":"assistant", "content":reply})
        
