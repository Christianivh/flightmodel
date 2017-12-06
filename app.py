import falcon

from .model import Resource


api = application = falcon.API()

model = Resource()
api.add_route('/flightmodel', model)