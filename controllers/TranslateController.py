# -*- coding: utf-8 -*-
"""
Onyx Project
https://onyxlabs.fr
Software under licence Creative Commons 3.0 France
http://creativecommons.org/licenses/by-nc-sa/3.0/fr/
You may not use this software for commercial purposes.
"""

from translate_skill.index import translate
from flask_login import login_required
from flask import render_template

from translate_skill.api import *


@translate.route('/' , methods=['GET','POST'])
@login_required
def index():
    return render_template('translate/index.html')

@translate.route('/config' , methods=['GET','POST'])
@login_required
def config():
    return render_template('translate/config.html')

@translate.route('/widget')
@login_required
def widget():
    return render_template('translate/widget.html')
