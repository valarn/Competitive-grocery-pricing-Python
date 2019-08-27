from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from forms import RegistrationForm, LoginForm
import pandas as pd
from sqlalchemy import create_engine
import os
import time
# from func import *
import func as custom
app = Flask(__name__)

posts = [
    {
        'author': 'Vala',
        'title': 'Web App to research Grocery products across different categories for R&D purposes',
        'date_posted': 'August 25, 2019'
    },
]


@app.route("/", methods=['GET', 'POST'])

@app.route("/home")
def Home():
    return render_template('home.html', title='Home Page')



@app.route('/charts')
def chart():
    return render_template('tableau.html')


@app.route('/recommend')
def search():

    return render_template('recommend.html')

# @app.route('/recommendation', methods = ['GET', 'POST'])
# def product_name():
#
#     processed_text = custom.suggestion(text)
#     return processed_text
    # if request.method == 'POST':
    #     text = request.form['text']
    #     if text.form =='':
    #         flash('No Product name written')
    #         return redirect('recommend.html')
    #     else:
    #         processed_text = text.upper()
    #
    #
    #     return render_template('recommendation.html',
    #     text = processed_text)

# @app.route('/recommendation', methods=("POST", "GET"))
# def html_table():
#     text = request.form['text']
#     final = custom.recommend_me(text)
#     return render_template('recommendation.html',  tables=[final.to_html(classes='data',index=False, header=True)], titles=custom.df.name.values, text=text)

@app.route('/recommendation')
def submit():
    user_input = request.form['text']
    # get user input from dict
    product = user_input["ProductName"]
    # run sort values code
    results = list(recommender_df[product].sort_values()[1:11].index)
    return jsonify({'results': results})




@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run(debug=True)
