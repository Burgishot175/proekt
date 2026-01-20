import streamlit as st
import pandas as pd

st.title(" Любими неща класна анкета")

# Инициализация на данните
if "subjects" not in st.session_state:
    st.session_state.subjects = {
        "Поп": 0,
        "Рап": 0,
        "Джаз": 0,
        "Рок": 0,
        "Чалга": 0
    }
if "colors" not in st.session_state:
    st.session_state.colors = {
        "Червен": 0,
        "Оранжев": 0,
        "Жълт": 0,
        "Зелен": 0,
      "Син": 0
      }
  
if "grades" not in st.session_state:
    st.session_state.grades = {
        "Български": 0,
        "Математика": 0,
        "Физическо": 0,
        "Програмиране": 0,
      "Физика": 0
      }
  
st.subheader("Избери любими неща")

subject = st.selectbox("Любим жанр музика:", list(st.session_state.subjects.keys()))
grade = st.selectbox("Любим предмет:", list(st.session_state.grades.keys()))
color = st.selectbox("Любим цвят:", list(st.session_state.colors.keys()))

if st.button("Запази избора"):
    st.session_state.subjects [subject] += 1
    st.session_state.grades [grade] += 1
    st.session_state.colors [color] += 1
    st.success("Изборът е записан!")
  
st.divider()

st.subheader(" Резултати")

# Графика за цветовете
st.write("Любим жанр музика")
subjects_df = pd.DataFrame.from_dict(
    st.session_state.subjects, orient="index", columns=["Брой"]
)

st.bar_chart(subjects_df)

# Графика за спортовете
st.write("Любими предмети")
grades_df = pd. DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой"]
)
st.bar_chart(grades_df)

st.write("Любими цветове")
colors_df = pd. DataFrame.from_dict(
    st.session_state.colors, orient="index", columns=["Брой"]
)
st.bar_chart(colors_df)
