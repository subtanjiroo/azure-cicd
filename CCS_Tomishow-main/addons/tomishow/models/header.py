'''
Author: Thinh dep trai
Model Description: 
'''
import base64
import os
from odoo import models, fields, api


class header(models.Model):
    _name = 'cms.header'
    _description = 'CMS model for header'



    logo = fields.Image(string='Logo' , readonly=False,computed="get_logo",  max_width=100, max_height=100)

    # logo_path = fields.Char(string='Path')
    logo_left_text = fields.Char(string='Text bên trái Logo')
    logo_right_text = fields.Char(string='Text bên phải Logo')



    #big title
    big_title = fields.Char(string='Title đề chính')
    #small title
    small_title = fields.Char(string='Slogan')

    phone_number = fields.Char(string='Số điện thoại')

    back_ground = fields.Binary(string='Background', max_width=1000, max_height=600)


    #esure that there's only 1 header
    @api.model
    def create(self, vals):
        if(self.search([])):
            raise Exception("Đã có header rồi")
        return super(header, self).create(vals)

    @api.onchange("logo")
    def save_image(self):
        #create folder if path is not created
        if(self.logo):
            with open("opt/temp/cms/logo_path.png", "wb") as f:
                f.write(base64.b64decode(self.logo))


    @api.depends("logo_path")
    def get_logo(self):
        for rec in self:
            if(rec.logo_path):
                rec.logo = base64.encode(open(rec.logo_path,"rb").read())
            else:
                rec.logo_path = "opt/temp/cms/logo_path.png"

    def test_button(self):
        #check if there are file at logo_path

        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.test_html)






