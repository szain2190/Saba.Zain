import sqlite3
conn = sqlite3.connect("Movies.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS movies (
    MovieName TEXT,
    ReleaseDate DATE,
    CopiesSold INT,
    MainActor TEXT
)
""")
conn.commit()
#c.execute("""
#INSERT INTO movies 
#VALUES ("Lord of the Rings", "2010-05-11",100000,"Sam Smith")
#""")
movie_list = [
    ("Harry Potter", "2010-07-13",10000000,"Sam Smith"),
    ("Life of Pi", "2013-06-11",1000000,"Sam Smith"),
    ("Avengers", "2012-04-11",1000000000,"Sam Smith"),
    ("Iron Man", "2010-05-14",1000000,"Robert Downey Jr"),
    ("Spider-man", "2011-05-10",10000000,"Tom Holland")
]
#c.executemany("""
#INSERT INTO movies
#VALUES (?,?,?,?)
#""",movie_list)
conn.commit()
c.execute("""
SELECT MovieName
FROM movies
WHERE MainActor = "Sam Smith"
""")
query = c.fetchall()
print(query)
conn.close()
