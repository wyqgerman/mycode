#!/usr/bin/env python3

from flask_wtf import FlaskForm as Form
from wtforms import RadioField
from wtforms.validators import ValidationError
from random import randrange


class CorrectAnswer(object):
    def __init__(self, answer):
        self.answer = answer

    def __call__(self, form, field):
        message = 'Try again.'

        if field.data != self.answer:
            raise ValidationError(message)


class PopTrivia(Form):
    class Meta:
        csrf = False
    q1 = RadioField(
        "The answer to question one is False.",
        choices=[('True', 'True'), ('False', 'False')],
        validators=[CorrectAnswer('False')]
        )
