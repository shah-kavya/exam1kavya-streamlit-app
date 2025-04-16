import streamlit as st
import pandas as pd
import numpy as np

def run_part2():
    st.header("Part 2: Data Visualization and Correlation")
        
    path='https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
    df = pd.read_csv(path)
    df.head()

    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline

    # list the data types for each column
    print(df.dtypes)

    # Write your code below and press Shift+Enter to execute
    print(df.dtypes['peak-rpm'])

    df.corr(numeric_only=True)

    # Write your code below and press Shift+Enter to execute
    selected_columns = df[['bore', 'stroke', 'compression-ratio', 'horsepower']]
    correlation_matrix = selected_columns.corr()
    print(correlation_matrix)

    # Engine size as potential predictor variable of price
    sns.regplot(x="engine-size", y="price", data=df)
    plt.ylim(0,)

    df[["engine-size", "price"]].corr()

    sns.regplot(x="highway-mpg", y="price", data=df)

    df[['highway-mpg', 'price']].corr()

    sns.regplot(x="peak-rpm", y="price", data=df)

    df[['peak-rpm','price']].corr()

    # Write your code below and press Shift+Enter to execute
    df[["stroke","price"]].corr()

    # Write your code below and press Shift+Enter to execute
    sns.regplot(x="stroke", y="price", data=df)

    sns.boxplot(x="body-style", y="price", data=df)

    sns.boxplot(x="engine-location", y="price", data=df)

    # drive-wheels
    sns.boxplot(x="drive-wheels", y="price", data=df)

    df.describe()

    df.describe(include=['object'])

    df['drive-wheels'].value_counts()

    df['drive-wheels'].value_counts().to_frame()

    drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
    drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
    drive_wheels_counts

    drive_wheels_counts.index.name = 'drive-wheels'
    drive_wheels_counts

    # engine-location as variable
    engine_loc_counts = df['engine-location'].value_counts().to_frame()
    engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
    engine_loc_counts.index.name = 'engine-location'
    engine_loc_counts.head(10)

    df['drive-wheels'].unique()

    df_group_one = df[['drive-wheels','body-style','price']]

    # grouping results
    df_group_one = df_group_one.groupby(['drive-wheels' , 'body-style'],as_index=False).mean()
    df_group_one

    # grouping results
    df_gptest = df[['drive-wheels','body-style','price']]
    grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
    grouped_test1

    grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
    grouped_pivot

    grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
    grouped_pivot

    # Write your code below and press Shift+Enter to execute
    df_group_two = df[['body-style', 'price']].groupby('body-style', as_index=False).mean().round(2)
    print(df_group_two)


    import matplotlib.pyplot as plt
    %matplotlib inline

    #use the grouped results
    plt.pcolor(grouped_pivot, cmap='RdBu')
    plt.colorbar()
    plt.show()

    fig, ax = plt.subplots()
    im = ax.pcolor(grouped_pivot, cmap='RdBu')

    #label names
    row_labels = grouped_pivot.columns.levels[1]
    col_labels = grouped_pivot.index

    #move ticks and labels to the center
    ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

    #insert labels
    ax.set_xticklabels(row_labels, minor=False)
    ax.set_yticklabels(col_labels, minor=False)

    #rotate label if too long
    plt.xticks(rotation=90)

    fig.colorbar(im)
    plt.show()

    df.corr(numeric_only=True)

    from scipy import stats

    pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

    pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

    pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

    pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )

    pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
    print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

    pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

    pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value )

    pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

    pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
    print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value )