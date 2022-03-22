from . import db


class Property(db.Model):

    __tablename__ = 'property'

    id = db.Column(db.String, primary_key=True, autoincrement= True)
    title = db.Column(db.String(80))
    description= db.Column(db.String(255))
    num_bedrooms = db.Column(db.String(5))
    num_bathrooms = db.Column(db.String(5))
    price = db.Column(db.String(15))
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(80))
   

    def __init__(self, title, description, num_bedrooms, num_bathrooms, price, property_type, location, photo):
        self.title = title
        self.description= description
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo
             

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support


    def __repr__(self):
        return '<Property %r>' % (self.title)
