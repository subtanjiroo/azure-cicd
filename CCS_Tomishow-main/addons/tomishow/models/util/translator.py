
import requests

def translate_fields_to_japanese(vals,fields_to_translate):
    """
        Translate specific fields to Japanese using MyMemory API
    """



    for field in fields_to_translate:
        # Kiểm tra nếu trường tiếng Nhật đã có giá trị trong `vals`
        jp_field = f'{field}_jp'

        # Nếu trường tiếng Nhật đã có giá trị, không dịch mà giữ nguyên giá trị hiện tại
        if field in vals and vals[field] and (jp_field not in vals or not vals[jp_field]):
            vals[jp_field] = _translate_text(vals[field])

def _translate_text(text):
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

def get_text(text_field,ans,odoo_model):
    """
        Get text
        :param ans: dict
        :param text_field: array of text_field name
        :return: dict
            {
                'text_field': 'text'
            }
    """
    for text_name in text_field:
        code_to_run = f"ans['{text_name}'] = odoo_model.{text_name}\n"
        code_to_run += f"ans['{text_name}_jp'] = odoo_model.{text_name}_jp"
        exec(code_to_run)
    return ans