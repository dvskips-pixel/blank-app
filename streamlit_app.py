import streamlit as st
from pathlib import Path
from streamlit.components.v1 import html

APP_FILE = Path(__file__).parent / "PHONE SYSTEM" / "index.html"

st.set_page_config(page_title="Awamu: phone lease desk", page_icon="📱", layout="wide")

# Let the embedded app own the whole viewport (no Streamlit chrome around it).
st.markdown(
    """
    <style>
      [data-testid="stHeader"], [data-testid="stStatusWidget"] { display: none; }
      [data-testid="stMain"], [data-testid="stMainBlockContainer"] { padding: 0 !important; }
      [data-testid="stMainBlockContainer"] > div { min-height: 100vh; }
      iframe[title="st.iframe"] { height: 100vh !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

html(APP_FILE.read_text(encoding="utf-8"), height=900, scrolling=True)
