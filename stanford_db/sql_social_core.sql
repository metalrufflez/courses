/* Question 1
   Find the names of all students who are friends with someone named Gabriel. */
select hs.name
  from Highschooler hs join Friend f
  on (hs.ID=f.ID1 and f.ID2 in
    (select ID
      from Highschooler
      where name = 'Gabriel'))
     or (hs.ID=f.ID2 and f.ID1 in
      (select ID from
        Highschooler
        where name = 'Gabriel'))
    group by hs.name;

/* Question 2
   For every student who likes someone 2 or more grades younger than themselves,
   return that student's name and grade, and the name and grade of the student
   they like. */
select hs.name, hs.grade, hs2.name, hs2.grade
  from Highschooler hs, Highschooler hs2, Likes l
  where ((hs.id=l.id1
      and hs2.id=l.id2
      and (hs.grade-hs2.grade)>=2));

/* Question 3
   For every pair of students who both like each other, return the name and
   grade of both students. Include each pair only once, with the two names
   in alphabetical order. */
select hs1.name, hs1.grade, hs2.name, hs2.grade
  from Likes l1, Likes l2, Highschooler hs1, Highschooler hs2
  where l1.id1 = l2.id2
   and l1.id2 = l2.id1
   and hs1.id=l1.id1
   and hs2.id=l1.id2
   and hs1.name < hs2.name;

/* Question 4
   Find names and grades of students who only have friends in the same grade.
   Return the result sorted by grade, then by name within each grade. */
select name, grade
  from Highschooler
  where id not in
    (select hs1.id
      from Highschooler hs1, Highschooler hs2, Friend f1
      where hs1.id=f1.id1 and hs2.id=f1.id2 and hs1.grade!=hs2.grade)
  order by grade, name;

/* Question 5
   Find the name and grade of all students who are liked by more than one other
   student. */
select hs.name, hs.grade
  from (select l1.id2 as id, count(l1.id2) as count
    from Likes l1 group by l1.id2) s
  join Highschooler hs
  where s.count > 1 and hs.id=s.id;
