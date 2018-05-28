# -*- coding: UTF-8 -*-
"""Stores the building and styling code to generate a web-page."""

import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My Favorite Movies</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="res/bootstrap.min.css">
    <link rel="stylesheet" href="res/bootstrap-theme.min.css">
    <script src="res/jquery-1.10.1.min.js"></script>
    <script src="res/bootstrap.min.js"></script>
    
    <style media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
            background-color:#e7e7e7;
            padding: 2px 4px;
            cursor:pointer;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 12px;
            padding-top: 12px;
        }
        .movie-tile:hover {
            margin-bottom: 11px;
            padding-top: 11px;
            background-color: #EEE;
            border: 1px solid #A9A9A9;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .header-page {
            text-align: center;
            text-decoration: none;
            background-color:#f8f8f8;
            border-color:#e7e7e7;
        }
        .title-page {
            font-weight: 800;
            color: #1e1e1e;
        }
        .storyline {
            color: #3d3d3d;
            padding: 2px 5px;
        }
        .poster-img {
            width: 180px;
            height: 270px;
            cursor: pointer;
        }
    </style>

    <script>
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.poster-img', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''  # NOQA


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">X</a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->



    <div class="container">
    <div class="navbar navbar-fixed-top header-page" role="navigation">
    <h4 class="title-page">My Favorite Movies</h4>
    <h5><a href="https://tinyurl.com/udacity-fsnd" target="_blank">(Movie Trailer Website | Udacity FSND STUDENT PROJECT)</a></h5>
    </div>
    </div>

    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''  # NOQA


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <img class="poster-img" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" src="{poster}" alt="poster image" title="Play Trailer">
    <h4>{title}</h4>
    <h5>{year}</h5>
    <p class="storyline">{storyline}</p>
    <h5 title="visit the movie page on IMDb"><a href="{imdb_page}" target="_blank">IMDb</a></h5>
</div>
'''  # NOQA


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            title=movie.title,
            year=movie.year,
            storyline=movie.storyline,
            imdb_page=movie.imdb_page,
            poster=movie.poster,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
