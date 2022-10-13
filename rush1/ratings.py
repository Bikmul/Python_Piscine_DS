#!/usr/local/bin/python3

import sys
from collections import Counter
from time import sleep

class Ratings:
    """
    Analyzing data from ratings.csv
    """
    def __init__(self, path_to_the_file):
        self.path = path_to_the_file
        self.usr = self.Users(self.path)
        """
        Put here any fields that you think you will need.
        """      
    # class Movies:    
    #     def dist_by_year(self):
    #         """
    #         The method returns a dict where the keys are years and the values are counts. 
    #         Sort it by years ascendingly. You need to extract years from timestamps.
    #         """
    #         return ratings_by_year
        
    #     def dist_by_rating(self):
    #         """
    #         The method returns a dict where the keys are ratings and the values are counts.
    #      Sort it by ratings ascendingly.
    #         """
    #         return ratings_distribution
        
    #     def top_by_num_of_ratings(self, n):
    #         """
    #         The method returns top-n movies by the number of ratings. 
    #         It is a dict where the keys are movie titles and the values are numbers.
    #  Sort it by numbers descendingly.
    #         """
    #         return top_movies
        
    #     def top_by_ratings(self, n, metric=average):
    #         """
    #         The method returns top-n movies by the average or median of the ratings.
    #         It is a dict where the keys are movie titles and the values are metric values.
    #         Sort it by metric descendingly.
    #         The values should be rounded to 2 decimals.
    #         """
    #         return top_movies
        
    #     def top_controversial(self, n):
    #         """
    #         The method returns top-n movies by the variance of the ratings.
    #         It is a dict where the keys are movie titles and the values are the variances.
    #       Sort it by variance descendingly.
    #         The values should be rounded to 2 decimals.
    #         """
    #         return top_movies

    class Users():
        
        def __init__(self, path):
            self.path = path
        
        def first(self):
            with open (self.path, 'r') as file:
                text = file.read()
            splited = text.split('\n')
            splited_text = []
            for i in splited:
                splited_text.append(i.split(','))
            for i in splited_text:
                
            return(splited_text)
        
        
if __name__ == '__main__':
    if len(sys.argv) == 2: 
        print(Ratings(sys.argv[1]).usr.first())     
  
   
   
   
   
   
    """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
     Inherit from the class Movies. Several methods are similar to the methods from it.
    """
