'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api, exceptions


class div_5(models.Model):
    _name = 'cms.div5'
    _description = ''
    name = fields.Char(default='Div 5')
    quote = fields.Char(string='Quote')
    author = fields.Char(string='Author')
    title = fields.Char(string='Title')

    @api.model
    def create(self,vals):
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm bản ghi')
        return super(div_5, self).create(vals)

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

        return {
            'quote': div5.quote,
            'author': div5.author,
            'title': div5.title,
        }


