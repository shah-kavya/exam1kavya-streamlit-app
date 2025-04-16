import streamlit as st
from Exam1Part1_Starter_kavyas import run_part1
from Exam1Part2_Starter_kavyas import run_part2

st.title("Automobile Data Analysis")

option = st.radio("Choose Part to Run:", ["Part 1: Data Cleaning & Prep", "Part 2: Visualization & Correlation"])

if option == "Part 1: Data Cleaning & Prep":
    run_part1()
elif option == "Part 2: Visualization & Correlation":
    run_part2()

