import os
APP_DIR = os.getenv('APP_DIR','/')
os.chdir(APP_DIR)

from eda_basketball import basketball_app
from eda_cryptocurrency import crypto_price_app
from eda_football import football_app
from eda_sp_500 import sp_500
import streamlit as st
from multiapp import MultiApp

# page expands to full width
st.set_page_config(
        page_title="Data Science APP`S",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

app = MultiApp()

app.add_app("(NBA)Baketball Data", basketball_app.view)
app.add_app("Crypto Price Data", crypto_price_app.view)
app.add_app("(NFL)Fotball Data", football_app.view)
app.add_app("S&P500 Companyes Price", sp_500.view)


app.run()