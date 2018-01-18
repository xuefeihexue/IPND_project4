#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser


# Crete a Movie class

class Movie:

    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube,
        ):
        ''' When a initial function is called, it will create a new space for the movie object.
        The arugments are assigned to the corresponding instance variables:
        Args:
            movie_title(str): hold the title of movie
            movie_storyline(str): hold the plot of movie
            poster_image:(str): hold the url link to poster of movie
            trailer_youtube(str): hold the url link to the youtube of movie
        Returns:
            returns an object of movie with four attributs as the same as input arguments.
        '''

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showtrailer(self):
        # This fuchtion shows the trailer of the movie instance

        webbrowser.open(self.trailer_url)
            # use the webbrowser.open function to open the browser with the link as input
