'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api, exceptions
import os
import base64
from odoo import http
import json
from odoo.http import Controller, route, request


class div_1(models.Model):
    _name = 'cms.div1'
    _description = ''

    name = fields.Char(default='Div 1')
    main_title = fields.Char(string='Tiêu đề chính')
    main_text = fields.Text(string='Text chính')

    left_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    left_title = fields.Char(string='Tiêu đề')
    left_text = fields.Text(string='Text')

    mid_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    mid_title = fields.Char(string='Tiêu đề')
    mid_text = fields.Text(string='Text')

    right_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    right_title = fields.Char(string='Tiêu đề')
    right_text = fields.Text(string='Text')


    @api.model
    def create(self,vals):
        """
            Ensure that there is only one div 1
        """
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm div 1')
        else:
            return super(div_1, self).create(vals)


    def write(self,vals):
        """
            save the logo_path in the path folder
        :return:
        """
        folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div1"
        left_icon_path = folder_path + "/left_icon.png"
        mid_icon_path = folder_path + "/mid_icon.png"
        right_icon_path = folder_path + "/right_icon.png"


        if vals['left_icon']:
            byte = base64.b64decode(self.left_icon)
            with open(left_icon_path, 'wb') as f:
                f.write(byte)
        if vals['mid_icon']:
            byte = base64.b64decode(self.mid_icon)
            with open(mid_icon_path, 'wb') as f:
                f.write(byte)
        if vals['right_icon']:
            byte = base64.b64decode(self.right_icon)
            with open(right_icon_path, 'wb') as f:
                f.write(byte)

        return super(div_1, self).write(vals)



    @api.model
    def get_div_1(self):

        div_1 = self.env['cms.div1'].search([])
        if not div_1:
            raise exceptions.ValidationError("Không có dữ liệu")


        div_1 = div_1[0]
        folder_path = "/tomishow/static/src/imgs/div1"

        left_icon_path = folder_path + "/left_icon.png"
        mid_icon_path = folder_path + "/mid_icon.png"
        right_icon_path = folder_path + "/right_icon.png"

        return {
            'main_title': div_1.main_title,
            'main_text': div_1.main_text,
            'left_icon': left_icon_path,
            'left_title': div_1.left_title,
            'left_text': div_1.left_text,
            'mid_icon': mid_icon_path,
            'mid_title': div_1.mid_title,
            'mid_text': div_1.mid_text,
            'right_icon': right_icon_path,
            'right_title': div_1.right_title,
            'right_text': div_1.right_text
        }
