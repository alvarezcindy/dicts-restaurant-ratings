import sys


def list_restaurant_ratings(filename):
    """Reads restaurant names and ratings from file, adds to dictionary,
        returns in alpha order

    """

    with open(filename) as text:

        rest_ratings = {}

        for line in text:
            restaurant, rating = line.rstrip().split(":")
            rest_ratings[restaurant] = rating

        for restaurant, rating in sorted(rest_ratings.items()):
            print(f'{restaurant} is rated at {rating}.')


list_restaurant_ratings(sys.argv[1])
