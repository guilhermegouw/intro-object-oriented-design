class Member:
    def __init__(
        self, name: str, member_id: str, email: str, borrowed_books_count: int = 0
    ):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.borrowed_books_count = borrowed_books_count
