import base64
from odoo import models, fields, api, exceptions

class div_7(models.Model):
    _name = 'cms.div7'
    _description = ''
    name = fields.Char(default='Div 7')
    main_title = fields.Char(string='Tiêu đề chính')
    title = fields.Char(string='Tiêu đề phụ')

    process_ids = fields.One2many('cms.div7.process', 'div7_id', string='Processes')
    rule_ids = fields.One2many('cms.div7.rule', 'div7_id', string='Rules')
    clickable_image_ids = fields.One2many('cms.div7.image', 'div7_id', string='Clickable Images')

    def test(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div7'].get_div_7())

    @api.model
    def create(self, vals):
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm bản ghi')
        return super(div_7, self).create(vals)

    def get_process(self):
        processes = self.env['cms.div7.process'].search([('div7_id', '=', self.id)])
        return [process.get_process() for process in processes]

    def get_rules(self):
        rules = self.env['cms.div7.rule'].search([('div7_id', '=', self.id)])
        return [rule.get_rule() for rule in rules]

    def get_clickable_images(self):
        images = self.env['cms.div7.image'].search([])  # Nếu cần filter, thay đổi query ở đây
        return [image.get_image() for image in images]

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
                'clickable_images': [
                    {
                        'image': string,
                    }
                ]
            }
        """
        div7 = self.search([])
        if not div7:
            raise exceptions.ValidationError('Không có bản ghi nào')

        div7 = div7[0]
        return {
            'main_title': div7.main_title,
            'title': div7.title,
            'process': div7.get_process(),
            'rule': div7.get_rules(),
            'clickable_images': div7.get_clickable_images()
        }

    def convert_to_base64(self, image):
        """
        Convert image to base64 encoding
        """
        if image:
            image_data = image
            return base64.b64encode(image_data).decode('utf-8')
        return None

class div_7_process(models.Model):
    _name = 'cms.div7.process'
    _description = ''

    text = fields.Text(string='Text')

    div7_id = fields.Many2one('cms.div7', string='Process', default=lambda self: self.env['cms.div_7'].search([]).id)

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

    div7_id = fields.Many2one('cms.div7', string='Rule', default=lambda self: self.env['cms.div_7'].search([]).id)

    def get_rule(self):
        return {
            'icon': self.env['cms.div7'].convert_to_base64(self.icon),  # Use div_7 to call the method
            'title': self.title,
            'text': self.text,
        }

class clickable_image(models.Model):
    _name = 'cms.div7.image'
    _description = ''
    _rec_name = 'title'

    title = fields.Char(string='Title')
    image = fields.Image(string='Image', max_width=200, max_height=200)
    div7_id = fields.Many2one('cms.div7', string='Clickable Image', default=lambda self: self.env['cms.div_7'].search([]).id)

    def get_image(self):
        return {
            'image': self.convert_to_base64(self.image),  # Convert image to base64
        }
