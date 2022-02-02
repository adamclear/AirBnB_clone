#!/usr/bin/python3
"""
This module contains the class: BaseModel.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    This class is the superclass for all subsequent classes for
    the AirBnB clone project.
    """

    def __init__(self):
        """
        Initializes the object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        String representation for printing.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary of all keys/values of the object.
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict
