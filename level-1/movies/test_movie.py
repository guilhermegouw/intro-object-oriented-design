import pytest
from movies.movie import Movie, MovieCollection, MovieReport


@pytest.fixture
def inception():
    return Movie("Inception", 2010, 8.8, 148)


@pytest.fixture
def movie_collection():
    collection = MovieCollection()
    collection.add_movie("The Matrix", 1999, 8.7, 136)
    collection.add_movie("Inception", 2010, 8.8, 148)
    collection.add_movie("Parasite", 2019, 8.5, 132)
    return collection


class TestMovie:
    def test_movie_initialization(self, inception):
        assert inception.title == "Inception"
        assert inception.year == 2010
        assert inception.rating == 8.8
        assert inception.duration == 148

    def test_movie_get_hours(self, inception):
        assert inception.get_hours() == 2

    def test_movie_get_minutes(self, inception):
        assert inception.get_minutes() == 28


class TestMovieReport:
    def test_get_movie_report(self, inception):
        report = MovieReport().get_movie_report(inception)
        expected_report = "Inception (2010) - Rating: 8.8/10, Duration: 2h 28m"
        assert report == expected_report

    def test_get_collection_report(self, movie_collection):
        expected_report = (
            "=== MOVIE COLLECTION REPORT ===\n"
            "The Matrix (1999) - Rating: 8.7/10, Duration: 2h 16m\n"
            "Inception (2010) - Rating: 8.8/10, Duration: 2h 28m\n"
            "Parasite (2019) - Rating: 8.5/10, Duration: 2h 12m\n"
            "\nAverage Rating: 8.7/10"
        )
        report = MovieReport().get_movie_collection_report(movie_collection)
        assert report == expected_report

    def test_get_collection_average_rating(self, movie_collection):
        avg_rating = MovieReport().get_collection_average_rating(movie_collection)
        assert avg_rating == pytest.approx(8.666666666666666, 0.01)
