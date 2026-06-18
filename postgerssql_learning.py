from sqlalchemy import create_engine, Integer, String, text
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped, mapped_column

YOUR_PASSWORD = 'postgres'

# DATABASE CONNECTION
engine = create_engine(f"postgresql+psycopg2://postgres:{YOUR_PASSWORD}@localhost:5432/dds_project")


# BASE CLASS
class Base(DeclarativeBase):
    pass


# TABLE MODEL
class Person(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(Integer, primary_key=True) #gives an integer number to every line in the table ( this general syntax refers to every collum)
    first_name: Mapped[str] = mapped_column(String(50)) #makes a colum for age, suggested into string typr and maxes in 50 charachters
    age: Mapped[int] = mapped_column(Integer) # makes a colum for age, in int type and makes it an integer

# CREATE TABLE (if it doesn't exist)
Base.metadata.create_all(engine)

# ERASE ALL DATA FROM THE TABLE
with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE people RESTART IDENTITY"))
    conn.commit()

# INSERT DATA
with Session(engine) as session:
    mike = Person(first_name="Mike", age=30)
    yoav = Person(first_name="yoav", age=19)

    mike2 = Person(first_name="Mike2", age=30)
    yoav2 = Person(first_name="yoav2", age=91)

    session.add(mike)
    session.add(yoav)
    session.add(yoav2)
    session.add(mike2)

    session.commit()

# READ DATA
# with Session(engine) as session:
#     people = session.query(Person).all()
#
#     for person in people:
#         print(person.id, person.first_name, person.age)
