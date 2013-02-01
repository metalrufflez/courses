/* Question 1
   Find the titles of all movies directed by Steven Spielberg. */
select title from Movie where director='Steven Spielberg';

/* Question 2
   Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. */
select year from Movie where mID in (select mID from Rating where stars>=4) order by year;

/* Question 3
   Find the titles of all movies that have no ratings. */
select title from Movie where mID not in (select mID from Rating where stars>=1);

/* Question 4
   Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date. */
select name from Reviewer where rID in (select rID from Rating where ratingDate is null);

/* Question 5
   Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. */
select r.name, m.title, rt.stars, rt.ratingDate from Reviewer r, Movie m, Rating rt where r.rID = rt.rID and m.mID = rt.mID order by r.name,m.title,rt.stars;

/* Question 6
   For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name and the title of the movie. */
select r.name, m.title from Rating r1, Rating r2, Reviewer r, Movie m where r1.rID=r2.rID and r1.mID = r2.mID and r1.stars>r2.stars and r1.mID=m.mID and r1.rID=r.rID and r1.RatingDate>r2.RatingDate;

/* Question 7
   For each movie that has at least one rating, find the highest number of stars that movie received. Return the movie title and number of stars. Sort by movie title. */
select m.title, r.stars from Movie m join (select mID, max(stars) stars from Rating group by mID) as r on r.mID=m.mID order by m.title;

/* Question 8
   List movie titles and average ratings, from highest-rated to lowest-rated. If two or more movies have the same average rating, list them in alphabetical order. */
select m.title, avg(r.stars) from Rating r join Movie m on r.mID=m.mID group by r.mID order by avg(r.stars) desc,m.title;

/* Question 9
   Find the names of all reviewers who have contributed three or more ratings. (As an extra challenge, try writing the query without HAVING or without COUNT.) */
select rw.name from Reviewer rw join (select r.rID, count(r.rID) as count from Rating r, Reviewer rw where r.rID=rw.rID group by r.rID) s on s.rID=rw.rID and s.count>=3;
