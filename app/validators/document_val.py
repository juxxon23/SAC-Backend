from marshmallow import Schema, fields, validate, validates, ValidationError

class DocumentVal(Schema):
    id_u = fields.String(required=True, validate=validate.Length(min=3, max=50))
    format_id = fields.Integer(required=True)
    description = fields.String(required=True)
    
class CollaboratorShare(Schema):
    id_acta = fields.String(required=True)
    email_inst = fields.String(required=True, validate=validate.Length(min=3, max=50))
 
class DocumentUpdate(Schema):
    id_a = fields.String(required=True)
    html_content = fields.String(required=True)
    content = fields.Raw(required=True)
    