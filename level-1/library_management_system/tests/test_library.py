import pytest
from library_management_system.book import Book
from library_management_system.library import Library
from library_management_system.member import Member


@pytest.fixture
def the_great_gatsby():
    return Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", True, None)


@pytest.fixture
def sample_member():
    return Member("Alice Johnson", "M001", "alice.email.com", 0)


class TestLibrary:
    def test_library_initialization(self):
        library = Library()
        assert library.books == []
        assert library.members == []

    def test_add_book(self, the_great_gatsby):
        library = Library()
        library.add_book(the_great_gatsby)
        assert len(library.books) == 1
        assert library.books[0].title == "The Great Gatsby"

    def test_add_member(self, sample_member):
        library = Library()
        library.add_member(sample_member)
        assert len(library.members) == 1
        assert library.members[0].name == "Alice Johnson"
