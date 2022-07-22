# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES
# HW1 Movie Recommendation System
# GeonJae Baek 212008626


# WHEN DONE, SUBMIT THIS FILE TO CANVAS

import math
from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    movieratings = {}
    
    with open(f, 'r') as file:
        for line in file:
            # movie, rating, and user
            movie, rating, user = line.split("|")
            rating = float(rating)
            movieratings[movie] = movieratings.get(movie, []) + [rating]
            
    return movieratings

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    movies = {}
    
    with open(f, 'r') as file:
        for line in file:
            # genre, id, and movie title
            genre, _id, movie = line.split("|")
            movie = movie.strip('\n')
            movies[movie] = genre
            
    return movies
            

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    genre_to_movie = {}
    
    for genre in d.keys():
        key = d[genre]
        if not key in genre_to_movie.keys():
            genre_to_movie[key] = []
        genre_to_movie[key].append(genre)
        
    return genre_to_movie
    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    ave = {}
    
    for key in d.keys():
        rating_avg = sum(d[key])/len(d[key])
        ave[key] = rating_avg
        
    return ave
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    
    popular_movies = sorted(d.items(), key = lambda x:x[1], reverse=True)
    
    return dict(popular_movies[:n])
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    filters = {}
    
    for movie, f_rating in d.items():
        if f_rating >= thres_rating:
            filters[movie] = f_rating
            
    return filters
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    popular_in_genre = []
    movies = genre_to_movies[genre]
    
    for movie, rating in movie_to_average_rating.items():
        if movie in movies:
            popular_in_genre.append((movie, rating))
    popular_in_genre = sorted(popular_in_genre, key = lambda x:x[1], reverse=True)
    
    return dict(popular_in_genre[:n])
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    ratings = []
    movies = genre_to_movies[genre]
    
    for movie, rating in movie_to_average_rating.items():
        if movie in movies:
            ratings.append(rating)
    genre_rating = sum(ratings) / len(ratings)
    
    return genre_rating
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    gen_popularity = []
    
    for genre in genre_to_movies:
        rating = get_genre_rating(genre, genre_to_movies, movie_to_average_rating)
        gen_popularity.append((genre, rating))
    gen_popularity = sorted(gen_popularity, key = lambda x:x[1], reverse=True)
    
    return dict(gen_popularity[:n])

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to movies and ratings
    # WRITE YOUR CODE BELOW
    user_ratings = {}
    
    for line in open(f):
        movie, rating, user_id = line.split('|')
        movie_name_ratings = (movie, rating)
        user_id = int(user_id)
        if rating in user_ratings:
            user_ratings[user_id].append(movie_name_ratings)
        else:
            user_ratings[user_id] = [movie_name_ratings]
            
    return user_ratings
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    user_genre = {}
    user_id = int(user_id)
    top_genre = ""
    highest_rating = 0
    sum_of_ratings = 0.0
    
    for tuples in user_to_movies[user_id]:
        movie_name = tuples[0]
        rating = tuples[1]
        genre = movie_to_genre[movie_name]
        if genre in user_genre:
            user_genre[genre].append(rating)
        else:
            user_genre[genre] = [rating]
            
    for genre, ratings_list in user_genre.items():

        for i in ratings_list:
            sum_of_ratings = sum_of_ratings + float(i)
            average_ratings = sum_of_ratings / len(ratings_list)
            if average_ratings > highest_rating:
                highest_rating = average_ratings
                top_genre = genre
                
    return top_genre
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    user_id = int(user_id)
    movies = user_to_movies[user_id]
    movie_names = []
    user_genre_rating = {}
    user_genre_avg_rating = {}
    movie_top_genre_rating = []
    recommendationsys = {}
    
    for mv in movies:
        movie_names.append(mv[0])
        genre = movie_to_genre[mv[0]]
        rating = mv[1]
        
        if genre not in user_genre_rating:
            user_genre_rating[genre] = [rating, 1]
        else:
            user_genre_rating[genre][0] += rating
            user_genre_rating[genre][1] += 1
       
    for gr, rt in user_genre_rating.items():
        a = []
        
        for i in rt:
            i = float(i)
            a.append(i)
        user_genre_avg_rating[gr] = a[0]/a[1]
        
    top_genre = max(user_genre_avg_rating, key = user_genre_avg_rating.get)
    
    for mv, gr in movie_to_genre.items():
        if (gr == top_genre) and (mv not in movie_names):
            movie_top_genre_rating.append((mv, movie_to_average_rating[mv]))
    movie_top_genre_rating.sort(key = lambda x:x[1])
    
    top_movie = movie_top_genre_rating
    
    if len(top_movie) >= 1:
        recommendationsys [top_movie[0][0]] = top_movie[0][1]
    if len(top_movie) >= 2:
        recommendationsys [top_movie[1][0]] = top_movie[1][1]
    elif len(top_movie) >= 3:
        recommendationsys [top_movie[2][0]] = top_movie[2][1]
        
    return recommendationsys