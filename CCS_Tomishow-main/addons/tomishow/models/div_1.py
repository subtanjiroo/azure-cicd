'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api
from odoo import http
from odoo.http import request
import json

class div_1(models.Model):
    _name = 'cms.div1'
    _description = ''

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
    def get_div_1(self):
        """
            Get div_1 data

        :param self: object
        :return:
            json format of div_1
            {
                'main_title': main_title,
                'main_text': main_text,
                'left_icon': left_icon,
                'left_title': left_title,
                'left_text': left_text,
                'mid_icon': mid_icon,
                'mid_title': mid_title,
                'mid_text': mid_text,
                'right_icon': right_icon,
                'right_title': right_title,
                'right_text': right
            }
        """

        div_1 = self.env['cms.div1'].search([])
        div_1 = div_1[0]
        return {
            'main_title': div_1.main_title,
            'main_text': div_1.main_text,
            'left_icon': div_1.left_icon,
            'left_title': div_1.left_title,
            'left_text': div_1.left_text,
            'mid_icon': div_1.mid_icon,
            'mid_title': div_1.mid_title,
            'mid_text': div_1.mid_text,
            'right_icon': div_1.right_icon,
            'right_title': div_1.right_title,
            'right_text': div_1.right_text
        }

class Div1_Controller(http.Controller):
    @http.route('/get_div_1', type='http', auth='public', methods=['GET'])
    def get_div_1_data(self):
        div_data = request.env['cms.div1'].get_div_1()
        return request.make_response(
            json.dumps(div_data), 
            [('Content-Type', 'application/json')]
        )

