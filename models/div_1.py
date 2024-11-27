from odoo import models, fields, api, exceptions
import os
import base64
import requests
class div_1(models.Model):
    _name = 'cms.div1'
    _description = 'Div 1'

    name = fields.Char(default='Div 1')
    main_title = fields.Char(string='Tiêu đề chính')
    main_text = fields.Text(string='Text chính')

    left_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    left_title = fields.Char(string='Tiêu đề')
    left_text = fields.Text(string='Text')

    mid_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    mid_title = fields.Char(string='Tiêu đề')
    mid_text = fields.Text(string='Text')

    right_icon = fields.Image(string='Icon', max_width=100, max_height=100)
    right_title = fields.Char(string='Tiêu đề')
    right_text = fields.Text(string='Text')

    # Trường dữ liệu tiếng Nhật
    main_title_jp = fields.Char(string='Tiêu đề chính (JP)')
    main_text_jp = fields.Text(string='Text chính (JP)')

    left_title_jp = fields.Char(string='Tiêu đề (JP)')
    left_text_jp = fields.Text(string='Text (JP)')

    mid_title_jp = fields.Char(string='Tiêu đề (JP)')
    mid_text_jp = fields.Text(string='Text (JP)')

    right_title_jp = fields.Char(string='Tiêu đề (JP)')
    right_text_jp = fields.Text(string='Text (JP)')

    @api.model
    def create(self, vals):
        """
            Ensure that there is only one div 1 and translate data to Japanese
        """
        if self.search([]):
            raise exceptions.ValidationError('Không thể tạo thêm div 1')

        # Dịch nội dung sang tiếng Nhật
        translated_vals = self._translate_fields_to_japanese(vals)
        vals.update(translated_vals)
        return super(div_1, self).create(vals)

    def write(self, vals):
        """
            Translate data to Japanese on update
        """
        translated_vals = self._translate_fields_to_japanese(vals)
        vals.update(translated_vals)
        return super(div_1, self).write(vals)

    def _translate_fields_to_japanese(self, vals):
        """
            Translate specific fields to Japanese using MyMemory API
        """
        fields_to_translate = [
            'main_title', 'main_text',
            'left_title', 'left_text',
            'mid_title', 'mid_text',
            'right_title', 'right_text'
        ]

        # Mảng để lưu trữ các giá trị đã dịch
        translated_vals = {}

        for field in fields_to_translate:
            # Kiểm tra nếu trường tiếng Nhật đã có giá trị trong `vals`
            jp_field = f'{field}_jp'

            # Nếu trường tiếng Nhật đã có giá trị, không dịch mà giữ nguyên giá trị hiện tại
            if jp_field in vals and vals[jp_field]:
                translated_vals[jp_field] = vals[jp_field]
            # Nếu trường tiếng Nhật chưa có giá trị, thực hiện dịch
            elif field in vals and vals[field]:
                translated_vals[jp_field] = self._translate_text(vals[field])

        return translated_vals

    def _translate_text(self, text):
        """
            Translate text to Japanese using MyMemory API
        """
        try:
            api_url = "https://api.mymemory.translated.net/get"
            params = {
                'q': text,
                'langpair': 'vi|ja'  # Dịch từ tiếng Việt sang tiếng Nhật
            }
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data.get('responseData', {}).get('translatedText', text)
            else:
                return text  # Trả về text gốc nếu lỗi
        except Exception as e:
            return text  # Trả về text gốc nếu có lỗi

    def test(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info(self.env['cms.div1'].get_div_1())


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

        # Chuyển đổi các icon sang dạng base64 nếu có
        def convert_to_base64(image):
            return base64.b64encode(image).decode('utf-8') if image else None

        return {
            'main_title': div_1.main_title,
            'main_text': div_1.main_text,
            'main_title_jp': div_1.main_title_jp,
            'main_text_jp': div_1.main_text_jp,
            'left_icon': convert_to_base64(div_1.left_icon),
            'left_title': div_1.left_title,
            'left_text': div_1.left_text,
            'left_title_jp': div_1.left_title_jp,
            'left_text_jp': div_1.left_text_jp,
            'mid_icon': convert_to_base64(div_1.mid_icon),
            'mid_title': div_1.mid_title,
            'mid_text': div_1.mid_text,
            'mid_title_jp': div_1.mid_title_jp,
            'mid_text_jp': div_1.mid_text_jp,
            'right_icon': convert_to_base64(div_1.right_icon),
            'right_title': div_1.right_title,
            'right_text': div_1.right_text,
            'right_title_jp': div_1.right_title_jp,
            'right_text_jp': div_1.right_text_jp
        }
