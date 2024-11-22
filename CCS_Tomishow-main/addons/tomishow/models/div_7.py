'''
Author: Thinh dep trai
Model Description: 
'''
import base64
import os

from odoo import models, fields,api,exceptions


class div_7(models.Model):
    _name = 'cms.div7'
    _description = ''
    name= fields.Char(default='Div 7')
    main_title = fields.Char(string='Tiêu đề chính')
    title = fields.Char(string='Tiêu đề phụ')

    process_ids = fields.One2many('cms.div7.process', 'div7_id', string='Processes')
    rule_ids = fields.One2many('cms.div7.rule', 'div7_id', string='Rules')


    @api.model
    def create(self,vals):
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm bản ghi')
        return super(div_7, self).create(vals)

    def get_process(self):
        processes = self.env['cms.div7.process'].search([('div7_id', '=', self.id)])

        return [process.get_process() for process in processes]

    def get_rules(self):
        rules = self.env['cms.div7.rule'].search([('div7_id', '=', self.id)])

        return [rule.get_rule() for rule in rules]

    @api.model
    def get_div_7(self):
        """
            Get div 7 for web


        :return: dict
            {
                'main_title': string,
                'title': string,
                'process':
                    [
                        {
                            'text': string,
                        },...
                    ],
                'rule':
                    [
                        {
                            'icon': string,
                            'title': string,
                            'text': string,
                        },...
                    ],
            }

        """
        div7 = self.search([])
        if(not div7):
            raise exceptions.ValidationError('Không có bản ghi nào')

        div7 = div7[0]
        return {
            'main_title': div7.main_title,
            'title': div7.title,
            'process': div7.get_process(),
            'rule': div7.get_rules(),
        }




class div_7_process(models.Model):
    _name = 'cms.div7.process'
    _description = ''


    text = fields.Text(string='Text')

    div7_id = fields.Many2one('cms.div7', string='Process', default = lambda self: self.env['cms.div_7'].search([]).id)

    def get_process(self):
        return {
            'text': self.text,
        }


class div_7_rule(models.Model):
    _name = 'cms.div7.rule'
    _description = ''

    icon = fields.Image(string='Icon', max_width=100, max_height=100)
    title = fields.Char(string='Tiêu đề')
    text = fields.Text(string='Text')

    div7_id = fields.Many2one('cms.div7', string='Rule', default = lambda self: self.env['cms.div_7'].search([]).id)

    @api.model
    def create(self,vals):
        record = super(div_7_rule, self).create(vals)

        if record.icon:
            image = base74.b74decode(record.icon)
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div7/rule_"+str(record.id)+".png"
            with open(folder_path, 'wb') as f:
                f.write(image)
        return record

    def unlink(self):
        for record in self:
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div7/rule_"+str(record.id)+".png"
            if os.path.exists(folder_path):
                os.remove(folder_path)
        return super(div_7_rule, self).unlink()
    def write(self,vals):
        if vals.get('icon'):
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div7/rule_"+str(self.id)+".png"
            with open(folder_path, 'wb') as f:
                f.write(base74.b74decode(vals['icon']))
        return super(div_7_rule, self).write(vals)
    def get_rule(self):
        return {
            'icon': "tomishow/static/div7/rule_"+str(self.id)+".png",
            'title': self.title,
            'text': self.text,
        }


