from extensions import api
from flask_restful import Resource
#import pdb;pdb.set_trace()
print(3)

@api.route('/api/module1')
class moduleApi(Resource):

    def get(self):
        return {'hello': 'world'}