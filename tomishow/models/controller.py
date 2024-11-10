from odoo import http
from odoo import models, fields, api
from odoo.http import Controller, route, request
import logging

# Tạo một logger
_logger = logging.getLogger(__name__)

class CustomerInfo(models.Model):
    _name = 'tomishow'
    _description = 'tomishow Render'


class Partner(Controller):
    @route(['/home'], type='http', auth='public', website=True)
    def partner(self):
        return request.render('tomishow.product_list_template')
