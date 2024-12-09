'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api, exceptions
from .util import *
import base64

class footer(models.Model):
    _name = 'cms.footer'
    _description = 'CMS for footer'

    footer_text1 = fields.Text(string= "Footer Text 1")
    footer_text1_jp=fields.Text(string='Footer Text 1 (JP)')
    footer_text1_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")
    footer_text2 = fields.Text(string= "Footer Text 2")
    footer_text2_jp=fields.Text(string='Footer Text 2 (JP)')
    footer_text2_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    working_time = fields.Text(string= "Working Time")
    working_time_jp=fields.Text(string='Working Time (JP)')
    working_time_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")
    working_time_text = fields.Text(string= "Working Time Text")
    working_time_text_jp=fields.Text(string='Working Time Text (JP)')
    working_time_text_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    callus = fields.Char(string= "Call Us")
    callus_jp=fields.Char(string='Call Us (JP)')
    callus_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")
    callus_text = fields.Text(string= "Call Us text")
    callus_text_jp=fields.Text(string='Call Us text (JP)')
    callus_text_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    address = fields.Char(string= "address")
    address_jp=fields.Char(string='address (JP)')
    address_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")
    address_text = fields.Text(string= "address text")
    address_text_jp=fields.Text(string='address text (JP)')
    address_text_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    mail = fields.Char(string= "mail")
    mail_jp=fields.Char(string='mail (JP)')
    mail_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")
    mail_text = fields.Text(string= "mail text")
    mail_text_jp=fields.Text(string='mail text (JP)')
    mail_text_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")
   

    copyright = fields.Char(string='copyright')
    copyright_jp=fields.Char(string='copyright (JP)')
    copyright_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")
    
    footer_logo = fields.Image(string='Hình ảnh')

    logo = fields.One2many('cms.footer.logo', 'logo_id', string='Social Logo')
    

    
    text_fields = ['working_time_text','working_time','callus', 'address', 'mail',"copyright",'callus_text', 'address_text', 'mail_text','footer_text1','footer_text2']
    img=['footer_logo']

    @api.model
    def create(self, vals):
        """
        Ensure that only one footer record is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Only one footer is allowed')
        else:
            return super(footer, self).create(vals)

    def write(self, vals):
        """
        Translate and save img
        """
        translate_fields_to_japanese(vals,self.text_fields)
        save_img('footer',self.img,vals,self)
        return super(footer, self).write(vals)
    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.footer'].get_footer())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }

    def get_logo(self):
        """
        Get icon and text of footer into array of objects
        :return: [
            {
                'icon': 'base64string',
                'text': 'text'
            }, ...
        ]
        """
        logos = self.env['cms.footer.logo'].search([('logo_id', '=', self.id)])
        return [logo.get_logo() for logo in logos]

    @api.model
    def get_footer(self):
        """
        Get footer data

        :return:
            JSON format of footer
            {
                'main_title': main_title,
                'text': text,
                'logo': [
                    {
                        'icon': 'base64string',
                        'text': text
                    }, ...
                ],
            }

        """
        footer = self.env['cms.footer'].search([])
        if not footer:
            raise exceptions.ValidationError('footer not found')
        
        footer = footer[0]

        ans = {
            'logo': footer.get_logo()
        }
        get_img_path(ans,'footer',self.img,footer)
        get_text(footer.text_fields, ans, footer)
        return ans

class Footer_Social_logo(models.Model):
    _name = 'cms.footer.logo'
    _description = ''

    icon = fields.Image(string='Icon', max_width=100, max_height=100)
    link = fields.Char(string= "Link")

    logo_id = fields.Many2one('cms.footer', string='Footer', default=lambda self: self.env['cms.footer'].search([]).id)

    img = ['icon']

    @api.model
    def create(self, vals):
        res = super(Footer_Social_logo, self).create(vals)
        save_img_sub_model("footer",'logo',res.id,res.img,vals,res)
        return res


    def write(self, vals):
        """
        translate and save img
        """
        save_img_sub_model("footer",'logo',self.id,self.img,vals,self)
        return super(Footer_Social_logo, self).write(vals)

    def unlink(self):
        """
        Remove image from static/imgs/footer/logo
        """
        for record in self:
            remove_img_sub_model('footer','logo',int(record.id))
        return super(Footer_Social_logo, self).unlink()
    def get_logo(self):
        """
        Get icon and text of footer into object
        """
        ans = {}
        get_img_path_sub_model(ans,'footer','logo',self.id,self.img,self)
        return ans

