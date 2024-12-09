'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api, exceptions
from .util import *



class div_2(models.Model):
    _name = 'cms.div2'
    _description = ''

    name=fields.Char(default='Div 2')

    menu_item2 = fields.Char(string= "Menu Item 2")
    menu_item2_jp=fields.Char(string='Menu Items (JP)')
    menu_item2_jp_toggle = fields.Boolean(string='JP' ,computed="lambda x: False")



    main_title = fields.Char(string='Tiêu đề chính')
    main_title_jp = fields.Char(string='Tiêu đề chính (JP)')
    main_title_jp_toggle = fields.Boolean(string='JP')

    main_text = fields.Text(string='Text chính')
    main_text_jp = fields.Text(string='Text chính (JP)')
    main_text_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    ##################################################
    ##                                              ##
    ##                                              ##
    ##                    Title                     ##
    ##                                              ##
    ##                                              ##
    ##################################################

    ##############################
    ##                          ##
    ##         Title 1          ##
    ##                          ##
    ##############################
    title_1 = fields.Char(string='Tiêu đề')
    title_1_jp=fields.Char(string='Tiêu đề (JP)')
    title_1_jp_toggle=fields.Boolean(string='JP',computed="lambda x: False")

    text_1 = fields.Text(string='Text')
    text_1_jp=fields.Text(string='Text (JP)')
    text_1_jp_toggle=fields.Boolean(string='JP',computed="lambda x: False")

    ##############################
    ##                          ##
    ##         Title 2          ##
    ##                          ##
    ##############################
    title_2 = fields.Char(string='Tiêu đề')
    title_2_jp=fields.Char(string='Tiêu đề (JP)')
    title_2_jp_toggle=fields.Boolean(string='JP',computed="lambda x: False")

    text_2 = fields.Text(string='Text')
    text_2_jp=fields.Text(string='Text (JP)')
    text_2_jp_toggle=fields.Boolean(string='JP',computed="lambda x: False")

    ##############################
    ##                          ##
    ##         Title 3          ##
    ##                          ##
    ##############################
    title_3 = fields.Char(string='Tiêu đề')
    title_3_jp=fields.Char(string='Tiêu đề (JP)')
    title_3_jp_toggle=fields.Boolean(string='JP',computed="lambda x: False")

    text_3 = fields.Text(string='Text')
    text_3_jp=fields.Text(string='Text (JP)')
    text_3_jp_toggle=fields.Boolean(string='JP',computed="lambda x: False")

    ##############################
    ##                          ##
    ##         Title 4          ##
    ##                          ##
    ##############################
    title_4 = fields.Char(string='Tiêu đề')
    title_4_jp=fields.Char(string='Tiêu đề (JP)')
    title_4_jp_toggle=fields.Boolean(string='JP',computed="lambda x: False")

    text_4 = fields.Text(string='Text')
    text_4_jp=fields.Text(string='Text (JP)')
    text_4_jp_toggle=fields.Boolean(string='JP',computed="lambda x: False")

    ##################################################
    ##                                              ##
    ##                                              ##
    ##                  Flipboard                   ##
    ##                                              ##
    ##                                              ##
    ##################################################
    ##############################
    ##                          ##
    ##       Flipboard 1        ##
    ##                          ##
    ##############################
    flip_board_1_title_not_flipped = fields.Char(string='Tiêu đề chưa lật')
    flip_board_1_title_not_flipped_jp = fields.Char(string='Tiêu đề chưa lật (JP)')
    flip_board_1_title_not_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_1_text_not_flipped = fields.Char(string='Text đã lật')
    flip_board_1_text_not_flipped_jp = fields.Char(string='Text đã lật (JP)')
    flip_board_1_text_not_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_1_title_flipped = fields.Char(string='Tiêu đề đã lật')
    flip_board_1_title_flipped_jp = fields.Char(string='Tiêu đề đã lật (JP)')
    flip_board_1_title_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_1_text_flipped = fields.Char(string='Text đã lật')
    flip_board_1_text_flipped_jp = fields.Char(string='Text đã lật (JP)')
    flip_board_1_text_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_1_background_image = fields.Binary(string='Background')
    flip_board_1_background_image_counter=fields.Integer()

    ##############################
    ##                          ##
    ##       Flipboard 2        ##
    ##                          ##
    ##############################
    flip_board_2_title_not_flipped = fields.Char(string='Tiêu đề chưa lật')
    flip_board_2_title_not_flipped_jp = fields.Char(string='Tiêu đề chưa lật (JP)')
    flip_board_2_title_not_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_2_text_not_flipped = fields.Char(string='Text đã lật')
    flip_board_2_text_not_flipped_jp = fields.Char(string='Text đã lật (JP)')
    flip_board_2_text_not_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_2_title_flipped = fields.Char(string='Tiêu đề đã lật')
    flip_board_2_title_flipped_jp = fields.Char(string='Tiêu đề đã lật (JP)')
    flip_board_2_title_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_2_text_flipped = fields.Char(string='Text đã lật')
    flip_board_2_text_flipped_jp = fields.Char(string='Text đã lật (JP)')
    flip_board_2_text_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_2_background_image = fields.Binary(string='Background')
    flip_board_2_background_image_counter=fields.Integer()

    ##############################
    ##                          ##
    ##       Flipboard 3        ##
    ##                          ##
    ##############################
    flip_board_3_title_not_flipped = fields.Char(string='Tiêu đề chưa lật')
    flip_board_3_title_not_flipped_jp = fields.Char(string='Tiêu đề chưa lật (JP)')
    flip_board_3_title_not_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_3_text_not_flipped = fields.Char(string='Text đã lật')
    flip_board_3_text_not_flipped_jp = fields.Char(string='Text đã lật (JP)')
    flip_board_3_text_not_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_3_title_flipped = fields.Char(string='Tiêu đề đã lật')
    flip_board_3_title_flipped_jp = fields.Char(string='Tiêu đề đã lật (JP)')
    flip_board_3_title_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_3_text_flipped = fields.Char(string='Text đã lật')
    flip_board_3_text_flipped_jp = fields.Char(string='Text đã lật (JP)')
    flip_board_3_text_flipped_jp_toggle = fields.Boolean(string='JP',computed="lambda x: False")

    flip_board_3_background_image = fields.Binary(string='Background')
    flip_board_3_background_image_counter=fields.Integer()

    img = ['flip_board_1_background_image', 'flip_board_2_background_image', 'flip_board_3_background_image']
    text_fields = ['main_title', 'main_text',
            'title_1', 'text_1',
            'title_2', 'text_2',
            'title_3', 'text_3',
            'title_4', 'text_4',"menu_item2",
            'flip_board_1_title_not_flipped', 'flip_board_1_text_not_flipped', 'flip_board_1_title_flipped', 'flip_board_1_text_flipped',
            'flip_board_2_title_not_flipped', 'flip_board_2_text_not_flipped', 'flip_board_2_title_flipped', 'flip_board_2_text_flipped',
            'flip_board_3_title_not_flipped', 'flip_board_3_text_not_flipped', 'flip_board_3_title_flipped', 'flip_board_3_text_flipped'
            ]


    def Preview(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div2'].get_div_2())
    def go_to_website(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',  
            'target': 'new',  # Mở trong tab mới
        }
    @api.model
    def create(self, vals):
        """
            Ensure that only one div_2 record is created
        """
        if self.search([]):
            raise exceptions.ValidationError('Record already exists')
        return super(div_2, self).create(vals)




    def write(self,vals):
        """
            Save img and translate fields
        """
        save_img('div2',self.img,vals,self)
        translate_fields_to_japanese(vals,self.text_fields)
        return super(div_2, self).write(vals)


    def get_flip_board(self):
        """
            Get flip_board data
        :return: [
            {
                'text_not_flipped': text_not_flipped,
                'text_flipped': text_flipped,
                'background_image': background_image

            }, ...
        ]
        """
        img = ['flip_board_1_background_image', 'flip_board_2_background_image', 'flip_board_3_background_image']
        img_path = {}
        get_img_path(img_path, 'div2', img, self)
        flip_board = []
        # flip_board_1
        flip_board.append({
            'title_not_flipped': self.flip_board_1_title_not_flipped,
            'title_not_flipped_jp': self.flip_board_1_title_not_flipped_jp,
            'text_not_flipped': self.flip_board_1_text_not_flipped,
            'text_not_flipped_jp': self.flip_board_1_text_not_flipped_jp,
            'title_flipped': self.flip_board_1_title_flipped,
            'title_flipped_jp': self.flip_board_1_title_flipped_jp,
            'text_flipped': self.flip_board_1_text_flipped,
            'text_flipped_jp': self.flip_board_1_text_flipped_jp,
            'background_image': img_path['flip_board_1_background_image']
        })
        #flip_board_2
        flip_board.append({
            'title_not_flipped': self.flip_board_2_title_not_flipped,
            'title_not_flipped_jp': self.flip_board_2_title_not_flipped_jp,
            'text_not_flipped': self.flip_board_2_text_not_flipped,
            'text_not_flipped_jp': self.flip_board_2_text_not_flipped_jp,
            'title_flipped': self.flip_board_2_title_flipped,
            'title_flipped_jp': self.flip_board_2_title_flipped_jp,
            'text_flipped': self.flip_board_2_text_flipped,
            'text_flipped_jp': self.flip_board_2_text_flipped_jp,
            'background_image': img_path['flip_board_2_background_image']
        })

        #flip_board_3
        flip_board.append({
            'title_not_flipped': self.flip_board_3_title_not_flipped,
            'title_not_flipped_jp': self.flip_board_3_title_not_flipped_jp,
            'text_not_flipped': self.flip_board_3_text_not_flipped,
            'text_not_flipped_jp': self.flip_board_3_text_not_flipped_jp,
            'title_flipped': self.flip_board_3_title_flipped,
            'title_flipped_jp': self.flip_board_3_title_flipped_jp,
            'text_flipped': self.flip_board_3_text_flipped,
            'text_flipped_jp': self.flip_board_3_text_flipped_jp,
            'background_image': img_path['flip_board_3_background_image']
        })
        return flip_board

    @api.model
    def get_div_2(self):
        """
            Get div_2 data

        :param self: object
        :return:
            json format of div_2
            {
                'main_title': main_title,
                'main_text': main_text,
                'title_1': title_1,
                'text_1': text_1,
                'title_2': title_2,
                'text_2': text_2,
                'title_3': title_3,
                'text_3': text_3,
                'title_4': title_4,
                'text_4': text_4,
                'flip_board': flip_board
            }
        """

        div_2 = self.env['cms.div2'].search([])
        if not div_2:
            raise exceptions.ValidationError("Không có dữ liệu")

        div_2 = div_2[0]

        ans = {'flip_board': div_2.get_flip_board()}
        get_text(['main_title', 'main_text',
                            'title_1', 'text_1',
                            'title_2', 'text_2',
                            'title_3', 'text_3',
                            'title_4', 'text_4'],ans, div_2)
        return ans
