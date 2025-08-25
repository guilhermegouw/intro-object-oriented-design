from typing import List


class Movie:
    def __init__(self, title: str, year: int, rating: float, duration: int):
        self.title = title
        self.year = year
        self.rating = rating
        self.duration = duration

    def get_hours(self) -> int:
        return self.duration // 60

    def get_minutes(self) -> int:
        return self.duration % 60

    def is_longer_than(self, minutes: int) -> bool:
        return self.duration > minutes


class MovieCollection:
    def __init__(self):
        self.movies: List[Movie] = []

    def add_movie(self, title: str, year: int, rating: float, duration: int):
        self.movies.append(Movie(title, year, rating, duration))

    def get_movies_longer_than(self, minutes: int) -> List[Movie]:
        return [movie for movie in self.movies if movie.is_longer_than(minutes)]

    def get_all_movies(self) -> List[Movie]:
        return self.movies.copy()


class MovieReport:
    def get_collection_average_rating(self, collection: MovieCollection) -> float:
        movies = collection.get_all_movies()
        if not movies:
            return 0.0
        total = sum(movie.rating for movie in movies)
        return total / len(movies)

    def get_movie_report(self, movie: Movie) -> str:
        hours = movie.get_hours()
        minutes = movie.get_minutes()
        return f"{movie.title} ({movie.year}) - Rating: {movie.rating}/10, Duration: {hours}h {minutes}m"

    def get_movie_collection_report(self, collection: MovieCollection) -> str:
        report = "=== MOVIE COLLECTION REPORT ===\n"
        for movie in collection.get_all_movies():
            report += self.get_movie_report(movie) + "\n"

        average_rating = self.get_collection_average_rating(collection)
        report += f"\nAverage Rating: {average_rating:.1f}/10"
        return report

    def save_report_to_file(self, collection: MovieCollection, filename: str):
        report = self.get_movie_collection_report(collection)
        with open(filename, "w") as f:
            f.write(report)
