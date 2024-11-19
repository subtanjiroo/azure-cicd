'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields


class div_4(models.Model):
    _name = 'cms.div4'
    _description = ''

    main_title = fields.Char(string='Tiêu đề chính')
    project_ids= fields.One2many('cms.div4.project', 'div4_id', string='Projects')


class div_4_project(models.Model):
    _name = 'cms.div4.project'
    _description = ''

    title = fields.Char(string='Tiêu đề')
    small_text = fields.Text(string='Text')
    image = fields.Image(string='Hình ảnh', max_width=800, max_height=400)

    text = fields.Html(string='Text')

    div4_id = fields.Many2one('cms.div4', string='Project', default = lambda self: self.env['cms.div_4'].search([]).id)



