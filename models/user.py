#!/usr/bin/python3
"""This is Module determines the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is Class determines User instance attributes"""

    email = ""
    first_name = ""
    password = ""
    last_name = ""
