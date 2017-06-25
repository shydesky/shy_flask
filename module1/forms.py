# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import (PasswordField, StringField, IntegerField, TextField)
from wtforms.validators import DataRequired, Email, EqualTo, Length, AnyOf

class Module1Form(Form):
    email = StringField('email', [Email('ss')], default='')

    def __init__(self, *args, **kwargs):
        super(Module1Form, self).__init__(*args, **kwargs)
