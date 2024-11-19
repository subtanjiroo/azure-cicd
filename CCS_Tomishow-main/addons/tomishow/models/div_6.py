'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields


class div_6(models.Model):
    _name = 'cms.div6'
    _description = ''

    main_title = fields.Char(string='Tiêu đề chính')
    title = fields.Char(string='Tiêu đề phụ')

    process_ids = fields.One2many('cms.div6.process', 'div6_id', string='Processes')
    rule_ids = fields.One2many('cms.div6.rule', 'div6_id', string='Rules')

class div_6_process(models.Model):
    _name = 'cms.div6.process'
    _description = ''


    text = fields.Text(string='Text')

    div6_id = fields.Many2one('cms.div6', string='Process', default = lambda self: self.env['cms.div_6'].search([]).id)

class div_6_rule(models.Model):
    _name = 'cms.div6.rule'
    _description = ''

    icon = fields.Image(string='Icon', max_width=100, max_height=100)
    title = fields.Char(string='Tiêu đề')
    text = fields.Text(string='Text')

    div6_id = fields.Many2one('cms.div6', string='Rule', default = lambda self: self.env['cms.div_6'].search([]).id)

