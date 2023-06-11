from flask import Flask, request
from flask_restx import Api, Resource, fields
from werkzeug.datastructures import FileStorage
from Models.model import data_model
from service import process_file

app = Flask(__name__)
api = Api(app)

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)

#Hardcoded data
data = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"}
]
@api.route('/data')
class DataResource(Resource):
    def get(self):
        return data

    @api.expect(api.model('Data', data_model), validate=True)
    def post(self):
        new_data = request.get_json()
        data.append(new_data)
        return new_data, 201


#fileaccepting code -->
@api.route('/upload')
class UploadResource(Resource):
    @api.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        file = args['file']
        if file.filename.endswith('.xlsx'):
            filename = file.filename
            process_file(file.stream, filename)
            return {'message': 'File processed and added to data.'}, 201
        else:
            return {'message': 'Invalid file format. Please upload an Excel file (.xlsx).'}, 400

if __name__ == '__main__':
    app.run(debug=True)




##explanation
## below code can be written in another file but if i do that than i need to run botht the files separetly so run the swagger and than swagger and api will rujn so it is better to put this code in this same file

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Swagger API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
