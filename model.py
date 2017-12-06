import json

import falcon
import predictflightmodel_run


class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        #name = self._image_store.save(req.stream, req.content_type)
        data = json.load(req.stream)
        result = predictflightmodel_run.predictflightmodel(data['plmodel'], data['arr_flights'], data['carrier_ct'], data['weather_ct'], data['nas_ct'])
        data = {'result': result[0] }
        resp.body = json.dumps(data, ensure_ascii=False)
        resp.status = falcon.HTTP_200