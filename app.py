import streamlit as st
from exam1part1_starter_kavya(2) import run_part1
from exam1part2_starter_kavya(2) import run_part2

st.title("Automobile Data Analysis")

option = st.radio("Choose Part to Run:", ["Part 1: Data Cleaning & Prep", "Part 2: Visualization & Correlation"])

if option == "Part 1: Data Cleaning & Prep":
    run_part1()
elif option == "Part 2: Visualization & Correlation":
    run_part2()
