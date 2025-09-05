import os
from datetime import datetime
import streamlit as st
st.caption("Version : " + datetime.fromtimestamp(os.path.getmtime(__file__)).strftime("%d/%m/%Y %H:%M:%S"))

@echo off
cd /d "C:\Users\kleso\OneDrive\Desktop\bot_trading\streamlit_app"
streamlit run streamlit_app.py
pause
