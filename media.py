# -*- coding: UTF-8 -*-
"""Provide the data structure for movies related informations."""

import webbrowser


class Movie():
    """Construction class for movie related informations.

    Attributes:
        - title (str):        Movie official title.
        - year (str):         Year the movie got released.
        - storyline (str):    Short description of the movie story.
        - poster (str):       Link to movie poster image.
        - trailer (str):      Link to the movie trailer on youtube website.
        - imdb_page (str):    Link to movie full information on IMDb website.
    """

    # Class constructor
    def __init__(self, title, year, storyline, poster, trailer, imdb_page):
        # Instance variables
        self.title = title
        self.year = year
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer
        self.imdb_page = imdb_page

    # Instance methods
    def show_trailer(self):
        """Open the movie trailer in web browser."""
        webbrowser.open(self.trailer)

    def show_poster(self):
        """Open the movie poster image in web browser."""
        webbrowser.open(self.poster)
