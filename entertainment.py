import fresh_tomatoes
import media

#names and description of some movies
toy_story = media.Movies("Toy Story",
                         "A story of a boy and his toys that come to life",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg")

tere_naam = media.Movies("Tere Naam",
                         "The movie is based on a real life incident of a friend of Bala(The Director), who had fallen in love, lost his mind and ended up at a mental asylum.",
                         "https://www.youtube.com/watch?v=brTUorLCY-M",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Tere_Naam_poster.jpg/220px-Tere_Naam_poster.jpg")

run = media.Movies("Run",
                   "A movie Run featuring Abhishek Bachchan, Bhoomika Chawla & Mahesh Manjrekar.",
                   "https://www.youtube.com/watch?v=wOKFxv1bGZo",
                   "https://upload.wikimedia.org/wikipedia/en/9/9e/Run_poster.jpg")

bombay_to_goa = media.Movies("Bombay to Goa",
                             "This is a Hindi film released in 2007. It stars Indian comedians Raju Srivastava, Sunil Pal, and Ahsaan Qureshi and comic actors Vijay Raaz, Asrani and Tinu Anand among others.",
                             "https://www.youtube.com/watch?v=4Iu_Wdyx2ZM",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Bombay_to_Goa_%282007_film%29.jpg/220px-Bombay_to_Goa_%282007_film%29.jpg")

movies = [toy_story,tere_naam,run,bombay_to_goa]

fresh_tomatoes.open_movies_page(movies)