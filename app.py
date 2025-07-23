import streamlit as st
from coding_data import coding_questions

custom_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    position: relative;
}

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    backdrop-filter: blur(12px);
    background-color: rgba(0,0,0,0.3);
    z-index: -1;
}

/* Box for chatbot heading, inputs, answers */
.black-box {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 1rem 1.5rem;
    border-radius: 10px;
    color: white;
    margin: 1.5rem 0;
    font-size: 1.1rem;
    width: fit-content;
}

/* Make caption readable */
.caption-style {
    background-color: rgba(0, 0, 0, 0.4);
    color: white !important;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    display: inline-block;
    margin-top: 1rem;
}

[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
</style>
"""


st.markdown(custom_css, unsafe_allow_html=True)
# --- Title & Input ---
st.title("🧠 Coding Practice Chatbot")
st.markdown("Ask me a coding question:")
user_input = st.text_input("")
st.caption(
    "Try typing things like 'prime', 'palindrome', or 'greatest of 3 numbers'")


# --- Download Button Function ---
def generate_download_button(code_str, filename):
    st.download_button(
        label="📥 Download Code",
        data=code_str,
        file_name=filename,
        mime="text/plain"
    )


# --- Chatbot Logic ---
if user_input:
    found = False
    for question, code in coding_questions.items():
        if user_input.lower() in question.lower():
            st.subheader(f"Here's your answer for: {question}")
            st.code(code, language='python')
            filename = f"{question.replace(' ', '_').lower()}.py"
            generate_download_button(code, filename)
            found = True
            break
    if not found:
        st.warning(
            "❌ Sorry, I don't know that yet. Try asking for 'Palindrome' or 'Prime number check'.")
