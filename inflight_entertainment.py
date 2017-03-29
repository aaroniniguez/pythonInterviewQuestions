#flight_length = 200
#movie_lengths = [100,120]
import itertools
def get_movie(flight_length, movie_lengths):
   MovieLists = list(itertools.permutations(movie_lengths, 2))
   for i in MovieLists:
        sum = 0
        for p in i:
           sum +=p 
        if sum == flight_length:
            return True
   return False
def getFlightInfo(fileInfo):
    f = open(fileInfo, "r")
    for line in f:
        if line == "```\n":
            print "```"
        else:
            line = line.replace("\n", "")
            flight_length = int(line.split(" ")[0])
            movie_lengths = line.split(" ")[1].split(",")
            movie_lengths = map(int,movie_lengths)
            print get_movie(flight_length, movie_lengths)
getFlightInfo("inflight_entertainment.txt")
