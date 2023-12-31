num_people = int(input())
genres = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]
genre_counts = {genre: 0 for genre in genres}

for i in range(num_people):
    name, *fav_genres = input().split()
    for genre in fav_genres:
        genre_counts[genre] += 1

for genre, count in sorted(genre_counts.items(), key=lambda x: (-x[1], x[0])):
    print(f"{genre} : {count}")
