'''
Author: Thinh dep trai
Model Description: 
'''
import base64
import os
from odoo import models, fields, api, exceptions


class header(models.Model):
    _name = 'cms.header'
    _description = 'CMS model for header'


    name = fields.Char(default='Header')
    logo = fields.Image(string='Logo', max_width=100, max_height=100)
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

    def write(self,vals):

        if vals.get('logo'):
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/header/logo.png"
            byte = base64.b64decode(vals['logo'])

            with open(folder_path, 'wb') as f:
                f.write(byte)
        if vals.get('back_ground'):
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/header/background.png"
            byte = base64.b64decode(vals['back_ground'])

            with open(folder_path, 'wb') as f:
                f.write(byte)
        return super(header, self).write(vals)


    @api.model
    def get_header(self):

        logo_path ="tomishow/static/imgs/header/logo.png"
        back_ground_path ="tomishow/static/imgs/header/background.png"


        header = self.search([])[0]
        if not header:
            raise exceptions.ValidationError('Không có header')

        return {
            'logo': logo_path,
            'logo_left_text': header.logo_left_text,
            'logo_right_text': header.logo_right_text,
            'big_title': header.big_title,
            'small_title': header.small_title,
            'phone_number': header.phone_number,
            'back_ground': back_ground_path
        }







