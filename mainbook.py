import pickle
from abc import ABC, abstractmethod
from collections import UserDict


class AbcStorage(ABC):
    """Abstract class for Mainbook"""

    @abstractmethod
    def save_to_file(self, fh):
        pass

    @abstractmethod
    def load_from_file(self, fh):
        pass


class MainBook(AbcStorage, UserDict):
    """Parent class for notebook and contact book"""

    def save_to_file(self, fh):
        """Saving data to file"""
        with open(fh, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, fh):
        """Load data from file"""
        try:
            with open(fh, 'rb') as file:
                self.data = pickle.load(file)

        except FileNotFoundError:
            pass

