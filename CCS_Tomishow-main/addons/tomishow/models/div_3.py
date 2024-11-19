'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields


class div_3(models.Model):
    _name = 'cms.div3'
    _description = ''

    main_title = fields.Char(string='Tiêu đề chính')
    icon_and_text = fields.One2many('cms.div3.iconandtext', 'div_3_id', string='Icon và Text')


class div3_icon_and_text(models.Model):
    _name = 'cms.div3.iconandtext'
    _description = ''

    icon = fields.Image(string='Icon', max_width=100, max_height=100)
    text = fields.Char(string='Tiêu đề')


    div_3_id = fields.Many2one('cms.div3', string='Div 3', default = lambda self: self.env['cms.div3'].search([]).id)