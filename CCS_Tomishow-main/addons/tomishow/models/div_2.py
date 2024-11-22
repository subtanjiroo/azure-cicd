'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api, exceptions
import os, base64



class div_2(models.Model):
    _name = 'cms.div2'
    _description = ''

    name=fields.Char(default='Div 2')

    main_title = fields.Char(string='Tiêu đề chính')
    main_text = fields.Text(string='Text chính')

    title_1 = fields.Char(string='Tiêu đề')
    text_1 = fields.Text(string='Text')

    title_2 = fields.Char(string='Tiêu đề')
    text_2 = fields.Text(string='Text')

    title_3 = fields.Char(string='Tiêu đề')
    text_3 = fields.Text(string='Text')

    title_4 = fields.Char(string='Tiêu đề')
    text_4 = fields.Text(string='Text')


    flip_board_1_title_not_flipped = fields.Char(string='Tiêu đề chưa lật')
    flip_board_1_text_not_flipped = fields.Char(string='Text chưa lật')
    flip_board_1_title_flipped = fields.Char(string='Tiêu đề đã lật')
    flip_board_1_text_flipped = fields.Char(string='Text chưa lật')
    flip_board_1_background_image = fields.Binary(string='Background')

    flip_board_2_title_not_flipped = fields.Char(string='Tiêu đề chưa lật')
    flip_board_2_text_not_flipped = fields.Char(string='Text chưa lật')
    flip_board_2_title_flipped = fields.Char(string='Tiêu đề đã lật')
    flip_board_2_text_flipped = fields.Char(string='Text chưa lật')
    flip_board_2_background_image = fields.Binary(string='Background')

    flip_board_3_title_not_flipped = fields.Char(string='Tiêu đề chưa lật')
    flip_board_3_text_not_flipped = fields.Char(string='Text chưa lật')
    flip_board_3_title_flipped = fields.Char(string='Tiêu đề đã lật')
    flip_board_3_text_flipped = fields.Char(string='Text chưa lật')
    flip_board_3_background_image = fields.Binary(string='Background')




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
            save the all the flipboard path in the path folder if they changed

        """


        folder_path = os.path.dirname(os.path.dirname(__file__))+"/static/imgs/div2"
        flip_board_1_background_image_path = folder_path + "/flip_board_1_background_image.png"
        flip_board_2_background_image_path = folder_path + "/flip_board_2_background_image.png"
        flip_board_3_background_image_path = folder_path + "/flip_board_3_background_image.png"



        if vals.get('flip_board_1_background_image'):
            byte = base64.b64decode(vals['flip_board_1_background_image'])
            with open(flip_board_1_background_image_path, 'wb') as f:
                f.write(byte)
        if vals.get('flip_board_2_background_image'):
            byte = base64.b64decode(vals['flip_board_2_background_image'])
            with open(flip_board_2_background_image_path, 'wb') as f:
                f.write(byte)
        if vals.get('flip_board_3_background_image'):
            byte = base64.b64decode(vals['flip_board_2_background_image'])
            with open(flip_board_3_background_image_path, 'wb') as f:
                f.write(byte)


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

        flip_board=[]

        folder_path = "tomishow/static/imgs/div2"
        flip_board_1_background_image_path = folder_path + "/flip_board_1_background_image.png"
        flip_board_2_background_image_path = folder_path + "/flip_board_2_background_image.png"
        flip_board_3_background_image_path = folder_path + "/flip_board_3_background_image.png"
        # flip_board_1
        flip_board.append({
            'title_not_flipped': self.flip_board_1_title_not_flipped,
            'text_not_flipped': self.flip_board_1_text_not_flipped,
            'title_flipped': self.flip_board_1_title_flipped,
            'text_flipped': self.flip_board_1_text_flipped,
            'background_image': flip_board_1_background_image_path
        })
        #flip_board_2
        flip_board.append({
            'title_not_flipped': self.flip_board_2_title_not_flipped,
            'text_not_flipped': self.flip_board_2_text_not_flipped,
            'title_flipped': self.flip_board_2_title_flipped,
            'text_flipped': self.flip_board_2_text_flipped,
            'background_image': flip_board_2_background_image_path
        })

        #flip_board_3
        flip_board.append({
            'title_not_flipped': self.flip_board_3_title_not_flipped,
            'text_not_flipped': self.flip_board_3_text_not_flipped,
            'title_flipped': self.flip_board_3_title_flipped,
            'text_flipped': self.flip_board_3_text_flipped,
            'background_image': flip_board_3_background_image_path
        })
        return flip_board


    def test(self):
        import logging
        _logger=logging.getLogger(__name__)
        _logger.info(self.env['cms.div2'].get_div_2())

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

        return {
            'main_title': div_2.main_title,
            'main_text': div_2.main_text,
            'title_1': div_2.title_1,
            'text_1': div_2.text_1,
            'title_2': div_2.title_2,
            'text_2': div_2.text_2,
            'title_3': div_2.title_3,
            'text_3': div_2.text_3,
            'title_4': div_2.title_4,
            'text_4': div_2.text_4,
            'flip_board': div_2.get_flip_board()
        }