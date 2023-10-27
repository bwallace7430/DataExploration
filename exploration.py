import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from pandas import read_csv

pd.set_option('display.float_format', '{:.2f}'.format)

imdb_movies_data = read_csv("imdb_movies.csv")
imdb_movies_data = imdb_movies_data[(imdb_movies_data['score'] != 0 ) & (imdb_movies_data['budget_x'] != 0) & (imdb_movies_data['revenue'] != 0)]
imdb_movies_data = imdb_movies_data[(imdb_movies_data['score'] != 1 ) & (imdb_movies_data['budget_x'] != 1) & (imdb_movies_data['revenue'] != 1)]
print(imdb_movies_data.describe())

movies_data = read_csv("movies.csv")
movies_data = movies_data[(movies_data['score'] != 0 ) & (movies_data['year'] != 0) & (movies_data['votes'] != 0) & (movies_data['budget'] != 0) & (movies_data['gross'] != 0) & (movies_data['runtime'] != 0)]
movies_data = movies_data[(movies_data['score'] != 1 ) & (movies_data['year'] != 1) & (movies_data['votes'] != 1) & (movies_data['budget'] != 1) & (movies_data['gross'] != 1) & (movies_data['runtime'] != 1)]
print(movies_data.describe())

def create_histogram(data_feature, title, x_label, y_label):
    plt.hist(data_feature, bins=60, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()

# create_histogram(imdb_movies_data['score'], 'IMDB Scores', 'Scores', 'Frequency')
# create_histogram(imdb_movies_data['budget_x'], 'Movie Budget', 'Dollars Spent', 'Frequency')
# create_histogram(imdb_movies_data['revenue'], 'Movie Revenue', 'Dollars Earned', 'Frequency')

# create_histogram(movies_data['year'], 'Release Year', 'Year', 'Frequency')
# create_histogram(movies_data['score'], 'Movie Scores', 'Score', 'Frequency')
# create_histogram(movies_data['votes'], 'Number of Reviews', 'Amount of Votes', 'Frequency')
# create_histogram(movies_data['budget'], 'Movie Budget', 'Dollars Spent', 'Frequency')
# create_histogram(movies_data['gross'], 'Gross Earned', 'Dollars Earned', 'Frequency')
# create_histogram(movies_data['runtime'], 'Movie Runtime', 'Length in Minutes', 'Frequency')

def create_boxplot(data_feature, title, x_label):
    sns.boxplot(data = data_feature, x = x_label)
    plt.show()

# create_boxplot(imdb_movies_data, 'IMDB Scores', 'score')
# create_boxplot(imdb_movies_data, 'Movie Budget', 'budget_x')
# create_boxplot(imdb_movies_data, 'Movie Revenue', 'revenue')

# create_boxplot(movies_data, 'Release Year', 'year')
# create_boxplot(movies_data, 'Movie Scores', 'score')
# create_boxplot(movies_data, 'Number of Reviews', 'votes')
# create_boxplot(movies_data, 'Movie Budget', 'budget')
# create_boxplot(movies_data, 'Gross Earned', 'gross')
# create_boxplot(movies_data, 'Movie Runtime', 'runtime')

def create_scatterplot(x, y, title, x_label, y_label):
    plt.scatter(x, y, label=title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()

create_scatterplot(imdb_movies_data['budget_x'], imdb_movies_data['score'], "IMDB Scores Given Budget", "Dollars Spent", "Score Recieved")
create_scatterplot(imdb_movies_data['revenue'], imdb_movies_data['score'], "IMDB Scores Given Revenue", "Dollars Earned", "Score Recieved")
create_scatterplot(movies_data['year'], movies_data['score'], "Scores Given Year Released", "Year Released", "Score Recieved")
create_scatterplot(movies_data['votes'], movies_data['score'], "Scores Given Number of Votes", "Votes Recieved", "Score Recieved")
create_scatterplot(movies_data['budget'], movies_data['score'], "Scores Given Budget", "Dollars Spent", "Score Recieved")
create_scatterplot(movies_data['gross'], movies_data['score'], "Scores Given Gross", "Dollars Earned", "Score Recieved")
create_scatterplot(movies_data['runtime'], movies_data['score'], "Scores Given Runtime", "Length in Minutes", "Score Recieved")