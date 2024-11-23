from odoo import http
from odoo import models, fields, api
from odoo.http import Controller, route, request
import logging

# Tạo một logger
_logger = logging.getLogger(__name__)

class CustomerInfo(models.Model):
    _name = 'tomishow'
    _description = 'tomishow Render'


class HomePage(Controller):
    @route(['/home'], type='http', auth='public', website=True)
    def HomePage(self):
        return request.render('tomishow.Home_Page')
class Details(Controller):
    @route(['/details'], type='http', auth='public', website=True)
    def Details(self):
        return request.render('tomishow.Details_Page')
