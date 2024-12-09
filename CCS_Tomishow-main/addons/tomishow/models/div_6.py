from odoo import models, fields, api, exceptions
import base64
from .util import *

class div_6(models.Model):
    _name = 'cms.div6'
    _description = ''
    name = fields.Char(default='Div 6')
    main_title = fields.Char(string='Tiêu đề chính')
    main_title_jp = fields.Char(string='Tiêu đề chính (JP)')
    main_title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")


    menu_item6 = fields.Char(string= "Menu Item 6")
    menu_item6_jp=fields.Char(string='Menu Items (JP)')
    menu_item6_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    people_ids = fields.One2many('cms.div6.people', 'div6_id', string='People')

    text_fields = ['main_title',"menu_item6"]

    @api.model
    def create(self, vals):
        """
            Ensure only one Div 6 is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Chỉ được tạo một Div 6')
        return super(div_6, self).create(vals)
    def write(self, vals):
        """
            Translate and save img
        """
        translate_fields_to_japanese(vals,self.text_fields)
        return super(div_6, self).write(vals)
    def get_people_web(self):
        peoples = self.env['cms.div6.people'].search([('div6_id', '=', self.id)])
        return [people.get_people() for people in peoples]

    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div6'].get_div_6())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }
    def write(self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        return super(div_6, self).write(vals)

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

        ans = {
            'people': div6.get_people_web()
        }
        get_text(self.text_fields, ans, div6)
        return ans

class div_6_people(models.Model):
    _name = 'cms.div6.people'
    _description = ''

    name = fields.Char(string='Tên')

    image = fields.Image(string='Hình ảnh', max_width=100, max_height=100)
    image_counter = fields.Integer(default=0)

    position = fields.Char(string='Chức vụ')
    position_jp = fields.Char(string='Chức vụ (JP)')
    position_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    text = fields.Text(string='Text')
    text_jp = fields.Text(string='Text (JP)')
    text_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")


    div6_id = fields.Many2one('cms.div6', string='People', default=lambda self: self.env['cms.div6'].search([]).id)

    text_fields = ['position', 'text']
    img = ['image']

    @api.model
    def create(self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        res = super(div_6_people, self).create(vals)
        save_img_sub_model('div6','people',res.id,res.img,vals,res)
        return res
    def write(self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        save_img_sub_model('div6','people',self.id,self.img,vals,self)
        return super(div_6_people, self).write(vals)

    def unlink(self):
        for record in self:
            remove_img_sub_model('div6','people',record.id)
        return super(div_6_people, self).unlink()

    def get_people(self):
        ans = {'name': self.name}
        get_text(self.text_fields, ans, self)
        get_img_path_sub_model(ans,'div6','people',self.id,self.img, self)
        return ans
