'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api, exceptions
import os, base64

class div_3(models.Model):
    _name = 'cms.div3'
    _description = ''
    name= fields.Char(default='Div 3')
    main_title = fields.Char(string='Tiêu đề chính')
    text = fields.Char(string="Text")
    icon_and_text = fields.One2many('cms.div3.iconandtext', 'div_3_id', string='Icon và Text')

    @api.model
    def create(self,vals):
        """
            Ensure that only one div_3 record is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Only one div 3 is allowed')
        else:
            return super(div_3, self).create(vals)




    def get_icon_and_text(self):
        """
            Get icon and text of div_3 into array of object
        :return: [
            {
                'icon'='icon/path',
                'text'='text'
            },...
        ]
        """
        icon_and_texts = self.env['cms.div3.iconandtext'].search([('div_3_id', '=', self.id)])

        return [icon_and_text.get_icon_and_text() for icon_and_text in icon_and_texts]

    @api.model
    def get_div_3(self):
        """
            Get div_3 data

        :return:
            json format of div_3
            {
                'main_title': main_title,
                'text': text,
                'icon_and_text': [
                    {
                        'icon': 'icon/path',
                        'text': text
                    }, ....
                ],
            }

        """
        div_3 = self.env['cms.div3'].search([])
        if not div_3:
            raise exceptions.ValidationError('Div 3 not found')

        div_3 = div_3[0]

        return {
            'main_title': div_3.main_title,
            'text': div_3.text,
            'icon_and_text': div_3.get_icon_and_text(),
            'text': div_3.text
        }


class div3_icon_and_text(models.Model):
    _name = 'cms.div3.iconandtext'
    _description = ''

    icon = fields.Image(string='Icon', max_width=100, max_height=100)
    text = fields.Char(string='Tiêu đề')


    div_3_id = fields.Many2one('cms.div3', string='Div 3', default = lambda self: self.env['cms.div3'].search([]).id)
    @api.model
    def create(self, vals):
        """
            Save the icon in the path folder if it is created
        :param vals:
        """
        icon_and_text = super(div3_icon_and_text, self).create(vals)

        if(icon_and_text.icon):
            icon = base64.b64encode(icon_and_text.icon)
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div3/icon_"+str(icon_and_text.id)+".png"

            with open(folder_path, 'wb') as f:
                f.write(icon)

        return icon_and_text
    def write(self,vals):
        """
            Save the icon in the path folder if it is changed
        """
        if vals.get('icon'):
            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div3/icon_"+str(self.id)+".png"
            with open(folder_path, 'wb') as f:
                f.write(base64.b64decode(vals['icon']))
        return super(div3_icon_and_text, self).write(vals)

    def unlink(self):
        """
            Delete the icon in the path folder if it is deleted
        """
        for record in self:

            folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div3/icon_"+str(record.id)+".png"
            #check if the file exists
            if os.path.exists(folder_path):
                os.remove(folder_path)
            import logging
            _logger = logging.getLogger(__name__)

            _logger.info('Deleted icon at' + folder_path + 'successfully')

        return super(div3_icon_and_text, self).unlink()

    def get_icon_and_text(self):
        """
            Get icon and text of div_3 into object
        """
        return {
            'icon': "tomishow/static/imgs/div3/"+"icon_"+str(self.id)+".png",
            'text': self.text
        }





