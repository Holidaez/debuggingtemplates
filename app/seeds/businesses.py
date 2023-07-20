from app.models import db, Business
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_businesses():
    buis1 = Business(
        name="Chuck E Cheese",
        category="American",
        desc="Chuck E. Cheese is a delightful and entertaining family-oriented restaurant and entertainment center that stands as a beacon of joy and amusement for people of all ages. Named after its charming and lovable mascot, Chuck E. Cheese, the establishment is an absolute treasure trove of fun and excitement, offering an array of activities and attractions that are sure to leave visitors both young and old with unforgettable memories.",
        owner_id=1
    )
    buis2 = Business(
        name="Monterreys",
        category="Mexican",
        desc="A diverse menu that includes a variety of traditional dishes from Mexico",
        owner_id=1
    )
    db.session.add(buis1)
    db.session.add(buis2)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_businesses():

    db.session.execute(text("DELETE FROM businesses"))

    db.session.commit()
