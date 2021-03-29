from marshmallow import Schema, fields, validate, validates, ValidationError

class DocumentVal(Schema):
    id_u = fields.String(required=True, validate=validate.Length(min=3, max=50))
    format_id = fields.Integer(required=True)
    
class CollaboratorShare(Schema):
    id_acta = fields.String(required=True)
    email_inst = fields.String(required=True, validate=validate.Length(min=3, max=50))
 
class DocumentUpdate(Schema):
    id_a = fields.String(required=True)
    content = fields.Raw(required=True)
    

"""
class HeaderContent(Schema):
    num_act = fields.String(required=True) # validar consecuente
    name_meet = fields.String(required=True)
    city_date = fields.String(required=True)
    start_time = fields.Time(required=True)
    end_time = fields.Time(required=True)
    place = fields.String(required=True)
    reg_cent = fields.String(required=True)
    topic = fields.String(required=True)
    objective = fields.String(required=True)
    len_header = fields.String(required=False)
    
class Assis(Schema):
    num_asis = fields.String(required=True)
    full_name = fields.String(required=True)
    id_instru = fields.String(required=True)
    bonding_type = fields.String(required=True)
    company_depen = fields.String(required=True)
    mail_instru = fields.String(required=True)
    phone_ext = fields.String(required=True)
    
class FooterContent(Schema):
    activity = fields.String(required=True)
    respo = fields.String(required=True)
    date_act = fields.Date(required=True)
    obser = fields.String(required=True)
    reg_asis = fields.String(required=True)
    objective = fields.String(required=True)
    list_asis = fields.List(fields.Nested(Assis), required=True)

class ActaContent(Schema):
    header = fields.Nested(HeaderContent)
    body_h = fields.String(required=True)
    body_t = fields.String(required=True)
    footer = fields.Nested(FooterContent)
"""    

    