import pytest
from library_management_system.member import Member


class TestMember:
    def test_member_initialization(self):
        member = Member("John Doe", "M001", "john.doe@email.com", 0)
        assert member.name == "John Doe"
        assert member.member_id == "M001"
        assert member.email == "john.doe@email.com"
        assert member.borrowed_books_count == 0
