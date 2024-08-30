from bs4 import BeautifulSoup
import requests
import pandas as pd



url="https://www.imdb.com/chart/top/"

##request page source from url
page=requests.get(url)
page

##display page content
page.content
##prints content with new line also

##intiale soup here
soup=BeautifulSoup(page.content,"html.parser")
print(soup.prettify())
#prints the content by removing new lines etc in the form of html formate

##getting the movies or scarpping the movie names
scraped_movies=soup.find_all('td',class_='titleColumn')
scraped_movies

##parse the movie names

movies=[]
for movie in scraped_movies:
    movie=movies.get_text().replace('\n',"")
    movie=movie.strip(" ")
    movies.append(movie)
movies

###get rating for movies
scrap_ratings=soup.find_all('td',class_='ratingColumn imdbRating')
scrap_ratings

###parse the ratings
ratings=[]
for rating in ratings:
    rating=rating.get_text().replace('\n','')
    ratings.append(rating)
ratings


###storing the scarpped dataaaaa
data=pd.DataFrame()
data['Movie Names']=movies
data['Ratings']=ratings
data.head()

##save the dataaa
data.to_json('IMDB TOP MOVIES.json',index=False)
