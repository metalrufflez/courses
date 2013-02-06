/* Question 1
   Add the reviewer Roger Ebert to your database, with an rID of 209. */
insert into Reviewer values(209, 'Roger Ebert');

/* Question 2
   Insert 5-star ratings by James Cameron for all movies in the database.
   Leave the review date as NULL. */
insert into Rating select r.rID, m.mID, '5', NULL from Reviewer r, Movie m
  where r.name = 'James Cameron';

/* Question 3
   For all movies that have an average rating of 4 stars or higher, add 25 
   to the release year. (Update the existing tuples; don't insert new tuples.) */
update Movie set year=year+25 
  where mID in (
    select s.mID from 
      (select mID, avg(stars) avg_stars 
        from Rating 
        group by mID 
        having count(mID) > 1) s 
      where s.avg_stars >= 4);

/* Question 4
   Remove all ratings where the movie's year is before 1970 or after 2000, 
   and the rating is fewer than 4 stars. */
delete from Rating 
  where rID in 
    (select r.rID 
      from Rating r join Movie m on m.mID=r.mID 
      and (m.year<1970 or m.year>2000) 
      and r.stars<4 order by m.mID) 
    and mID in (
      select r.mID 
       from Rating r join Movie m on m.mID=r.mID 
       and (m.year<1970 or m.year>2000) 
       and r.stars<4 order by m.mID) 
    and stars < 4;
