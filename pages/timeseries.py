import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

yt_channels = ['Варламов Talks', 'Сергей Гуриев', 'Живой гвоздь (эхо)', 'Майкл Наки',
       'Екатерина Шульман', 'Популярная политика', 'Максим Кац',
       'Михаил Ходорковский', 'Илья Яшин', 'Котрикадзе Дзядко', 'Объектив',
       'Михаил Фишман', 'Билд на русском', 'Фишман', 'Живой гвоздь',
       'Леонид Волков', 'Varlamov News', 'Колезев', 'Ходорковский LIVE',
       'Екатерина Дунцова', 'Борис Надеждин', 'Дарья Беседина',
       'Продолжение следует', 'Александр Штефанов', 'The Breakfast Show',
       'CIT', 'И Грянул Грэм', 'ГражданинЪ TV', 'Yulia Latynina']

options = st.multiselect("Choose one or more youtube channels:", yt_channels, default=['Максим Кац', 'Варламов Talks'])

df = pd.read_excel("data/followers_timeseries.xlsx", parse_dates=['date'])
df_changes = pd.read_excel("data/followers_changes_timeseries.xlsx", parse_dates=['date'])
df_changes.set_index('date', inplace=True)
df.set_index('date', inplace=True)
st.line_chart(df[options], y_label="Подписчики в тыс.")
st.area_chart(df_changes[options], y_label="Новые подписчики в тыс.")