'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api,exceptions
import base64

class div_8(models.Model):
    _name = 'cms.div8'
    _description = ''

    name= fields.Char(default='Div 8')
    google_map = fields.Char(string='Link Google Map')

    time = fields.Char(string='Thời gian')

    connection_ids = fields.One2many('cms.div8.connection', 'div8_id', string='Thông tin liên hệ')

    @api.model
    def create(self, vals):
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm div 8')
        else:
            return super(div_8, self).create(vals)
    def test(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div8'].get_div_8())
    def get_connection(self):
        connections = self.env['cms.div8.connection'].search([('div8_id', '=', self.id)])
        return [connection.get_connection() for connection in connections]

    @api.model
    def get_div_8(self):
        """
            Get Div 8 data for web
        :return: dict
            {
                'google_map': string,
                'time': string,
                'connection': string,
                'connections': [
                    {
                        'title': '',
                        'icon': '',
                        'text': ''
                    },
                    ...
                ]
            }
        """

        div8 = self.search([])[0]
        if not div8:
            raise exceptions.ValidationError('Không có dữ liệu')

        return {
            'google_map': div8.google_map,
            'time': div8.time,
            'connections': div8.get_connection()
        }


class div_8_connection(models.Model):
    _name = 'cms.div8.connection'
    _description = ''

    title = fields.Char(string='Tiêu đề')
    icon = fields.Image(string='Icon')
    text = fields.Html(string='Text')
    div8_id = fields.Many2one('cms.div8', string='Div 8', default=lambda self: self.env['cms.div8'].search([])[0].id)

    def get_connection(self):
        # Nếu có icon, chuyển đổi nó thành chuỗi base64
        icon_base64 = ''
        if self.icon:
            icon_base64 = base64.b64encode(self.icon).decode('utf-8')

        return {
            'title': self.title,
            'icon': icon_base64,  # Trả về chuỗi base64 thay vì bytes
            'text': self.text
        }

