# -*- coding: utf-8 -*-

from flask import Flask, request, session, abort, url_for, g
from flask_mobility import Mobility
from flask_cors import CORS

# Controllers
from controllers import HomeController
from controllers import ErrorController
from controllers import ScraperController

#Other
from libraries.repo import Repo
from datetime import timedelta

# Config
import config.app as APP

# Setting up Error Handler

site = Flask(__name__, static_folder="assets")
site.permanent_session_lifetime = timedelta(days=APP.SESSION_DAYS) 
Mobility(site)
CORS(site)

# Enables no-caching

@site.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'public, max-age=604800'
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# CSRF Protection

@site.before_request
def csrf_protection():
    exceptions = [
        url_for('test')
    ]
    if request.method != 'GET' and request.path not in exceptions:
        token = session.get('csrf_token')
        if not token or token != request.form.get('csrf_token'): abort(403)

route = site.add_url_rule # different name for definition

# Guest Routes

route('/', 'index', HomeController.index, methods=['GET', 'POST'])
route('/privacy', 'privacy', HomeController.privacy)
route('/terms', 'terms', HomeController.tos)

route('/scraper/home', 'scraper:home', ScraperController.home, methods=['POST', 'GET'])

route('/database/manage', 'database:manage', ScraperController.database_manage, methods=['GET', 'POST'])

# Error Routes

@site.errorhandler(400) # Bad Request
def bad_request(code): return ErrorController.show(400)

@site.errorhandler(401) # Unauthorized
def unauthorize(code): return ErrorController.show(401)

@site.errorhandler(403) # Not Allowed
def not_allowed(code): return ErrorController.show(404)

@site.errorhandler(404) # Not Found
def not_found(code): return ErrorController.show(404)

@site.errorhandler(405) # Method not allowed
def method_not_allowed(code): return ErrorController.show(405)

@site.errorhandler(500) # Internal Error
def internal_error(code): return ErrorController.show(500)

@site.errorhandler(501) # Not Implemented
def not_implemented(code): return ErrorController.show(501)

@site.errorhandler(502) # Bad Gateway
def bad_gateway(code): return ErrorController.show(502)

@site.errorhandler(503) # Service Unavailable
def service_unavailable(code): return ErrorController.show(503)

@site.errorhandler(504) # Gateway timeout
def gateway_timeout(code): return ErrorController.show(504)

# Testing
route('/test', 'test', HomeController.test, methods=['GET','POST'])