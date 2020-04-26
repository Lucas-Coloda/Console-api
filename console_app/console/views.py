from flask import Blueprint, abort, jsonify
from flask_restful import Resource, reqparse
from console_app.console.models import Console
from console_app import api, db

console = Blueprint('console', __name__)

parser = reqparse.RequestParser()
parser.add_argument('id', type = int)
parser.add_argument('name',type=str)
parser.add_argument('year',type=int)
parser.add_argument('price',type=float)
parser.add_argument('active', type = bool)


@console.route("/")
@console.route("/home")
def home():
    return "Catálogo de consoles"

class ConsoleApi(Resource):
    def get(self, id=None, page=1):
        if id == None:
            consoles = Console.query.paginate(page, 5).items
        else:
            consoles = [Console.query.get(id)]
        
        if len(consoles) == 0 or consoles[0] == None:
            return jsonify({})

        res = []
        for console in consoles:
            res.append(console.toJson())
            
        return jsonify(res)

    def post(self):
        args = parser.parse_args()

        console = Console()

        print('\n\n\n\n\n')
        print(args)
        print('\n\n\n\n\n')

        console.selfUpdateFromArgs(args)

        db.session.add(console)
        db.session.commit()

        return jsonify(console.toJson())

    def put(self, id):
        console = Console.query.get(id)

        if not console:
            abort(404)

        args = parser.parse_args()

        console.selfUpdateFromArgs(args)

        db.session.commit()

        return jsonify(console.toJson())
    
    def delete(self, id):
        console = Console.query.get(id)

        if not console:
            abort(404)

        db.session.delete(console)
        db.session.commit()

        return jsonify({'id': id})


api.add_resource(
    ConsoleApi,
    '/api/console/<int:id>',
    '/api/consoles',
    '/api/consoles/<int:page>'
)
