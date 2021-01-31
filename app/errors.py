from flask import render_template


def page_not_found(e):
    return render_template("errors/404.html")

#TODO add error handlers for most popular HTTP codes