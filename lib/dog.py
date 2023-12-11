from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit

def get_all(session):
    getDogs = session.query(Dog)
    allDogs = getDogs.all()
    return allDogs
    


def find_by_name(session, name):
    dog = session.query(Dog).filter(Dog.name.like(f'%{name}%')).first()
    return dog

def find_by_id(session, id):
    dog = session.query(Dog).filter(Dog.id == id).first()
    return dog

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()