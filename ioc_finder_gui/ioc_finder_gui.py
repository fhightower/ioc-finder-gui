#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import flash, Flask, render_template, redirect, request, url_for, jsonify
import ioc_finder

app = Flask(__name__)
app.secret_key = 'abc'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/find", methods=['POST'])
def find_iocs():
    """Find indicators of compromise."""
    text = request.form['text']

    if not text:
        flash('Please enter some text.', 'error')
        return redirect(url_for('index'))
    else:
        iocs = ioc_finder.find_iocs(text)
        return jsonify(iocs)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
