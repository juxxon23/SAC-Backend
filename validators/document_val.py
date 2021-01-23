from marshmallow import Schema, fields, validate, validates, ValidationError

class DocumentVal(Schema):
    document_u = fields.String(required=True, validate=validate.Length(min=3, max=50))
    content = fields.String(required=True)
    format_id = fields.Integer(required=True)
    competencies_list = fields.List(fields.Integer(), required=True)
    results_list = fields.List(fields.Integer(), required=True)
    
