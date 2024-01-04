from models import Dog

def create_table(Base,engine):
    Base.metadata.create_all(engine)
    pass
def save(session, dog):
    session.add(dog)
    session.commit()
    pass
def get_all(session):
    query = session.query(Dog).all()
    return query
    pass

def find_by_name(session, name):
    """Return a list of Dogs with the given name"""
    query = session.query(Dog).filter(Dog.name == name).first()
    return query
    

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id) .first()
    return query
    pass
def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.breed == breed ,Dog.name == name ).first()
    return query
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    pass