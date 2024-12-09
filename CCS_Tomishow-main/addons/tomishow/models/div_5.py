'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api, exceptions
from .util import *

class div_5(models.Model):
    _name = 'cms.div5'
    _description = ''

    menu_item5 = fields.Char(string= "Menu Item 5")
    menu_item5_jp=fields.Char(string='Menu Items (JP)')
    menu_item5_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    name = fields.Char(default='Div 5')
    quote = fields.Char(string='Quote')
    quote_jp = fields.Char(string='Quote (JP)')
    quote_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    author = fields.Char(string='Tác giả')
    author_jp = fields.Char(string='Tác giả (JP)')
    author_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    title = fields.Char(string='Tiêu đề')
    title_jp = fields.Char(string='Tiêu đề (JP)')
    title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    image = fields.Image(string='Hình ảnh')

    text_fields = ['quote', 'author', 'title',"menu_item5"]
    img=['image']

    @api.model
    def create(self,vals):
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm bản ghi')
        return super(div_5, self).create(vals)
    def write (self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        save_img('div5',self.img,vals,self)
        return super(div_5, self).write(vals)
    @api.model
    def get_div_5(self):
        """
            Get div 5 for web
        :return: dict
            {
                'quote': string,
                'author': string,
                'title': string,
            }
        """
        div5 = self.search([])[0]
        if not div5:
            raise exceptions.ValidationError('Không có dữ liệu')
        ans = {}
        get_text(self.text_fields, ans, div5)
        get_img_path(ans,'div5',self.img, div5)
        return ans

    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div5'].get_div_5())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }
