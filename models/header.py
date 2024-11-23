'''
Author: Thinh dep trai
Model Description: 
'''
import os
from odoo import models, fields, api, exceptions
import base64

class header(models.Model):
    _name = 'cms.header'
    _description = 'CMS model for header'

    name = fields.Char(default='Header')
    logo = fields.Image(string='Logo', max_width=100, max_height=100)
    logo_left_text = fields.Char(string='Text bên trái Logo')
    logo_right_text = fields.Char(string='Text bên phải Logo')

    big_title = fields.Char(string='Title đề chính')
    small_title = fields.Char(string='Slogan')

    phone_number = fields.Char(string='Số điện thoại')

    back_ground = fields.Binary(string='Background', max_width=1000, max_height=600)

    def test(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.header'].get_header())

    @api.model
    def create(self, vals):
        if self.search([]):
            raise Exception("Đã có header rồi")
        return super(header, self).create(vals)

    @api.model
    def get_header(self):
        """
        Get the header data for web
        :return: dict
            {
                'logo': 'logo/path',
                'logo_left_text': logo_left_text,
                'logo_right_text': logo_right_text,
                'big_title': big_title,
                'small_title': small_title,
                'phone_number': phone_number,
                'back_ground': 'back_ground/path'
            }
        """

        header = self.search([])[0]
        if not header:
            raise exceptions.ValidationError('Không có header')

        # Chuyển đổi ảnh dạng binary sang chuỗi base64 để có thể JSON-serializable
        back_ground_base64 = base64.b64encode(header.back_ground).decode('utf-8') if header.back_ground else None
        logo_base64 = base64.b64encode(header.logo).decode('utf-8') if header.logo else None

        return {
            'logo': logo_base64,
            'logo_left_text': header.logo_left_text,
            'logo_right_text': header.logo_right_text,
            'big_title': header.big_title,
            'small_title': header.small_title,
            'phone_number': header.phone_number,
            'back_ground': back_ground_base64
        }
