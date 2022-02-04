#!/usr/bin/python3
"""
This module contains the class: BaseModel.
"""
import uuid
from datetime import datetime
import models
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    This class is the superclass for all subsequent classes for
    the AirBnB clone project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated-at':
                    value = datetime.strptime(key, time)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all keys/values of the object.
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
