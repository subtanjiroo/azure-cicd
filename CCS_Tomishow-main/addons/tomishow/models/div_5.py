'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields


class div_5(models.Model):
    _name = 'cms.div5'
    _description = ''

    main_title = fields.Char(string='Tiêu đề chính')
    people_ids = fields.One2many('cms.div5.people', 'div5_id', string='People')
class div_5_people(models.Model):
    _name = 'cms.div5.people'
    _description = ''

    name = fields.Char(string='Tên')
    image = fields.Image(string='Hình ảnh', max_width=100, max_height=100)
    position = fields.Char(string='Chức vụ')
    text = fields.Text(string='Text')

    div5_id = fields.Many2one('cms.div5', string='People', default = lambda self: self.env['cms.div_5'].search([]).id)

