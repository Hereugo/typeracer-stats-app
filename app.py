import streamlit as st
import pandas as pd

username: str = st.text_input('Username', 'hereugo')

df: pd.DataFrame = pd.read_csv(f'{username}_history.csv')

st.line_chart(df, x='date', y='speed')
