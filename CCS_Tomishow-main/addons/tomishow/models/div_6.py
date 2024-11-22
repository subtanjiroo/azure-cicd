'''
Author: Thinh dep trai
Model Description: 
'''
import base64
import os

from odoo import models, fields, api,exceptions


class div_6(models.Model):
    _name = 'cms.div6'
    _description = ''
    name= fields.Char(default='Div 6')
    main_title = fields.Char(string='Tiêu đề chính')
    people_ids = fields.One2many('cms.div6.people', 'div6_id', string='People')

    @api.model
    def create(self,vals):
        """
            Ensure only one Div 6 is created

        """
        if self.search([]):
            raise exceptions.ValidationError('Chỉ được tạo một Div 6')
        return super(div_6, self).create(vals)

    def get_people_web(self):
        peoples = self.env['cms.div6.people'].search([('div6_id', '=', self.id)])
        return [people.get_people() for people in peoples]



    @api.model
    def get_div_6(self):
        """
            Get Div 6 data for web
        :return: dict
            {
                'main_title': '',
                'people': [
                    {
                        'name': '',
                        'image': '',
                        'position': '',
                        'text': ''
                    },
                    ...
                ]
            }
        """

        div6 = self.search([])[0]
        if not div6:
            raise exceptions.ValidationError('Không có dữ liệu')

        return {
            'main_title': div6.main_title,
            'people': div6.get_people_web()
        }

class div_6_people(models.Model):
    _name = 'cms.div6.people'
    _description = ''

    name = fields.Char(string='Tên')
    image = fields.Image(string='Hình ảnh', max_width=100, max_height=100)
    position = fields.Char(string='Chức vụ')
    text = fields.Text(string='Text')

    div6_id = fields.Many2one('cms.div6', string='People', default = lambda self: self.env['cms.div_6'].search([]).id)

    @api.model
    def create(self,vals):
        """ create image file if image is not null """
        record = super(div_6_people, self).create(vals)
        if record.image:
            image = base64.b64decode(record.image)
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div6/people_"+str(record.id)+".png"
            with open(folder_path, 'wb') as f:
                f.write(image)
        return record
    def unlink(self):
        for record in self:
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div6/people_"+str(record.id)+".png"
            if os.path.exists(folder_path):
                os.remove(folder_path)
        return super(div_6_people, self).unlink()

    def write(self,vals):
        """ update image file if image is changed """
        if vals.get('image'):
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div6/people_"+str(self.id)+".png"
            with open(folder_path, 'wb') as f:
                f.write(base64.b64decode(vals['image']))
        return super(div_6_people, self).write(vals)


    def get_people(self):
        return {
            'name': self.name,
            'image': '/tomishow/static/div6/people_'+str(self.id)+'.png',
            'position': self.position,
            'text': self.text
        }



