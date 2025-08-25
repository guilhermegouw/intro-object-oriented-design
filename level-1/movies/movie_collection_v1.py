"""
Scenario: You have a class that manages a movie collection, but it's doing too
many things.
"""


class MovieCollection:
    def __init__(self):
        # Movies stored as list of lists: [title, year, rating, duration_minutes]
        self.movies = [
            ["The Matrix", 1999, 8.7, 136],
            ["Inception", 2010, 8.8, 148],
            ["Parasite", 2019, 8.5, 132],
        ]

    def add_movie(self, title, year, rating, duration):
        self.movies.append([title, year, rating, duration])

    def get_average_rating(self):
        total = sum(movie[2] for movie in self.movies)
        return total / len(self.movies)

    def get_movies_longer_than(self, minutes):
        return [movie for movie in self.movies if movie[3] > minutes]

    def format_movie_report(self):
        report = "=== MOVIE COLLECTION REPORT ===\n"
        for movie in self.movies:
            hours = movie[3] // 60
            mins = movie[3] % 60
            report += f"{movie[0]} ({movie[1]}) - Rating: {movie[2]}/10, Duration: {hours}h {mins}m\n"
        report += f"\nAverage Rating: {self.get_average_rating():.1f}/10"
        return report

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.format_movie_report())


# Usage
collection = MovieCollection()
print(collection.format_movie_report())
