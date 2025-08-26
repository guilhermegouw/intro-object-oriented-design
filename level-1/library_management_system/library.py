from typing import List, Optional

from library_management_system.book import Book
from library_management_system.member import Member


class Library:
    def __init__(
        self, books: Optional[List[Book]] = None, members: Optional[List[Member]] = None
    ):
        self.books = books if books is not None else []
        self.members = members if members is not None else []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def add_member(self, member: Member) -> None:
        self.members.append(member)

    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member_by_id(self, member_id: str) -> Optional[Member]:
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
