
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def run_part2():
    st.header("Part 2: Data Visualization and Correlation")
        
    path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
    df = pd.read_csv(path)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Selected Correlation Matrix")
    selected_columns = df[['bore', 'stroke', 'compression-ratio', 'horsepower']]
    st.dataframe(selected_columns.corr())

    st.subheader("Engine Size vs Price")
    fig, ax = plt.subplots()
    sns.regplot(x="engine-size", y="price", data=df, ax=ax)
    ax.set_ylim(0,)
    st.pyplot(fig)

    st.subheader("Highway MPG vs Price")
    fig, ax = plt.subplots()
    sns.regplot(x="highway-mpg", y="price", data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("Peak RPM vs Price")
    fig, ax = plt.subplots()
    sns.regplot(x="peak-rpm", y="price", data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("Stroke vs Price")
    fig, ax = plt.subplots()
    sns.regplot(x="stroke", y="price", data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("Box Plots")
    for col in ["body-style", "engine-location", "drive-wheels"]:
        fig, ax = plt.subplots()
        sns.boxplot(x=col, y="price", data=df, ax=ax)
        st.pyplot(fig)

    st.subheader("Grouped Averages (Drive-wheels and Body-style)")
    df_grouped = df[['drive-wheels','body-style','price']].groupby(['drive-wheels','body-style'],as_index=False).mean()
    pivot = df_grouped.pivot(index='drive-wheels', columns='body-style', values='price').fillna(0)
    st.dataframe(pivot)

    st.subheader("Heatmap")
    fig, ax = plt.subplots()
    im = ax.pcolor(pivot, cmap='RdBu')
    ax.set_xticks(np.arange(pivot.shape[1]) + 0.5)
    ax.set_yticks(np.arange(pivot.shape[0]) + 0.5)
    ax.set_xticklabels(pivot.columns, rotation=90)
    ax.set_yticklabels(pivot.index)
    fig.colorbar(im)
    st.pyplot(fig)

    st.subheader("Pearson Correlations with Price")
    corr_vars = ['wheel-base', 'horsepower', 'length', 'width', 'curb-weight', 'engine-size', 'bore', 'city-mpg', 'highway-mpg']
    for var in corr_vars:
        pearson_coef, p_value = stats.pearsonr(df[var], df['price'])
        st.write(f"{var} → r = {pearson_coef:.3f}, p = {p_value:.5f}")
