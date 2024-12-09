import base64
from odoo import models, fields, api, exceptions
from .util import *

class div_7(models.Model):
    _name = 'cms.div7'
    _description = ''
    name = fields.Char(default='Div 7')

    menu_item7 = fields.Char(string= "Menu Item 7")
    menu_item7_jp=fields.Char(string='Menu Items (JP)')
    menu_item7_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    main_title = fields.Char(string='Tiêu đề chính')
    main_title_jp = fields.Char(string='Tiêu đề chính (JP)')
    main_title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    title = fields.Char(string='Tiêu đề phụ')
    title_jp = fields.Char(string='Tiêu đề phụ (JP)')
    title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    process_ids = fields.One2many('cms.div7.process', 'div7_id', string='Processes')
    rule_ids = fields.One2many('cms.div7.rule', 'div7_id', string='Rules')
    clickable_image_ids = fields.One2many('cms.div7.image', 'div7_id', string='Clickable Images')

    text_fields = ['main_title', 'title',"menu_item7"]
    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div7'].get_div_7())

    @api.model
    def create(self, vals):
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm bản ghi')
        return super(div_7, self).create(vals)
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }
    def write(self, vals):
        translate_fields_to_japanese(vals, self.text_fields)
        return super(div_7, self).write(vals)

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
        ans ={
            'process': div7.get_process(),
            'rule': div7.get_rules(),
            'clickable_images': div7.get_clickable_images()
        }
        get_text(self.text_fields, ans, div7)
        return ans



class div_7_process(models.Model):
    _name = 'cms.div7.process'
    _description = ''

    text = fields.Text(string='Text')
    text_jp = fields.Text(string='Text (JP)')
    text_jp_toggle =fields.Boolean(string='JP' , computed="lambda x: False")

    text_fields = ['text']
    div7_id = fields.Many2one('cms.div7', string='Process', default=lambda self: self.env['cms.div_7'].search([]).id)

    @api.model
    def create(self,vals):
        translate_fields_to_japanese(vals, self.text_fields)
        return super(div_7_process, self).create(vals)

    def write(self, vals):
        translate_fields_to_japanese(vals, self.text_fields)
        return super(div_7_process, self).write(vals)
    def get_process(self):
        ans={}
        get_text(self.text_fields, ans, self)
        return ans
class div_7_rule(models.Model):
    _name = 'cms.div7.rule'
    _description = ''

    icon = fields.Image(string='Icon', max_width=100, max_height=100)
    icon_counter = fields.Integer(default=0)

    title = fields.Char(string='Tiêu đề')
    title_jp = fields.Char(string='Tiêu đề (JP)')
    title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")
    text = fields.Text(string='Text')
    text_jp = fields.Text(string='Text (JP)')
    text_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    div7_id = fields.Many2one('cms.div7', string='Rule', default=lambda self: self.env['cms.div_7'].search([]).id)

    text_fields = ['title', 'text']
    img = ['icon']

    @api.model
    def create(self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        res = super(div_7_rule, self).create(vals)
        save_img_sub_model('div7','rule',res.id,res.img,vals,res)
        return res

    def write(self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        save_img_sub_model('div7','rule',self.id,self.img,vals,self)
        return super(div_7_rule, self).write(vals)

    def unlink(self):
        for record in self:
            remove_img_sub_model('div7','rule',self.id)
        return super(div_7_rule, self).unlink()
    def get_rule(self):
        ans = {}
        get_text(self.text_fields, ans, self)
        get_img_path_sub_model(ans,'div7','rule',self.id,self.img,self)
        return ans

class clickable_image(models.Model):
    _name = 'cms.div7.image'
    _description = ''
    _rec_name = 'title'

    title = fields.Char(string='Title')
    title_jp = fields.Char(string='Title (JP)')
    title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")
    image = fields.Image(string='Image', max_width=200, max_height=200)
    image_counter = fields.Integer(default=0)
    div7_id = fields.Many2one('cms.div7', string='Clickable Image', default=lambda self: self.env['cms.div_7'].search([]).id)

    text_fields = ['title']
    img = ['image']

    @api.model
    def create(self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        res = super(clickable_image, self).create(vals)
        save_img_sub_model('div7','image',res.id,res.img,vals,res)
        return res

    def write(self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        save_img_sub_model('div7','image',self.id,self.img,vals,self)
        return super(clickable_image, self).write(vals)

    def unlink(self):
        for record in self:
            remove_img_sub_model('div7','image',record.id)
        return super(clickable_image, self).unlink()

    def get_image(self):
        ans={}
        get_text(self.text_fields, ans, self)
        get_img_path_sub_model(ans,'div7','image',self.id,self.img,self)
        return ans

