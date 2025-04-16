
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_part1():
    st.header("Part 1: Data Cleaning and Preparation")

    filename = "https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/auto.csv"
    headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
            "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
            "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
            "peak-rpm","city-mpg","highway-mpg","price"]
    df = pd.read_csv(filename, names=headers)
    df.replace("?", np.nan, inplace=True)

    df["normalized-losses"] = df["normalized-losses"].astype("float")
    df["normalized-losses"].fillna(df["normalized-losses"].mean(), inplace=True)
    df["bore"] = df["bore"].astype("float")
    df["bore"].fillna(df["bore"].mean(), inplace=True)
    df["stroke"] = df["stroke"].astype("float")
    df["stroke"].fillna(df["stroke"].mean(), inplace=True)
    df["horsepower"] = df["horsepower"].astype("float")
    df["horsepower"].fillna(df["horsepower"].mean(), inplace=True)
    df["peak-rpm"] = df["peak-rpm"].astype("float")
    df["peak-rpm"].fillna(df["peak-rpm"].mean(), inplace=True)
    df["num-of-doors"].fillna("four", inplace=True)
    df.dropna(subset=["price"], inplace=True)
    df["price"] = df["price"].astype("float")
    df.reset_index(drop=True, inplace=True)

    df['city-L/100km'] = 235 / df['city-mpg'].astype('float')
    df['highway-L/100km'] = 235 / df['highway-mpg'].astype('float')
    df['length'] = df['length'].astype('float') / df['length'].astype('float').max()
    df['width'] = df['width'].astype('float') / df['width'].astype('float').max()
    df['height'] = df['height'].astype('float') / df['height'].astype('float').max()
    df["horsepower"] = df["horsepower"].astype(int)

    st.subheader("Cleaned Data Preview")
    st.dataframe(df.head())

    st.subheader("Horsepower Distribution (Histogram)")
    fig, ax = plt.subplots()
    ax.hist(df["horsepower"], bins=10)
    ax.set_xlabel("Horsepower")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
    group_names = ['Low', 'Medium', 'High']
    df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)

    st.subheader("Binned Horsepower Counts")
    st.bar_chart(df["horsepower-binned"].value_counts())

    dummy_variable_1 = pd.get_dummies(df["fuel-type"])
    dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
    df = pd.concat([df, dummy_variable_1], axis=1)
    df.drop("fuel-type", axis=1, inplace=True)

    dummy_variable_2 = pd.get_dummies(df["aspiration"])
    dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo':'aspiration-turbo'}, inplace=True)
    df = pd.concat([df, dummy_variable_2], axis=1)
    df.drop("aspiration", axis=1, inplace=True)

    st.subheader("Final Cleaned DataFrame with Dummies")
    st.dataframe(df.head())

    st.success(f"Final shape: {df.shape[0]} rows × {df.shape[1]} columns")
