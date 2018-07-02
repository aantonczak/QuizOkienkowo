import sqlite3

def dodajOsobe(nazwa,wynik,kategoria):
    conn = sqlite3.connect('ranking.db')
    c = conn.cursor()
    c.execute("INSERT INTO osoby(nazwa,wynik,kategoria) VALUES ('{}','{}','{}')".format(nazwa,wynik,kategoria))
    conn.commit()
    conn.close()

def pobierzRanking():
    conn = sqlite3.connect('ranking.db')
    c = conn.cursor()
    c.execute("SELECT * FROM osoby GROUP BY nazwa ORDER BY wynik DESC")
    return c.fetchall()
    conn.commit()
    conn.close()

def pobierzKategorie():
    conn = sqlite3.connect('pytania.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type ='table'")
    return c.fetchall()
    conn.commit()
    conn.close()

def pobierzWszystkoZKategorii(Kategoria):
    conn = sqlite3.connect('pytania.db')
    c = conn.cursor()
    c.execute("SELECT * FROM '{}'".format(Kategoria))
    return c.fetchall()
    conn.commit()
    conn.close()

def pobierzPytania(Kategoria):
    conn = sqlite3.connect('pytania.db')
    c = conn.cursor()
    c.execute("SELECT pytanie FROM ('{}')".format(Kategoria) )
    return c.fetchall()
    conn.commit()
    conn.close()

def dodajKategorie(Kategoria):
    conn = sqlite3.connect('pytania.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE '{}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pytanie text NOT NULL,
                odpowiedzA  text NOT NULL,
                odpowiedzB  text NOT NULL,
                odpowiedzC  text NOT NULL,
                odpowiedzD  text NOT NULL,
                poprawnaOdp text NOT NULL
            )""".format(Kategoria))
    conn.commit()
    conn.close()

def dodajPytanie(kategoria,pytanie,A,B,C,D,odp):
    conn = sqlite3.connect('pytania.db')
    c = conn.cursor()
    c.execute("INSERT INTO '{}'(pytanie,odpowiedzA,odpowiedzB,odpowiedzC,odpowiedzD,poprawnaOdp) VALUES ('{}','{}','{}','{}','{}','{}')".format(kategoria,pytanie, A, B, C, D, odp))
    #return c.fetchall()
    conn.commit()
    conn.close()

def usunKategorie(Kategoria):
    conn = sqlite3.connect('pytania.db')
    c = conn.cursor()
    c.execute("DROP TABLE '{}'".format(Kategoria))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    pass