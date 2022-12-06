#!/usr/bin/python3
"""aaaa"""
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """aaaa"""
    {"status": "OK"}