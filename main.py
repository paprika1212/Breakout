import streamlit as st
from Fetchify.components.sidebar import sidebar
import pandas as pd
from io import StringIO

st.set_page_config(page_title="Fetchify", page_icon="🔎", layout="wide")
st.header("Fetchify 🔎")
sidebar()


openai_api_key = st.session_state.get("OPENAI_API_KEY")
if not openai_api_key:
    st.warning(
        "Enter your OpenAI API key in the sidebar. You can get a key at"
        " https://platform.openai.com/account/api-keys."
    )


csv_file = st.file_uploader("Upload a CSV file")