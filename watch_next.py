import spacy
nlp = spacy.load('en_core_web_md')

def watch_next(watched_movie_description, text_file):
    '''
    Returns movie name after comparing movie description provided against movie descriptions in text file
    param watched_movie_description: variable containing description of movie watched already
    :param text_file: text file containing movie names and descriptions from which function chooses most similar
    :return: movie name from text file
    '''
    # Opens text file and creates 2 lists, 1 of movie names and 1 of movie descriptions
    with open(text_file, "r", encoding="utf-8") as f:
        content = f.readlines()
        movie_names = []
        movie_descriptions = []
        for line in content:
            line = line.strip("\n").split(":")
            movie_names.append(line[0])
            movie_descriptions.append(line[1])
   # counter keeps track of which movie description most similar to already watched one
    max_similarity = 0
    best_match = ""
    watched_movie_description = nlp(watched_movie_description)
    # for loop checks each movie plot against the hulk one and finds similarity. If similarity is higher than previous movie
    # then max_similarity is updated and movie plot is stored in variable best_match
    for i in movie_descriptions:
        similarity = nlp(i).similarity(watched_movie_description)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = i
    #
    position = movie_descriptions.index(best_match)
    return movie_names[position]


text_file = "movies.txt"
watched_movie_description = '''
Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into
a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet
Sakaar where he is sold into slavery and trained as a gladiator.'''


print(f'The next movie to watch is {watch_next(watched_movie_description, "movies.txt")}')



