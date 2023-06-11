from flask_restx import fields

data_model = {
    'id': fields.Integer(required=True, description='ID of the data'),
    'name': fields.String(required=True, description='Name of the data')
}
