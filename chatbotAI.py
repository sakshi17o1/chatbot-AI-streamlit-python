import streamlit as st
import google.generativeai as gai
import webbrowser

if "chat_data" not in st.session_state:
    st.session_state.chat_data = []


gai.configure(api_key="AIzaSyDYnr6UUlVT6q0n00zbOCllWdBSxu959VY")

model=gai.GenerativeModel("gemini-2.5-flash")

st.header("​🤖​ My Personal AI Bot")

st.subheader("💭 Ask anything in your mind...!")

user_input=st.chat_input("Write your query")

if user_input:
    st.session_state.chat_data.append(("Me", user_input))

    if "who build you" in user_input or "who make ypu" in user_input or "who devloped you"  in user_input:

        responce   = "I am an AI Model. Designd and developed by Sakshi in 2025."  
        st.session_state.chat_data.append(("Bot", responce))
    elif "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in user_input:
        webbrowser.open("www.google.com")


    else:
      
        responce=model.generate_content(user_input)
 
        st.session_state.chat_data.append(("Bot", responce.text))

for key,data in st.session_state.chat_data:
    with st.chat_message(key):
        if key=="​🙍​Me":
            st.markdown(f"​🙍​ {data}")
        else:
            st.markdown(f"​🤖​ {data}")
