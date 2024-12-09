from odoo import models, fields, api, exceptions
import os
import base64
from .util import *
class div_1(models.Model):
    _name = 'cms.div1'
    _description = ''

    name = fields.Char(default='Div 1')

    main_title = fields.Char(string='Tiêu đề chính' )
    main_title_jp=fields.Char(string='Tiêu đề chính (JP)')
    main_title_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    menu_item1 = fields.Char(string= "Menu Item 1")
    menu_item1_jp=fields.Char(string='Menu Items (JP)')
    menu_item1_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")


    main_text = fields.Text(string='Text chính')
    main_text_jp = fields.Text(string='Text chính (JP)')
    main_text_jp_toggle = fields.Boolean(string="JP" ,computed="lambda x: False")

    left_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    left_icon_counter=fields.Integer()

    left_title = fields.Char(string='Tiêu đề')
    left_title_jp = fields.Char(string='Tiêu đề (JP)')
    left_title_jp_toggle = fields.Boolean(string="JP" ,computed="lambda x: False")

    left_text = fields.Text(string='Text')
    left_text_jp = fields.Text(string='Text (JP)')
    left_text_jp_toggle = fields.Boolean(string="JP" ,computed="lambda x: False")

    mid_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    mid_icon_counter=fields.Integer()
    mid_title = fields.Char(string='Tiêu đề')
    mid_title_jp = fields.Char(string='Tiêu đề (JP)')
    mid_title_jp_toggle = fields.Boolean(string="JP" ,computed="lambda x: False")
    mid_text = fields.Text(string='Text')
    mid_text_jp = fields.Text(string='Text (JP)')
    mid_text_jp_toggle = fields.Boolean(string="JP" ,computed="lambda x: False")

    right_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    right_icon_counter=fields.Integer()
    right_title = fields.Char(string='Tiêu đề')
    right_title_jp = fields.Char(string='Tiêu đề (JP)')
    right_title_jp_toggle = fields.Boolean(string="JP" ,computed="lambda x: False")
    right_text = fields.Text(string='Text')
    right_text_jp = fields.Text(string="JP" ,computed="lambda x: False")
    right_text_jp_toggle = fields.Boolean(string='Toggle JP')

    
    text_fields = ['main_title','main_text','left_title','left_text','mid_title','mid_text','right_title','right_text','menu_item1']
    img=['left_icon','mid_icon','right_icon']
    @api.model
    def create(self,vals):
        """
            Ensure that there is only one div 1
        """
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm div 1')
        else:
            return super(div_1, self).create(vals)

    def write(self, vals):
        """
            save img and translate fields
        """
        save_img('div1',self.img,vals,self)
        translate_fields_to_japanese(vals,self.text_fields)
        return super(div_1, self).write(vals)




    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div1'].get_div_1())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }

    @api.model
    def get_div_1(self):
        """
            Get div_1 data

        :param self: object
        :return:
            json format of div_1
            {
                'main_title': main_title,
                'main_text': main_text,
                'left_icon': left_icon,
                'left_title': left_title,
                'left_text': left_text,
                'mid_icon': mid_icon,
                'mid_title': mid_title,
                'mid_text': mid_text,
                'right_icon': right_icon,
                'right_title': right_title,
                'right_text': right
            }
        """

        div_1 = self.env['cms.div1'].search([])
        if not div_1:
            raise exceptions.ValidationError("Không có dữ liệu")

        ans = {}
        get_img_path(ans,'div1',self.img,div_1)
        get_text(self.text_fields,ans,div_1)
        return ans
