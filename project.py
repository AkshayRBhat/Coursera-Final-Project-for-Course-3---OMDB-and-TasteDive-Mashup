#Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

import requests_with_caching
import json
def get_movies_from_tastedive(name):
    dict= {"q": name, "type": "movies", "limit": 5}
    tastedive_response = requests_with_caching.get("https://tastedive.com/api/similar", params=dict)
    py_dic = json.loads(tastedive_response.text)
    print(py_dic)
    return py_dic

#Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.    

def extract_movie_titles():
    title =[]
    movie_n = dic_from_get_movies['Similar']['Results']
    print(movie_n)
    for movie in movie_info:
        title.append(movie['Name'])
    return title

#Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.

def get_related_titles(movie_title):
    print(movie_title)
    new_list =[]
    for title in movie_title:
        getc = get_movies_from_tastedive(title)
        ext = extract_movie_titles(getc)
        for movie in ext:
            if movie not in new_list:
                new_list.append(movie)
    return new_list

#Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.

def get_movie_data(movie_name):
    dict = {'t': movie_name, 'r': 'json'}
    omdbapi_dic = requests_with_caching.get('http://www.omdbapi.com/', params=dict)
    d = json.loads(omdbapi_dic.text)
    return d
    
#Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.


def get_movie_rating(movie_dict):
    if len(movie_dict['Ratings']) > 1:
        if movie_dict['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            rotten_rating = movie_dict['Ratings'][1]['Value'][:2]
            rotten_rating = int(rotten_rating)
    else:
        rotten_rating = 0

    return rotten_rating

#Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

def get_sorted_recommendations(list_of_movies):
    related_movies = get_related_titles(list_of_movies)
    ratings = list()
    sorted_list = list()
    for movie in related_movies:
        a = get_movie_data(movie)
        ratings.append(get_movie_rating(a))

    temp_tuple1 = zip(related_movies, ratings)
    temp_tuple2 = sorted(temp_tuple1, key=getkey, reverse=True)
    print(temp_tuple2)
    for i in range(len(temp_tuple2) - 1):
        if temp_tuple2[i][0] not in sorted_list:
            if temp_tuple2[i][1] == temp_tuple2[i + 1][1]:
                if temp_tuple2[i][0] < temp_tuple2[i + 1][0]:
                    sorted_list.append(temp_tuple2[i + 1][0])
                    sorted_list.append(temp_tuple2[i][0])
            else:
                sorted_list.append(temp_tuple2[i][0])

    print(sorted_list)

    return sorted_list
