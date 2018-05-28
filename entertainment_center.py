# -*- coding: UTF-8 -*-
"""Stores the movies informations and feed that to the building file."""

import media
import fresh_tomatoes


# Instances of the Movie class, holding the information of my favorite movies
# Class data structure: title, year, storyline, poster, trailer, imdb_page
godfather = media.Movie(
    "The Godfather",
    "1972",
    "The aging patriarch of an organized crime dynasty transfers control of "
    "his clandestine empire to his reluctant son.",
    "https://tinyurl.com/MOVIE-Godfather",
    "https://youtu.be/sY1S34973zA",
    "https://www.imdb.com/title/tt0068646/")

shawshank = media.Movie(
    "The Shawshank Redemption",
    "1994",
    "Two imprisoned men bond over a number of years, finding solace and "
    "eventual redemption through acts of common decency.",
    "https://tinyurl.com/MOVIE-Shawshank",
    "https://youtu.be/6hB3S9bIaco",
    "https://www.imdb.com/title/tt0111161/")

beautiful_mind = media.Movie(
    "A Beautiful Mind",
    "2001",
    "After John Nash, a brilliant but asocial mathematician, accepts secret "
    "work in cryptography, his life takes a turn for the nightmarish.",
    "https://tinyurl.com/MOVIE-A-Beautiful-Mind",
    "https://youtu.be/aS_d0Ayjw4o",
    "https://www.imdb.com/title/tt0268978/")

catch_me = media.Movie(
    "Catch Me If You Can",
    "2002",
    "A brilliant young master of deception and the FBI agent hot on his trail"
    " Based on real life story of Frank Abagnale",
    "https://tinyurl.com/MOVIE-Catch-Me-If-You-Can",
    "https://youtu.be/71rDQ7z4eFg",
    "https://www.imdb.com/title/tt0264464/")

italian_job = media.Movie(
    "The Italian Job",
    "2003",
    "After being betrayed and left for dead in Italy, Charlie Croker and "
    "his team plan an elaborate gold heist against their former ally.",
    "https://tinyurl.com/MOVIE-TheItalianJob",
    "https://youtu.be/5Eyw-Qiwpj0",
    "https://www.imdb.com/title/tt0317740/")

robot = media.Movie(
    "I, Robot",
    "2004",
    "A technophobic cop investigates a crime that may have been perpetrated "
    "by a robot, which leads to a larger threat to humanity.",
    "https://tinyurl.com/MOVIE-I-Robot",
    "https://youtu.be/rL6RRIOZyCM",
    "https://www.imdb.com/title/tt0343818/")

kingdom_of_heaven = media.Movie(
    "Kingdom of Heaven",
    "2005",
    "Balian of Ibelin travels to Jerusalem during the Crusades of the "
    "12th century, and there he finds himself as the defender of the "
    "city and its people.",
    "https://tinyurl.com/MOVIE-Kingdom-of-Heaven",
    "https://youtu.be/moNH4N44D28",
    "https://www.imdb.com/title/tt0320661/")

inception = media.Movie(
    "Inception",
    "2010",
    "A thief, who steals corporate secrets through the use of dream-sharing "
    "technology, is given the inverse task of planting an idea into "
    "the mind of a CEO.",
    "https://tinyurl.com/MOVIE-IMG-Inception",
    "https://youtu.be/8hP9D6kZseM",
    "https://www.imdb.com/title/tt1375666/")

gladiator = media.Movie(
    "Gladiator",
    "2000",
    "When a Roman General is betrayed, and his family murdered by an "
    "emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
    "https://tinyurl.com/MOVIE-Gladiator",
    "https://youtu.be/0BLZbrLogTo",
    "https://www.imdb.com/title/tt0172495/")

heat = media.Movie(
    "Heat",
    "1995",
    "A group of professional bank robbers start to feel the heat from police.",
    "https://tinyurl.com/MOVIE-IMG-Heat",
    "https://youtu.be/3UB16UIpgjI",
    "https://www.imdb.com/title/tt0113277/")

Oceans_eleven = media.Movie(
    "Ocean's Eleven",
    "2001",
    "Danny Ocean and his eleven accomplices plan to rob three Las Vegas "
    "casinos simultaneously.",
    "https://tinyurl.com/MOVIE-Oceans-Eleven",
    "https://youtu.be/imm6OR605UI",
    "https://www.imdb.com/title/tt0240772/")

the_bank_job = media.Movie(
    "The Bank Job",
    "2008",
    "A car dealer with a dodgy past and new family, recognizes the "
    "opportunity of a lifetime only to fall into a deadly web of corruption "
    "and illicit scandal. ",
    "https://tinyurl.com/MOVIE-The-Bank-Job",
    "https://youtu.be/gjmE6SUjsDg",
    "https://www.imdb.com/title/tt0200465/")

dragon = media.Movie(
    "How to Train Your Dragon",
    "2010",
    "A hapless young Viking who aspires to hunt dragons becomes the "
    "unlikely friend of a young dragon himself, and learns there may be "
    "more to the creatures than he assumed.",
    "https://tinyurl.com/MOVIE-How-to-Train-Your-Dragon",
    "https://youtu.be/HqMYHjlBMUY",
    "https://www.imdb.com/title/tt0892769/")

# List of the movies to be included in the generated web page
movies = [
        godfather,
        shawshank,
        beautiful_mind,
        catch_me, italian_job,
        robot,
        kingdom_of_heaven,
        inception,
        gladiator,
        heat,
        Oceans_eleven,
        the_bank_job,
        dragon]

# Generate a web page displaying the movies in the list
# using the building and styling file "fresh_tomatoes.py".
fresh_tomatoes.open_movies_page(movies)
