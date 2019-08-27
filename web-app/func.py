from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
import pandas as pd

## Importing the dataframes
df = pd.read_csv('../datasets/comp_data3.csv')

recommender_df = pd.read_csv('../datasets/recommender_df.csv')


def suggestion(search):
    names = df.loc[df['name'].str.contains(search), 'name'][:5]

    return jsonify({'results': names})



def recommend_me(search):
    for title in df.loc[df['name'].str.contains(search), 'name']:
        print(title)
        recommendation = recommender_df[title].sort_values()[1:10]
    recom = pd.DataFrame(recommendation)
    recoms = pd.merge(df, recom, on = 'name')
    recommended_cat = df.loc[df['name'].str.contains(search),'category'].head(1).values[0]
    final = recoms[recoms['category']== recommended_cat]
    result = final[['name','brand', 'store','price','category']]
    return result
