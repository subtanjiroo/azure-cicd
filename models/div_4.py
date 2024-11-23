from odoo import models, fields, api, exceptions
import base64
import os

class div_4(models.Model):
    _name = 'cms.div4'
    _description = ''

    name = fields.Char(default='Div 4')
    main_title = fields.Char(string='Tiêu đề chính')
    project_ids = fields.One2many('cms.div4.project', 'div4_id', string='Projects')

    @api.model
    def create(self, vals):
        """
            Ensure only one Div 4 is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Chỉ được tạo một Div 4')
        return super(div_4, self).create(vals)

    def test(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div4'].get_div_4())

    def get_project_web(self):
        projects = self.env['cms.div4.project'].search([('div4_id', '=', self.id)])
        return [project.get_project_for_web() for project in projects]

    @api.model
    def get_div_4(self):
        """
        Get Div 4 data for web
        :return: dict
            {
                'main_title': string,
                'projects':
                    [
                        {
                            'title': string,
                            'small_text': string,
                            'image': "image/path",
                        },....
                    ]
            }
        """

        div4 = self.search([])
        if not div4:
            raise exceptions.ValidationError('Không có dữ liệu')

        div4 = div4[0]

        return {
            'main_title': div4.main_title,
            'projects': div4.get_project_web()
        }

class div_4_project(models.Model):
    _name = 'cms.div4.project'
    _description = ''

    title = fields.Char(string='Tiêu đề')
    small_text = fields.Text(string='Text')
    image = fields.Image(string='Hình ảnh', max_width=800, max_height=400)

    text = fields.Html(string='Bài viết')

    div4_id = fields.Many2one('cms.div4', string='Project', default=lambda self: self.env['cms.div4'].search([]).id)

    def get_project_for_web(self):
        """
        Returns project data in a format suitable for web display.
        Converts image to base64 encoding if present.
        """
        def convert_to_base64(image):
            return base64.b64encode(image).decode('utf-8') if image else None

        return {
            'title': self.title,
            'small_text': self.small_text,
            'image': convert_to_base64(self.image)
        }
