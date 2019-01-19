    # -*- coding: utf-8 -*-

from flask import render_template, request, url_for, redirect, jsonify, flash, session, abort, current_app
from htmlmin.minify import html_minify
from functools import wraps
from libraries.repo import Repo
from plugins.helper import Helper
import config.app as APP

def render(name, **kwargs):
    # Injecting helper variables
    platform = {
        'CSRF_TOKEN':Repo.csrfToken()
    }
    configs = {
        'SITE_NAME':APP.SITE_NAME
    }
    
    # Checking and injecting Session variables
    plugins = {
        'helper':Helper
    }

    # Validating and returning template
    name = ("desktop/" if not request.MOBILE else "mobile/") + name
    data = ''
    # Minifying HTML file
    data = html_minify(render_template(name+".html",
        platform=platform, 
        configs=configs,
        plugins=plugins,
    **kwargs))

    # Checking if the request is AJAX based
    if request.is_xhr:
        for r in ['<html>','<head>','</head>','<body>','</body>','</html>']: data = data.replace(r,'')
    return data