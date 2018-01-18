import media
import fresh_tomatoes

shawshank=media.Movie("The Shawshank Redemption",
                "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                "https://images-na.ssl-images-amazon.com/images/I/519NBNHX5BL._SY445_.jpg",
                "https://youtu.be/6hB3S9bIaco")

goldfather=media.Movie("The Godfather",
                "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                "http://c300221.r21.cf1.rackcdn.com/the-goldfather-1345496165_org.jpg",
                "https://youtu.be/1aV9X2d-f5g")

darknight=media.Movie("The Dark Knight",
                "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                "http://is1.mzstatic.com/image/thumb/Video128/v4/e9/61/d3/e961d39d-f8d8-6b3b-3a2e-dc0432c2fbf4/source/1200x630bb.jpg",
                "https://youtu.be/AASZJ_KtVWM")

angryman=media.Movie("12 Angry Men",
                "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.",
                "http://www.filmsite.org/posters/twelveangrymen.jpg",
                "https://youtu.be/Dosg0p7LAB4")

movie=[shawshank,goldfather,darknight,angryman]

# Using fresh_tomatoes.py to create a HTML link and display all the movie posters and titles, if click the poster, a youtue trailer will display
fresh_tomatoes.open_movies_page(movie)
