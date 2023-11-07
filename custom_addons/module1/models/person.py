from odoo import api, fields, models

class modulePerson(models.Model):
    _name = "module.person"
    _description = 'Person table in odoo dev db'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    phoneNumber = fields.Char(string='Phone Number')
    town = fields.Char(string='City')
    email = fields.Char(string='Email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],string='gender')