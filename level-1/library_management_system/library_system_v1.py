"""
Library Management System - Version 1

Problems of Design:
    1. Library responsibilities:
        - Manage books (add, remove, update)
        - Manage members (add, remove, update)
        - Handle book checkouts and returns
        - Track overdue books and send notifications
        - Generate reports on library usage
    2. Data Structures:
        - Books: List of lists (title, author, isbn, is_available, due_date)
        - Members: List of lists (name, member_id, email, borrowed_books_count)
    3. Methods:
        Library:
            - add_book(title, author, isbn)
            - add_member(name, member_id, email)
        Member:
            - checkout_book(isbn, member_id, due_date)
            - return_book(isbn, member_id)
        LibraryManager:
            - get_overdue_books()
            - send_overdue_notifications()
            - generate_library_report()
"""


class Library:
    def __init__(self):
        # Books stored as list of lists: [title, author, isbn, is_available, due_date]
        self.books = [
            ["1984", "George Orwell", "978-0-452-28423-4", True, None],
            [
                "To Kill a Mockingbird",
                "Harper Lee",
                "978-0-06-112008-4",
                False,
                "2024-09-15",
            ],
            [
                "The Great Gatsby",
                "F. Scott Fitzgerald",
                "978-0-7432-7356-5",
                True,
                None,
            ],
            [
                "Pride and Prejudice",
                "Jane Austen",
                "978-0-14-143951-8",
                False,
                "2024-09-10",
            ],
        ]

        # Members stored as list of lists: [name, member_id, email, borrowed_books_count]
        self.members = [
            ["Alice Johnson", "M001", "alice@email.com", 1],
            ["Bob Smith", "M002", "bob@email.com", 1],
            ["Carol Davis", "M003", "carol@email.com", 0],
        ]

    def add_book(self, title, author, isbn):
        self.books.append([title, author, isbn, True, None])

    def add_member(self, name, member_id, email):
        self.members.append([name, member_id, email, 0])

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book[2] == isbn:
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member[1] == member_id:
                return member
        return None

    def checkout_book(self, isbn, member_id, due_date):
        book = self.find_book_by_isbn(isbn)
        member = self.find_member_by_id(member_id)

        if not book:
            return "Book not found"
        if not member:
            return "Member not found"
        if not book[3]:  # is_available
            return "Book is already checked out"
        if member[3] >= 3:  # borrowed_books_count
            return "Member has reached borrowing limit"

        book[3] = False
        book[4] = due_date
        member[3] += 1
        return f"Book '{book[0]}' checked out successfully"

    def return_book(self, isbn, member_id):
        book = self.find_book_by_isbn(isbn)
        member = self.find_member_by_id(member_id)

        if not book:
            return "Book not found"
        if not member:
            return "Member not found"
        if book[3]:  # is_available
            return "Book was not checked out"

        book[3] = True
        book[4] = None
        member[3] -= 1
        return f"Book '{book[0]}' returned successfully"

    def get_overdue_books(self):
        from datetime import datetime

        today = datetime.now().strftime("%Y-%m-%d")

        overdue = []
        for book in self.books:
            if (
                not book[3] and book[4] and book[4] < today
            ):  # not available and has due date
                overdue.append(f"{book[0]} by {book[1]} (Due: {book[4]})")
        return overdue

    def send_overdue_notifications(self):
        overdue_books = self.get_overdue_books()
        notifications_sent = []

        for book_info in overdue_books:
            # Extract book title from the formatted string (hacky!)
            title = book_info.split(" by ")[0]

            # Find which member has this book
            for book in self.books:
                if book[0] == title and not book[3]:
                    # Find member who has this book (very inefficient!)
                    for member in self.members:
                        if member[3] > 0:  # has borrowed books
                            notification = f"Dear {member[0]}, your book '{title}' is overdue. Please return it ASAP."
                            notifications_sent.append(notification)
                            break
                    break

        return notifications_sent

    def generate_library_report(self):
        total_books = len(self.books)
        available_books = sum(1 for book in self.books if book[3])
        checked_out_books = total_books - available_books
        total_members = len(self.members)
        active_members = sum(1 for member in self.members if member[3] > 0)

        report = "=== LIBRARY MANAGEMENT REPORT ===\n"
        report += f"Total Books: {total_books}\n"
        report += f"Available Books: {available_books}\n"
        report += f"Checked Out Books: {checked_out_books}\n"
        report += f"Total Members: {total_members}\n"
        report += f"Active Members: {active_members}\n"
        report += "\nOverdue Books:\n"

        overdue = self.get_overdue_books()
        if overdue:
            for book in overdue:
                report += f"- {book}\n"
        else:
            report += "- None\n"

        return report

    def save_report_to_file(self, filename):
        report = self.generate_library_report()
        with open(filename, "w") as f:
            f.write(report)
        return f"Report saved to {filename}"

    def export_books_to_csv(self, filename):
        import csv

        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Author", "ISBN", "Available", "Due Date"])
            for book in self.books:
                writer.writerow(book)
        return f"Books exported to {filename}"


# Usage
library = Library()
print(library.generate_library_report())
print("\n" + "=" * 40)
print("Overdue notifications:")
for notification in library.send_overdue_notifications():
    print(notification)
