class Movie():
    """This Class Provides The Way To Store Movie Related Information"""
    def __init__(self, movie_title, movie_story_line,
                 poster_image_url, trailer_youtube_url):
        # In This Function Different Properties Of Movies:
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
