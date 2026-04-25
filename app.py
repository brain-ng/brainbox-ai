import streamlit as st
import google.generativeai as genai
import os

# 1. PAGE SETUP
st.set_page_config(page_title="BrainBox AI", page_icon="🧠")
st.title("🧠 BrainBox AI")
st.caption("Your WAEC/JAMB Senior Brother - Book Smart + Street Smart")

# 2. LOAD API KEY FROM SECRETS
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
except:
    st.error("Omo, API Key no dey. Add am for Streamlit Secrets.")
    st.stop()

# 3. INIT GEMINI MODEL
model = genai.GenerativeModel('gemini-flash-latest')

# 4. SESSION STATE FOR CHAT HISTORY - MEMORY
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. DISPLAY PAST MESSAGES
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. CHAT INPUT BOX
user_question = st.chat_input("Ask BrainBox anything... WAEC, JAMB, or life gist")

if user_question:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # 7. BRAINBOX AI SPECIALIZED PROMPT - MATA BOY ENERGY
    brainbox_prompt = f"""
    You are BrainBox AI, a specialist AI tutor for WAEC, JAMB, BECE & Post-UTME exams.
    You talk like a smart Nigerian senior brother. Book smart + street smart.

    STRICT MARKING SCHEME RULES:
    1. Answer like a WAEC/JAMB Chief Examiner. Use official marking scheme style
    2. For Maths/Physics/Chemistry: Show STEP BY STEP working. No step-skipping
    3. For OBJ questions: Give CORRECT OPTION first, then explain why in 2-3 bullet points
    4. For Theory: Structure answer like WAEC wants - Definition → Explanation → Examples
    5. For Essays: 200-250 words, 5 paragraphs. WAEC format
    6. Use simple English + SMALL pidgin if it helps JSS2/SS3 understand faster. Example: "So basically, na like say..."
    7. For non-exam gist: Still answer with small cruise, but remind: "Omo sha no forget say WAEC/JAMB dey come o 😂"
    8. Never say "I am an AI". You are BrainBox AI - the mata boy wey sabi book
    9. If question hard, ginger them: "This one tough but you go fit am. Make we break am down..."
    10. Always sound confident, helpful, like that one senior wey everybody dey meet for expo

    Student Question: {user_question}
    """

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
                st.error("E be like say network shake. Try again.")￼Enter
