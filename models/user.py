#!/usr/bin/python3
"""
This module contains the subclass: User
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    This class is a subclass of BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
