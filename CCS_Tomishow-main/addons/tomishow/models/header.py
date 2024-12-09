'''
Author: Thinh dep trai
Model Description: 
'''
import os
from odoo import models, fields, api, exceptions
import base64
from .util import translate_fields_to_japanese,save_img,get_img_path,get_text
class header(models.Model):
    _name = 'cms.header'
    _description = 'CMS model for header'

    name = fields.Char(default='Header')

    logo = fields.Image(string='Logo', max_width=100, max_height=100)
    logo_counter=fields.Integer(default=0)

    ##############################
    ##                          ##
    ## Logo left and right text ##
    ##                          ##
    ##############################

    logo_left_text = fields.Char(string='Text bên trái Logo')
    logo_right_text = fields.Char(string='Text bên phải Logo')
    logo_left_text_jp_toggle=fields.Boolean(string="JP" ,computed="lambda x: False")

    logo_left_text_jp = fields.Char(string='Text bên trái Logo (JP)')
    logo_right_text_jp_toggle=fields.Boolean(string="JP" ,computed="lambda x: False")
    logo_right_text_jp = fields.Char(string='Text bên phải Logo (JP)')

    ##################################################
    ##                                              ##
    ##                                              ##
    ##          Big title and Small title           ##
    ##                                              ##
    ##                                              ##
    ##################################################

    big_title = fields.Char(string='Title đề chính')
    big_title_jp = fields.Char(string='Title đề chính (JP)')
    big_title_jp_toggle=fields.Boolean(string="JP" ,computed="lambda x: False")

    small_title = fields.Char(string='Slogan')
    small_title_jp = fields.Char(string='Slogan (JP)')
    small_title_jp_toggle=fields.Boolean(string="JP" ,computed="lambda x: False")


    phone_number = fields.Char(string='Số điện thoại')


    back_ground = fields.Image(string='Background', max_width=1000, max_height=600)
    back_ground_counter = fields.Integer(default=0)

    text_fields = ['logo_left_text','logo_right_text','big_title','small_title']
    img=['logo','back_ground']
    preview_toggle = fields.Boolean(default=False)

    def preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        ans={}
        get_img_path(ans,'header',self.img,self)
        get_text(self.text_fields,ans,self)
        _logger.info(self.env['cms.header'].get_header())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }
    def test(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info();

    @api.model
    def create(self, vals):
        if self.search([]):
            raise Exception("Đã có header rồi")
        return super(header, self).create(vals)



    def write(self, vals):

        #save image
        save_img("header",self.img,vals,self)
        translate_fields_to_japanese(vals,self.text_fields)
        return super(header, self).write(vals)

    @api.model
    def get_header(self):
        """
        Get the header data for web
        :return: dict
            {
                'logo': 'logo/path',
                'logo_left_text': logo_left_text,
                'logo_right_text': logo_right_text,
                'big_title': big_title,
                'small_title': small_title,
                'phone_number': phone_number,
                'back_ground': 'back_ground/path'
            }
        """

        header = self.search([])[0]
        if not header:
            raise exceptions.ValidationError('Không có header')
        ans = {}
        get_img_path(ans,'header',self.img,header);
        get_text(self.text_fields,ans,header)

        return ans;
