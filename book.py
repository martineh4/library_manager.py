# book.py

class Book:
    """A class representing a book with a title, author, and ISBN"""
    def __init__(self, title: str, author: str, isbn: str):
        """
        Initialize a book instance

        Args:
            title (str): Title of the book
            author (str): Author of the book
            isbn (str): ISBN of the book
        """
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        """Returns a string representation of the book"""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
    def get_details(self):
        """Returns a dictionary containing details of the book"""
        return {
            "title": self.title,
            "author": self.author,
            "ISBN": self.isbn
        }
