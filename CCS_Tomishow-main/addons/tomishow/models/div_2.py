'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api
from odoo import http
from odoo.http import request
import json

class div_2(models.Model):
    _name = 'cms.div2'
    _description = ''

    main_title = fields.Char(string='Main Title')
    main_text = fields.Text(string='Main Text')

    title_1 = fields.Char(string='Title 1')
    text_1 = fields.Text(string='Text 1')

    title_2 = fields.Char(string='Title 2')
    text_2 = fields.Text(string='Text 2')

    title_3 = fields.Char(string='Title 3')
    text_3 = fields.Text(string='Text 3')

    title_4 = fields.Char(string='Title 4')
    text_4 = fields.Text(string='Text 4')


    flip_board_1_text_not_flipped = fields.Text(string='Text Not Flipped')
    flip_board_1_text_flipped = fields.Text(string='Text Flipped')
    flip_board_1_background_image = fields.Image(string='Background Image', max_width=1000, max_height=100)
    flip_board_2_text_not_flipped = fields.Text(string='Text Not Flipped')
    flip_board_2_text_flipped = fields.Text(string='Text Flipped')
    flip_board_2_background_image = fields.Image(string='Background Image', max_width=1000, max_height=100)
    flip_board_3_text_not_flipped = fields.Text(string='Text Not Flipped')
    flip_board_3_text_flipped = fields.Text(string='Text Flipped')
    flip_board_3_background_image = fields.Image(string='Background Image', max_width=1000, max_height=100)


    @api.model
    def create(self, vals):
        res = super(div_2, self).create(vals)
        return res

    @api.model
    def get_div_2(self):
        """
            Get div_2 data
        :param self: object
        :return:
            json format of div_2
            {
                'main_title': main_title,
                'main_text': main_text,
                'title_1': title_1,
                'text_1': text_1,
                'title_2': title_2,
                'text_2': text_2,
                'title_3': title_3,
                'text_3': text_3,
                'title_4': title_4,
                'text_4': text_4,
                'flip_board': flip_board
            }
        """
        div_2 = self.env['cms.div2'].search([])  # Lấy record đầu tiên của div_2
        div_2 = div_2[0]
        flip_board = []
        # Thay vì dùng flip_board, lấy các trường flip_board_1, flip_board_2, flip_board_3
        flip_board.append({
            'text_not_flipped': div_2.flip_board_1_text_not_flipped,
            'text_flipped': div_2.flip_board_1_text_flipped,
            'background_image': div_2.flip_board_1_background_image
        })
        flip_board.append({
            'text_not_flipped': div_2.flip_board_2_text_not_flipped,
            'text_flipped': div_2.flip_board_2_text_flipped,
            'background_image': div_2.flip_board_2_background_image
        })
        flip_board.append({
            'text_not_flipped': div_2.flip_board_3_text_not_flipped,
            'text_flipped': div_2.flip_board_3_text_flipped,
            'background_image': div_2.flip_board_3_background_image
        })

        return {
            'main_title': div_2.main_title,
            'main_text': div_2.main_text,
            'title_1': div_2.title_1,
            'text_1': div_2.text_1,
            'title_2': div_2.title_2,
            'text_2': div_2.text_2,
            'title_3': div_2.title_3,
            'text_3': div_2.text_3,
            'title_4': div_2.title_4,
            'text_4': div_2.text_4,
            'flip_board': flip_board  # Trả về danh sách flip_board đã sửa lại
        }


class Div2_Controller(http.Controller):
    @http.route('/get_div_2', type='http', auth='public', methods=['GET'])
    def get_div_2_data(self):
        div_data = request.env['cms.div2'].get_div_2()
        return request.make_response(
            json.dumps(div_data), 
            [('Content-Type', 'application/json')]
        )











