import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import pandas as pd

st.write("""
# Simple stock Price APP

Show are the stock closing price and volume of Google!

""")
nowDate = datetime.strftime(datetime.now(), '%Y-%m-%d')
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickeDf = tickerData.history(period='1d', start='2010-1-1', end=nowDate)

st.write(""" 
    ## Closing Price
""")
st.line_chart(tickeDf.Close)
st.write(""" 
    ## Volume Price
""")
st.line_chart(tickeDf.Volume)

