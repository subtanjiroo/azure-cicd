from odoo import models, fields, api, exceptions
import base64
import os

class div_6(models.Model):
    _name = 'cms.div6'
    _description = ''
    name = fields.Char(default='Div 6')
    main_title = fields.Char(string='Tiêu đề chính')
    people_ids = fields.One2many('cms.div6.people', 'div6_id', string='People')

    @api.model
    def create(self, vals):
        """
            Ensure only one Div 6 is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Chỉ được tạo một Div 6')
        return super(div_6, self).create(vals)

    def get_people_web(self):
        peoples = self.env['cms.div6.people'].search([('div6_id', '=', self.id)])
        return [people.get_people() for people in peoples]

    def test(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div6'].get_div_6())

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

    div6_id = fields.Many2one('cms.div6', string='People', default=lambda self: self.env['cms.div6'].search([]).id)

    def convert_to_base64(self, image):
        """
        Convert image to base64 encoding
        """
        if image:
            image_data = image
            return base64.b64encode(image_data).decode('utf-8')
        return None

    def get_people(self):
        return {
            'name': self.name,
            'image': self.convert_to_base64(self.image),  # Convert image to base64
            'position': self.position,
            'text': self.text
        }
