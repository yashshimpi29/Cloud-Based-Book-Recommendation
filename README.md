# Cloud-Based-Book-Recommendation
<p>Link: https://knowyournextbook.herokuapp.com/ </p>
Book Recommendation System using Flask web service and Heroku cloud services.<br>
Major Services Used: Python, Flask, Postgres, Heroku, Git<br>

## Steps involved
<h3> Data Extraction and Cleaning </h3>
<li> Data is extracted from Kaggle and consisted of 50k rows of book dataset.</li>
<li> Data Cleaning involved: 
  <ol> 
    <li>Separating out bookID 
    <li>The original dataset had many book format type. I converted it into 10 types.
    <li>Converting Pages to numeric type
    <li>Cleaning up date column
    <li>Making a list of unique genres
    <li>Working with authors name - removing brackets
  </ol>
</li>
<li> Another important thing was finding the weighted rating for all books so that book have 4.5 rating but only 10 votes is not priortized over a book have 4.1 rating and 1000 votes.
  
<h3> Recommendation Types </h3>
 
<p>First Recommendation I tried and the one that is posted here is based on the description of the book. We use TFIDF Vectorizer to transform the book description and then perform cosine similarity on it.</p>
<p> Another method is to convert the genres into 1-0 binary format and find similar genre books. This technique gave me different results compared to the above </p>
  
<h3> Flask and Database</h3>
<p>
Once the code for recommedation is set, we create a flask app. For testing purpose I used it in localhost.
To avoid spelling mistakes from the user end, I made the use of live search. Some books have same title so made another row in our dataframe of the format "book name by: book author (year)" This dataframe was sent to local postgres and that column the input for the search bar.
</p>


 <h3> Deploying to Heroku </h3>
<p> 
I made the use of Freee Tier Heroku service and that had some limitations on what I could do. Since free tier had limited memory space, I had to get top 10% of the data based on score from the overall data and perform cosine similarity on that. I also made use of heroku postgres for database usage. The database credentials were inserted in the code and the hosted using Git Bash Terminal.
</p>

    
