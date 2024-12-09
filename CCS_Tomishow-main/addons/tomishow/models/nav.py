'''
Author: Thinh dep trai
Model Description: 
'''

import os
from odoo import models, fields, api, exceptions
import base64
from .util import *

class navigationbar(models.Model): 
    _name = 'cms.nav'
    _description = 'CMS for nav'

    name = fields.Char(default='Navigation Bar')
    logo = fields.Image(string='Logo', max_width=100, max_height=100)

    image = fields.Image(string='Logo Connect', max_width=100, max_height=100)
    connect_phone = fields.Char(string="Phone")
    connect_phone_jp = fields.Char(string="Text (JP)")
    connect_phone_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    connect_text = fields.Char(string="Text")
    connect_text_jp = fields.Char(string="Text (JP)")
    connect_text_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    text_fields= ['connect_text','connect_phone']
    img=['image','logo']
    @api.model
    def create(self, vals):
        """
        Ensure that only one nav record is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Only one navigation is allowed')
        else:
            return super(navigationbar, self).create(vals)

    def write(self, vals):
        """
        Translate and save img
        """
        translate_fields_to_japanese(vals,self.text_fields)
        save_img('nav',self.img,vals,self)
        return super(navigationbar, self).write(vals)
    def preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        ans={}
        get_img_path(ans,'header',self.img,self)
        get_text(self.text_fields,ans,self)
        _logger.info(self.env['cms.header'].get_header())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }
    @api.model
    def get_nav(self):
        """
        Get nav data in JSON serializable format

        :return:
            JSON format of nav
            {
                'logo': logo,
                'image': image,
                'connect_phone': connect_phone,
                'connect_text': connect_text,
                'connect_text_jp': connect_text_jp,
            }
        """
        nav = self.search([])[0]

        if not nav:
            raise exceptions.ValidationError('Navigation bar not found')
        ans = {}
        get_text(self.text_fields, ans, nav)
        get_img_path(ans, 'nav', nav.img, nav)

        return ans
