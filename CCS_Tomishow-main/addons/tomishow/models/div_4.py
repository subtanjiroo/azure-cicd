'''
Author: Thinh dep trai
Model Description: 
'''
import base64
import os

from odoo import models, fields, api, exceptions


class div_4(models.Model):
    _name = 'cms.div4'
    _description = ''

    name= fields.Char(default='Div 4')
    main_title = fields.Char(string='Tiêu đề chính')
    project_ids= fields.One2many('cms.div4.project', 'div4_id', string='Projects')

    @api.model
    def create(self,vals):
        """
            Ensure only one Div 4 is created

        """
        if self.search([]):
            raise exceptions.ValidationError('Chỉ được tạo một Div 4')
        return super(div_4, self).create(vals)


    def get_project_web(self):
        projects = self.env['cms.div4.project'].search([('div4_id', '=', self.id)])
        project_list = []
        for project in projects:
            project_list.append({
                'title': project.title,
                'small_text': project.small_text,
                'image': "tomishow/static/imgs/div4/project_"+str(project.id)+".png"

            })
        return project_list





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


        return{
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

    div4_id = fields.Many2one('cms.div4', string='Project', default = lambda self: self.env['cms.div_4'].search([]).id)

    @api.model
    def create(self,vals):
        project = super(div_4_project, self).create(vals)

        if project.image:
            image = base64.b64decode(project.image)
            folder_path= os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div4/project_"+str(project.id)+".png"
            with open(folder_path, 'wb') as f:
                f.write(image)
        return project

    def unlink(self):
        for project in self:
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div4/project_"+str(project.id)+".png"
            if os.path.exists(folder_path):
                os.remove(folder_path)
        return super(div_4_project, self).unlink()

    def write(self,vals):
        if vals.get('image'):
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div4/project_"+str(self.id)+".png"
            with open(folder_path, 'wb') as f:
                f.write(base64.b64decode(vals['image']))
        return super(div_4_project, self).write(vals)




