# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def movie5_5(name):
    for a in movies:
        if a['name'] == name:
            if a['imdb'] > 5.5:
                return True
    return False

print(movie5_5("What is the name"))
#2
def movies5_5():
    score = []
    for a in movies:
        if a['imdb'] > 5.5:
            score.append(a['name'])
    return score

print(movies5_5())
#3
def list(category):
    movie = []
    for a in movies:
        if a['category'] == category:
            movie.append(a['name'])
    return movie

print(list('Comedy'))

#4
def average():
    sum = 0
    t = len(movies)
    for a in movies:
        sum += a['imdb']
    return sum/t

print(round(average(), 2))

#5
def categoryaverage(category):
    sum = 0
    for a in movies:
        if a['category'] == category:
            sum += a['imdb']
    return sum/len(list(category))

print(categoryaverage('Comedy'))
