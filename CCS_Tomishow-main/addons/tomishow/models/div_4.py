from odoo import models, fields, api, exceptions
import base64
from .util import *

class div_4(models.Model):
    _name = 'cms.div4'
    _description = ''


    menu_item4 = fields.Char(string= "Menu Item 4")
    menu_item4_jp=fields.Char(string='Menu Items (JP)')
    menu_item4_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")

    name = fields.Char(default='Div 4')
    main_title = fields.Char(string='Tiêu đề chính')
    main_title_jp = fields.Char(string='Tiêu đề chính (JP)')
    main_title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")
    project_ids = fields.One2many('cms.div4.project', 'div4_id', string='Projects')

    text_fields = ['main_title',"menu_item4"]
    @api.model
    def create(self, vals):
        """
            Ensure only one Div 4 is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Chỉ được tạo một Div 4')
        return super(div_4, self).create(vals)

    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div4'].get_div_4())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }
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

        ans ={'projects': div4.get_project_web()}
        get_text(self.text_fields, ans, div4)
        return ans



class div_4_project(models.Model):
    _name = 'cms.div4.project'
    _description = ''

    title = fields.Char(string='Tiêu đề')
    title_jp = fields.Char(string='Tiêu đề (JP)')
    title_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    small_text = fields.Text(string='Text')
    small_text_jp = fields.Text(string='Text (JP)')
    small_text_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    image = fields.Image(string='Hình ảnh', max_width=800, max_height=400)
    text = fields.Html(string='Bài viết')
    text_jp = fields.Html(string='Bài viết (JP)')
    text_jp_toggle = fields.Boolean(string='JP', computed="lambda x: False")

    div4_id = fields.Many2one('cms.div4', string='Project', default=lambda self: self.env['cms.div4'].search([]).id)
    text_fields = ['title', 'small_text', 'text']
    img = ['image']

    @api.model
    def create(self,vals):
        translate_fields_to_japanese(vals,self.text_fields)
        res = super(div_4_project, self).create(vals)
        save_img_sub_model('div4','project',res.id,res.img,vals,res)
        return res

    def write(self, vals):
        """
        translate and save img
        """
        translate_fields_to_japanese(vals,self.text_fields)
        save_img_sub_model('div4','project',self.id,self.img,vals,self)
        return super(div_4_project, self).write(vals)

    def unlink(self):
        for record in self:
            remove_img_sub_model('div4','project',int(record.id))
        return super(div_4_project, self).unlink()

    def get_project_for_web(self):
        """
        Returns project data in a format suitable for web display.
        Converts image to base64 encoding if present.
        """

        ans = {
            'id': self.id

        }
        get_text(['title', 'small_text','text'], ans, self)
        get_img_path_sub_model(ans, 'div4', 'project', self.id, self.img, self)
        return ans