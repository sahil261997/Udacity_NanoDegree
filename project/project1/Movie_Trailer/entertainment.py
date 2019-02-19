import fresh_tomatoes
import media

"""
Class Movie In media with Arguments :
Movie(self , movie_title , movie_story_line ,
      poster_image_url , trailer_youtube_url)"""

# Movie 1.Toy Story :
Toy_Story = media.Movie(
      "Toy Story", "A Story Of a Boy and his toys come alive",
      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Movie 2.Avatar :
Avatar = media.Movie(
      "Avatar", "A marine to a alien planet",
      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Movie 3. Dr.Strange :
Strange = media.Movie(
      "Dr.Strange", "In Doctor Strange, surgeon Strange" +
      " learns the mystic arts after a career-ending car accident.",
      "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",  # NOQA
      "https://www.youtube.com/watch?v=HSzx-zryEgM")


# Movie 4.Need For Speed :
NFS = media.Movie(
      "Need For Speed", " street racer Tobey Marshall," +
      " who sets off to race cross-country, as a way of " +
      " avenging his friend's death at the hands of a rival racer",
      "https://upload.wikimedia.org/wikipedia/en/e/e3/Need_For_Speed_poster.jpg",  # NOQA
      "https://www.youtube.com/watch?v=u3wtVI-aJuw")

# Movie 5.Shawshank Redemption :
Shawshank = media.Movie(
      "Shawshank Redemption",
      "the story of banker Andy Dufresne",
      "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
      "https://www.youtube.com/watch?v=6hB3S9bIaco")

# Movie 6.Home Alone 2 :
Home_Alone = media.Movie(
      "Home Alone 2", "A Boy Lost In New York",
      "https://upload.wikimedia.org/wikipedia/en/5/50/Home_Alone_2.jpg",  # NOQA
      "https://www.youtube.com/watch?v=z_An3W-oO2k")


# movies[] is use list all the movies in a single array :
movies = [Toy_Story, Avatar, Strange, NFS, Shawshank, Home_Alone]

"""
fresh_tomatoes has a Function Named
open_movies_page(), which take the
array as a argument
"""
fresh_tomatoes.open_movies_page(movies)
