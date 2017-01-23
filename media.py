import webbrowser


class Movies():
    #this function initialises the variables
    def __init__(self,movie_title,movie_storyline,movie_trailer,movie_poster):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_url = movie_trailer
        self.poster_url = movie_poster
    #this function opens the web browser to play the trailer    
    def show_trailer(self):
        webbrowser.open(self.trailer_url)