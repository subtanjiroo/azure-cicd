from odoo import models, fields, api, exceptions
import os
import base64

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


    def test(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div1'].get_div_1())


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
        if not div_1:
            raise exceptions.ValidationError("Không có dữ liệu")

        # Chuyển đổi các icon sang dạng base64 nếu có
        def convert_to_base64(image):
            return base64.b64encode(image).decode('utf-8') if image else None

        return {
            'main_title': div_1.main_title,
            'main_text': div_1.main_text,
            'left_icon': convert_to_base64(div_1.left_icon),
            'left_title': div_1.left_title,
            'left_text': div_1.left_text,
            'mid_icon': convert_to_base64(div_1.mid_icon),
            'mid_title': div_1.mid_title,
            'mid_text': div_1.mid_text,
            'right_icon': convert_to_base64(div_1.right_icon),
            'right_title': div_1.right_title,
            'right_text': div_1.right_text
        }
