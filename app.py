import streamlit as st
import google.generativeai as genai
from google.generativeai import types

st.set_page_config(page_title="BrainBox NG", page_icon="🧠")
st.title("🧠 BrainBox NG")

# --- SYSTEM PROMPT - BIG BRO VIBE ---
SYSTEM_PROMPT = """
You are BrainBox NG. You be that senior tech bro for area wey sabi book pass.

CRITICAL RULE: NEVER MENTION GOOGLE, GEMINI, or AI MODEL. 
If they ask "who build you", "are you ChatGPT", "are you Gemini", reply: 
"My CEO Dare Temitayo build me from scratch. Na why I sabi Naija like this. I no be imported AI 😎"

Talk like big bro: Mix English + Pidgin. Call them "boss", "chief", "omo". 
Short answers 3-5 lines. Naija examples only. Always hype them at end.
No sugarcoat. If you no know, say "Omo I no sure".

Now respond to user.
"""

# --- SETUP ---
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=GEMINI_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask BrainBox anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("BrainBox dey think..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,  # <-- THIS LINE IMPORTANT
                    temperature=0.8
                )
            )
            answer = response.text
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

    # 8. GENERATE ANSWER WITH SPINNER
    with st.chat_message("assistant"):
        with st.spinner("BrainBox dey cook the answer..."):
            try:
                response = model.generate_content(brainbox_prompt)
                answer = response.text
                st.markdown(answer)
                # Save to chat history for memory
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error("E be like say network shake. Try again.")
