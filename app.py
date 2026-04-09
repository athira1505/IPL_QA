import streamlit as st
from src.pipeline import answer_question
import base64

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(layout="wide")

# --------------------------
# BACKGROUND IMAGE (LOCAL)
# --------------------------
def set_bg():
    with open("background.jpg", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                        url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* REMOVE TOP BAR */
        header {{visibility: hidden;}}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}

        /* CENTER CONTENT */
        .block-container {{
            padding-top: 15vh;
        }}

        /* REMOVE DARK BOX */
        div[data-testid="stVerticalBlock"] > div {{
            background-color: transparent !important;
        }}

        /* TITLE */
        h1 {{
            color: white !important;
            text-align: center;
            font-size: 55px !important;
        }}

        /* LABEL */
        label {{
            color: white !important;
            font-size: 18px !important;
        }}

        /* INPUT */
        .stTextInput>div>div>input {{
            border-radius: 10px;
            height: 50px;
            font-size: 18px;
        }}

        /* BUTTON CENTER */
        .stButton {{
            display: flex;
            justify-content: center;
        }}

        .stButton>button {{
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            height: 50px;
            width: 200px;
            font-size: 18px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

# --------------------------
# TITLE
# --------------------------
st.markdown("<h1>🏏 IPL Question Answering System</h1>", unsafe_allow_html=True)

# --------------------------
# CENTERED INPUT AREA
# --------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    q = st.text_input("Ask a question...")

    if st.button("Get Answer"):
        if q:
            ans = answer_question(q)

            # --------------------------
            # CLEAN ANSWER BOX
            # --------------------------
            st.markdown(
    f"""
    <div style="
        background: rgba(34, 139, 34, 0.5);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        text-align: center;
        font-size: 20px;
        font-weight: 500;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
    ">
        {ans}
    </div>
    """,
    unsafe_allow_html=True
)