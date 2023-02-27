import spacy
nlp = spacy.load('en_core_web_md')

# makes a dictionary with movie title as key and movie plot as value
with open("movies.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    movies = {}
    for line in content:
        line = line.strip("\n").split(":")
        movies[line[0]] = line[1]

# makes 2 lists, 1 for dictionary keys and 1 for dictionary values. This will be used to get movie name from movie plot.
movies_name = list(movies.keys())
movies_plot = list(movies.values())

movie_to_compare = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati
trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk 
land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# keeps track of which plot has highest similarity to above movie plot
max_similarity = 0
best_match = ""
model_movie = nlp(movie_to_compare)

# for loop checks each movie plot against the hulk one and finds similarity. If similarity is higher than previous movie
# then max_similarity is updated and movie plot is stored in variable best_match
for movie_plot in movies_plot:
    similarity = nlp(movie_plot).similarity(model_movie)
    if similarity > max_similarity:
        max_similarity = similarity
        best_match = movie_plot

# This is to test code is working. Outputs final values for max_similarity and closest movie plot
print(max_similarity)
print(best_match)

# Index value of movie plot is same as index value of movie name. Prints out movie name key matching chosen movie plot
position = movies_plot.index(best_match)
print(f"The next movie to watch is {movies_name[position]}")



