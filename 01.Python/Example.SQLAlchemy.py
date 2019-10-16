from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid

engine = create_engine('mysql+pymysql://tadmin:3417ebb43361@localhost:3306/prototype', echo=True)

Base = declarative_base()


# exit()

class Sentence(Base):
    __tablename__ = 'ExampleTable'  # __tablename__是必须的
    row_id = Column(Integer, primary_key=True)  # 主键是必须的
    text = Column(String)


Session = sessionmaker(bind=engine)

# connect db
session = Session()

for i in range(10, 50):
    uuidText = str(uuid.uuid1())
    row = Sentence(row_id=i, text='%s %s' % (uuidText, i))

    try:
        session.add(row)
        session.commit()

        ## --- DELETE --- ##
        # session.delete(row)
        # Delete By Filter
        # session.query(User).filter(User.id==7).delete()

        ## --- UPDATE --- ##
        # session.query(FooBar).update({"x": 5})

    except Exception as error:
        # IF Error Then Rollback
        session.rollback()
        print(error)
        # continue
else:
    session.close()

## --- SELECT --- ##
print("start select...")

session = Session()

for instance in session.query(Sentence).order_by(Sentence.text):
    target_column = instance.text
    if isinstance(target_column, bytes):
        target_column = target_column.decode("utf-8")

    print(instance.row_id, target_column)

else:
    session.close()
