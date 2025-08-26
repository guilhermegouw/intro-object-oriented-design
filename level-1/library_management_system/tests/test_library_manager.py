import pytest
from library_management_system.library import Library
from library_management_system.library_manager import LibraryManager


@pytest.fixture
def library():
    library = Library()
    library.add_book("1984", "George Orwell", "978-0-452-28423-4")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
    library.add_member("Alice Johnson", "M001", "alice@email.com")
    library.add_member("Bob Smith", "M002", "bob@email.com")
    return library


class TestLibraryManager:
    def test_library_manager_initialization(self):
        manager = LibraryManager()
        assert manager.library is not None

    def test_libary_manager_checkout_book(self, library):
        manager = LibraryManager(library)
        manager.checkout_book("978-0-452-28423-4", "M001", "2024-09-20")
        book = manager.library.find_book_by_isbn("978-0-452-28423-4")
        assert book.is_available is False
        assert book.due_date == "2024-09-20"
        member = manager.library.find_member_by_id("M001")
        assert member.borrowed_books_count == 1
        assert "978-0-452-28423-4" in member.borrowed_books
        assert "2024-09-20" in member.due_dates
