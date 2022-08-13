#sqlcreatetable.py
import sqlite3

#############DB CONNECTION#############
conn = sqlite3.connect('userscores.db')
c = conn.cursor()

#############GLOBAL VARIABLES FOR EASY CALLING#############
Name = raw_input('Enter your name: ')
Score = 0
#############CREATE DB TABLE IF NOT CREATED ALREADY#############
def create_table():
        c.execute("""CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, totalscore INTEGER);"""
                  )
        
#############REQUESTS THE USERNAME#############
def user_entry():
        c.execute("""INSERT INTO scores VALUES (NULL,?,NULL)""", (Name,)
                  )
        conn.commit()

#############PRINTS THE PLAYER SCORE#############
def read_score():
        c.execute("""SELECT totalscore FROM scores WHERE id = (SELECT max(id) FROM scores);"""
                  )	
        get_score = c.fetchone()
        print max(get_score)

#############PRINTS THE PLAYER NAME#############
def read_name():
        c.execute("""SELECT name FROM scores WHERE name = ?;""", (Name,)
                  )
        get_name = c.fetchone()
        print max(get_name)

#############PRINTS OUT THE LEADERBOARD !> 5#############
def read_topscore():
        c.execute("""SELECT name, totalscore FROM scores ORDER BY totalscore DESC LIMIT 5"""
                  )
        conn.text_factory = str
        topscore = c.fetchall()
        for item in topscore:
                print "".join(str(item)).strip("()").strip(",").decode('utf-8')

#############UPDATES THE USER SCORES#############
def update():
        c.execute("""SELECT totalscore FROM scores"""
                  )
        c.execute("""UPDATE scores SET totalscore = ? + 1 WHERE id = (SELECT max(id) FROM scores)""", (str(Score))
                  )
        conn.commit()

def update_2():
        c.execute("""SELECT totalscore FROM scores"""
                  )
        c.execute("""UPDATE scores SET totalscore = ? + 2 WHERE id = (SELECT max(id) FROM scores)""", (str(Score))
                  )
        conn.commit()

def update_3():
        c.execute("""SELECT totalscore FROM scores"""
                  )
        c.execute("""UPDATE scores SET totalscore = ? + 3 WHERE id = (SELECT max(id) FROM scores)""", (str(Score))
                  )
        conn.commit()

def update_4():
        c.execute("""SELECT totalscore FROM scores"""
                  )
        c.execute("""UPDATE scores SET totalscore = ? + 4 WHERE id = (SELECT max(id) FROM scores)""", (str(Score))
                  )
        conn.commit()

def update_5():
        c.execute("""SELECT totalscore FROM scores"""
                  )
        c.execute("""UPDATE scores SET totalscore = ? + 5 WHERE id = (SELECT max(id) FROM scores)""", (str(Score))
                  )
        conn.commit()
        
        #conn.close()
        
