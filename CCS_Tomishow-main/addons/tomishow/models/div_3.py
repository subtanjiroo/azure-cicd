'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api, exceptions
from .util import *

class div_3(models.Model):
    _name = 'cms.div3'
    _description = ''


    menu_item3 = fields.Char(string= "Menu Item 3")
    menu_item3_jp=fields.Char(string='Menu Items (JP)')
    menu_item3_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    name = fields.Char(default='Div 3')

    main_title = fields.Char(string='Tiêu đề chính')
    main_title_jp = fields.Char(string='Tiêu đề chính (JP)')
    main_title_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    text = fields.Char(string="Text")
    text_jp = fields.Char(string="Text (JP)")
    text_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    icon_and_text = fields.One2many('cms.div3.iconandtext', 'div_3_id', string='Icon và Text')

    text_fields= ['main_title', 'text',"menu_item3"]

    @api.model
    def create(self, vals):
        """
        Ensure that only one div_3 record is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Only one div 3 is allowed')
        else:
            return super(div_3, self).create(vals)

    def write(self, vals):
        """
        Translate and save img
        """
        translate_fields_to_japanese(vals,self.text_fields)

        return super(div_3, self).write(vals)
    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div3'].get_div_3())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }

    def get_icon_and_text(self):
        """
        Get icon and text of div_3 into array of objects
        :return: [
            {
                'icon': 'base64string',
                'text': 'text'
            }, ...
        ]
        """
        icon_and_texts = self.env['cms.div3.iconandtext'].search([('div_3_id', '=', self.id)])
        return [icon_and_text.get_icon_and_text() for icon_and_text in icon_and_texts]

    @api.model
    def get_div_3(self):
        """
        Get div_3 data

        :return:
            JSON format of div_3
            {
                'main_title': main_title,
                'text': text,
                'icon_and_text': [
                    {
                        'icon': 'base64string',
                        'text': text
                    }, ...
                ],
            }

        """
        div_3 = self.env['cms.div3'].search([])
        if not div_3:
            raise exceptions.ValidationError('Div 3 not found')

        div_3 = div_3[0]

        ans = {
            'icon_and_text': div_3.get_icon_and_text()
        }
        get_text(div_3.text_fields, ans, div_3)
        return ans


class div3_icon_and_text(models.Model):
    _name = 'cms.div3.iconandtext'
    _description = ''

    icon = fields.Image(string='Icon', max_width=100, max_height=100)
    text = fields.Char(string='Tiêu đề')
    text_jp = fields.Char(string='Tiêu đề (JP)')
    text_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    div_3_id = fields.Many2one('cms.div3', string='Div 3', default=lambda self: self.env['cms.div3'].search([]).id)

    text_fields = ['text']
    img = ['icon']

    @api.model
    def create(self, vals):
        translate_fields_to_japanese(vals,self.text_fields)
        res = super(div3_icon_and_text, self).create(vals)
        save_img_sub_model("div3",'iconandtext',res.id,res.img,vals,res)
        return res


    def write(self, vals):
        """
        translate and save img
        """
        save_img_sub_model("div3",'iconandtext',self.id,self.img,vals,self)
        translate_fields_to_japanese(vals,self.text_fields)
        return super(div3_icon_and_text, self).write(vals)

    def unlink(self):
        """
        Remove image from static/imgs/div3/iconandtext
        """
        for record in self:
            remove_img_sub_model('div3','iconandtext',int(record.id))
        return super(div3_icon_and_text, self).unlink()
    def get_icon_and_text(self):
        """
        Get icon and text of div_3 into object
        """
        ans = {}
        get_text(self.text_fields,ans, self)
        get_img_path_sub_model(ans,'div3','iconandtext',self.id,self.img,self)
        return ans






