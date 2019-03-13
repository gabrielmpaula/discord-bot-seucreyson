from dotabase import *

session = dotabase_session()

for hero in session.query(Hero):
    print(vars(hero))