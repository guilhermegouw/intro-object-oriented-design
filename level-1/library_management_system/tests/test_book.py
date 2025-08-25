import pytest
from freezegun import freeze_time
from library_management_system.book import Book


@pytest.fixture
def the_great_gatsby():
    return Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", True, None)


class TestBook:
    def test_book_initialization(self, the_great_gatsby):
        assert the_great_gatsby.title == "The Great Gatsby"
        assert the_great_gatsby.author == "F. Scott Fitzgerald"
        assert the_great_gatsby.isbn == "9780743273565"
        assert the_great_gatsby.is_available is True
        assert the_great_gatsby.due_date is None

    @freeze_time("2024-09-05")
    def test_book_is_overdue(self, the_great_gatsby):
        assert not the_great_gatsby.is_overdue()
        the_great_gatsby.due_date = "2024-09-01"
        assert the_great_gatsby.is_overdue() is False
