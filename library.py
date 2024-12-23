#  Library Management System
# Build a system to manage library books and members.
# Features:
# Add books and members.
# Borrow and return books.
# Track which books are borrowed and by whom

class Library:
    def __init__(self,books,mem):
        self.books = books
        self.members = mem
    def activity(self,name,borrow):
        self.name = {'name': name}
        self.borrow ={'Borrowed book name' : borrow}
        
