'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api,exceptions
from .util import *

class div_8(models.Model):
    _name = 'cms.div8'
    _description = ''

    menu_item8 = fields.Char(string= "Menu Item 8")
    menu_item8_jp=fields.Char(string='Menu Items (JP)')
    menu_item8_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    name= fields.Char(default='Div 8')

    google_map = fields.Char(string='Link Google Map')

    time = fields.Char(string='Thời gian')
    time_jp = fields.Char(string='Thời gian (JP)')
    time_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")


    text_fields = ['time',"menu_item8"]

    connection_ids = fields.One2many('cms.div8.connection', 'div8_id', string='Thông tin liên hệ')

    @api.model
    def create(self, vals):
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm div 8')
        else:
            return super(div_8, self).create(vals)
    def write(self, vals):
        translate_fields_to_japanese(vals, self.text_fields)
        return super(div_8, self).write(vals)
    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div8'].get_div_8())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }
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

        ans = {
            'google_map': div8.google_map,

            'connections': div8.get_connection()
        }
        get_text(self.text_fields, ans, div8)
        return ans


class div_8_connection(models.Model):
    _name = 'cms.div8.connection'
    _description = ''

    title = fields.Char(string='Tiêu đề')
    title_jp = fields.Char(string='Tiêu đề (JP)')
    title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    icon = fields.Image(string='Icon')
    icon_counter = fields.Integer(default=0)

    text = fields.Html(string='Text')
    text_jp = fields.Html(string='Text (JP)')
    text_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")


    text_fields = ['title', 'text']
    img=['icon']
    div8_id = fields.Many2one('cms.div8', string='Div 8', default=lambda self: self.env['cms.div8'].search([])[0].id)

    def create(self,vals):
        translate_fields_to_japanese(vals, self.text_fields)
        res = super(div_8_connection, self).create(vals)
        save_img_sub_model('div8', 'connection', res.id, res.img, vals, res)
        return res
    def write(self, vals):
        translate_fields_to_japanese(vals, self.text_fields)
        save_img_sub_model('div8', 'connection', self.id, self.img, vals, self)
        return super(div_8_connection, self).write(vals)
    def unlink(self):
        for record in self:
            remove_img_sub_model('div8', 'connection', record.id)
        return super(div_8_connection, self).unlink()
    def get_connection(self):

        ans = {}
        get_text(self.text_fields, ans, self)
        get_img_path_sub_model(ans, 'div8', 'connection', self.id, self.img, self)
        return ans


