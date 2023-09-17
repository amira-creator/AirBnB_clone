#!/usr/bin/python3
"""This is Module determines Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is Class determines Review instance attribute."""

    place_id = ""
    text = ""
    user_id = ""
