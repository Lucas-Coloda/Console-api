from console_app import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))
    active = db.Column(db.Boolean)
    amount_games = db.Column(db.Integer)

    def __init__(self, id = None, name = None, year = None, price = None, active = None, amount_games = None):
        self.id = id
        self.name = name
        self.year = year
        self.price = price
        self.active = active
        self.amount_games = amount_games

    def selfUpdateFromArgs(self, args):
        self.id = args['id'] if ('id' in args and args['id'] != None) else None
        self.name = args['name']
        self.year = args['year']
        self.price = args['price']
        self.active = args['active']
        self.amount_games = args['amount_games']
    
    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'price': self.price,
            'active': self.active,
            'amount_games': self.amount_games,
        }
    
    def __repr__(self):
        return 'Console {0}'.format(self.id)
