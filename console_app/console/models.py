from console_app import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))
    active = db.Column(db.Boolean)

    def __init__(self, id = None, name = None, year = None, price = None, active = None):
        self.id = id
        self.name = name
        self.year = year
        self.price = price
        self.active = active

    def selfUpdateFromArgs(self, args):
        self.id = args['id'] if ('id' in args and args['id'] != None) else None
        self.name = args['name']
        self.year = args['year']
        self.price = args['price']
        self.active = args['active']
    
    def toJson(self):
        return {
            self.id: {
                'name': self.name,
                'year': self.year,
                'price': self.price,
                'active': self.active,
            }
        }
    
    def __repr__(self):
        return 'Console {0}'.format(self.id)
