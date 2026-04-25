import streamlit as st
import google.generativeai as genai

# 1. PAGE SETTINGS
st.set_page_config(
    page_title="BrainBox AI", 
    page_icon="🧠",
    layout="centered"
)

# 2. BRANDING SECTION - GLOBAL BUT SPECIALIZED
st.title("BrainBox AI 🧠")
st.subheader("Specialized for WAEC, JAMB, BECE & Post-UTME")
st.caption("Your exam-focused study partner. No signup. Just A1 answers.")
st.divider()

# 3. SETUP GEMINI BRAIN
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# 4. CHAT MEMORY
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. SHOW OLD MESSAGES WITH AVATARS
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar="👨‍🎓"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant", avatar="🧠"):
            st.markdown(message["content"])

# 6. USER INPUT BOX
if user_question := st.chat_input("Ask WAEC/JAMB/BECE/Post-UTME questions..."):
    
    # Show student question
    with st.chat_message("user", avatar="👨‍🎓"):
        st.markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})
    
    # 7. BRAINBOX AI SPECIALIZED PROMPT
    brainbox_prompt = f"""
    You are BrainBox AI, a specialist AI tutor for WAEC, JAMB, BECE & Post-UTME exams.
    
    STRICT MARKING SCHEME RULES:
    1. Answer like a WAEC/JAMB Chief Examiner. Use official marking scheme style
    2. For Maths/Physics/Chemistry: Show STEP BY STEP working. No step-skipping
    3. For OBJ questions: Give CORRECT OPTION first, then explain why in 2-3 bullet points
    4. For Theory: Structure answer like WAEC wants - Definition → Explanation → Examples → Diagram if needed
    5. For Essays: 200-250 words, 5 paragraphs. WAEC format: Intro, Body 1, Body 2, Body 3, Conclusion
    6. For JAMB/Post-UTME: Be fast, accurate. Speed matters. Give direct answers + quick reason
    7. Use simple English. Add pidgin example ONLY if it helps JSS2/SS3 student understand faster
    8. For non-exam gist: Still answer, but remind: "Sha no forget say WAEC/JAMB dey come o 😂"
    9. Never say "I
