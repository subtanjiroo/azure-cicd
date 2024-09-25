from odoo import models, fields, api

class Chatbox(models.TransientModel):
    _name = 'chatbox.ai'
    _description = 'Chatbox AI'

    name = fields.Char(string="Name")
    text = fields.Char(string="context")

