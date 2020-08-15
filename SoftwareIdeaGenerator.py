from random import randrange

print('-- Idea Generator --')
l = ['Python', 'Java', 'JavaScript', 'PHP', 'C#']
t = ['diet', 'finance', 'workout', 'art', 'music', 'news', 'sports', 'movies', 'books', 'travel', 'hobbies', 'children', 'restaurants', 'trends', ' learning', 'games', 'accomplishments', 'coffee', 'alien']
k = ['game', 'calculator', 'AI', 'utility', 'graphic']
p = ['desktop', 'android', 'web', 'server side']

amount = input('How Many Ideas Should I Generate?: ')

for i in range(int(amount)):
    language = l[randrange(len(l))]
    topic = t[randrange(len(t))]
    kind = k[randrange(len(k))]
    platform = p[randrange(len(p))]
    print('A {} {} written in {} as a {} app.'.format(topic, kind, language, platform))
