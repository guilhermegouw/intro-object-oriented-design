from datetime import datetime
from typing import Optional


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        isbn: str,
        is_available: bool = True,
        due_date: Optional[datetime] = None,
    ):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
        self.due_date = due_date

    def is_overdue(self) -> bool:
        if self.due_date is None or self.is_available:
            return False
        return datetime.now() > self.due_date
