# metadata_helper.py
import csv

movie_list = []
with open('./imdb.csv') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		movie_list.append(row[0])

'''
# appends the movies to the queries file
with open('./queries.txt', 'a') as f:
	f.writelines([movie + "\n" for movie in movie_list])
'''

print("done")