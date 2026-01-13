import streamlit as st
import pandas as pd

st.title(" Любими неща класна анкета")

# Инициализация на данните
if "subjects" not in st.session_state:
    st.session_state.subjects = {
        "Математика": 0,
        "Български": 0,
        "Програмиране": 0,
        "Физическо": 0,
        "Физика": 0
    }
if "colors" not in st.session_state:
    st.session_state.colors = {
        "red": 0,
        "orange": 0,
        "yellow": 0,
        "green": 0,
      "blue": 0
      }
  
if "grades" not in st.session_state:
    st.session_state.grades = {
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
      "2": 0
      }
  
st.subheader("Избери любими неща")

subject = st.selectbox("Любим предмет:", list(st.session_state.subjects.keys()))
grade = st.selectbox("Оценки:", list(st.session_state.grades.keys()))
color = st.selectbox("Оценки:", list(st.session_state.colors.keys()))

if st.button("Запази избора"):
    st.session_state.subjects [subject] += 1
    st.session_state.grades [grade] += 1
    st.session_state.colors [color] += 1
    st.success("Изборът е записан!")
  
st.divider()

st.subheader(" Резултати")

# Графика за цветовете
st.write("Любими цветове")
subjects_df = pd.DataFrame.from_dict(
    st.session_state.subjects, orient="index", columns=["Брой"]
)

st.bar_chart(subjects_df)

# Графика за спортовете
st.write("Любими спортове")
grades_df = pd. DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой"]
)
st.bar_chart(grades_df)

st.write("Любими спортове")
colors_df = pd. DataFrame.from_dict(
    st.session_state.colors, orient="index", columns=["Брой"]
)
st.bar_chart(colors_df)
