from marshmallow import Schema, fields, validate, validates, ValidationError


class RegisterUser(Schema):
    email_inst = fields.String(
        required=True, validate=validate.Length(min=13, max=50))
    document_u = fields.String(
        required=True, validate=validate.Length(min=3, max=50))
    password_u = fields.String(
        required=True, validate=validate.Length(min=8, max=20))
    name_u = fields.String(
        required=False)
    lastname_u = fields.String(
        required=False)
    phone_u = fields.String(
        required=False)
    regional_u = fields.String(
        required=False)
    center_u = fields.String(
        required=False)
    description_c = fields.String(
        required=False)
    description_r = fields.String(
        required=False)
    bonding_type = fields.String(
        required=False)

class RegisterExtra(Schema):
    email_inst = fields.String(
        required=False)
    document_u = fields.String(
        required=False)
    password_u = fields.String(
        required=False)
    name_u = fields.String(
        required=True, validate=validate.Length(min=3, max=30))
    lastname_u = fields.String(
        required=True, validate=validate.Length(min=3, max=30))
    phone_u = fields.String(
        required=True, validate=validate.Length(min=7, max=10))
    regional_u = fields.String(
        required=True, validate=validate.Length(min=3, max=100))
    centro_u = fields.String(
        required=True, validate= validate.Length(min=3, max=100))
    competencies_u = fields.String(
        required=True, validate= validate.Length(min=5, max=50))
    results_u = fields.String(
        required=True, validate= validate.Length(min=5, max=50))
    bonding_type = fields.String(
        required= True, validate= validate.Length(min=6, max=11))
