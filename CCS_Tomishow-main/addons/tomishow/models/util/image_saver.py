'''
Author: Thinh dep trai
Model Description: save image
'''

import os
import base64
path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static', 'imgs')
import os
import base64

def save_img(div, img, vals, odoo_model):
    """
        Save image to static/imgs/div/img.png
        :param div: div_name
        :param img: array of img_field name
        :param vals: array of write values
        :param odoo_model: odoo object of the div
        :return: None
    """
    # Tạo đường dẫn đến thư mục lưu trữ
    file_path = os.path.join(path, div)
    
    # Duyệt qua danh sách các trường hình ảnh
    for img_name in img:
        if img_name in vals:  # Nếu trường có trong vals
            # Giải mã dữ liệu base64
            if vals[img_name] is not False:
                file_data = base64.b64decode(vals[img_name])
                
                # Tạo tên file với trường hình ảnh
                current_file_path = os.path.join(file_path, f'{img_name}.png')
                
                # Tạo thư mục nếu chưa tồn tại
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                
                # Ghi file vào hệ thống
                with open(current_file_path, 'wb') as f:
                    f.write(file_data)

import os
import base64

def save_img_sub_model(div,sub_model,sub_model_id, img, vals,odoo_model):
    """
        Save image to static/imgs/div/img.png
        :param div: div_name
        :param img: array of img_field name
        :param vals: array of write values
        :param odoo_model: odoo object of the div
        :return: None
    """
    file_path = os.path.join(path,div,sub_model)
    code_to_run = ""
    ans=""
    for img_name in img:
        if img_name in vals:
            code_to_run += f"file =base64.b64decode(vals['{img_name}'])\n"
            code_to_run += f"current_file_path = os.path.join(file_path,str({sub_model_id}),'{img_name}'+'.png')\n"
            #create folder if not exist
            code_to_run += f"if not os.path.exists(os.path.join(file_path,str({sub_model_id}))):\n"
            code_to_run += f"\tos.makedirs(os.path.join(file_path,str({sub_model_id})))\n"
            code_to_run += f"with open(current_file_path,'wb') as f:\n"
            code_to_run += f"    f.write(file)\n"
    exec (code_to_run)

    return ans
def remove_img_sub_model(div,sub_model,sub_model_id):
    """
        Remove image from static/imgs/div/img.png
        :param div: div_name
        :param img: array of img_field name
        :param odoo_model: odoo object of the div
        :return: None
    """
    file_path = os.path.join(path,div,sub_model,str(sub_model_id))
    #remove all file in the folder first
    if os.path.exists(file_path):
        import shutil
        shutil.rmtree(file_path)
    return True





def get_img_path(ans, div, img, odoo_model):
    """
        Get image path
        :param ans: dict
        :param div: div_name
        :param img: array of img_field name
        :param odoo_model: odoo object of the div
        :return: dict
            {
                'img_field': 'img_path'
            }
    """
    for img_name in img:
        ans[img_name] = f'/tomishow/static/imgs/{div}/{img_name}.png'

def get_img_path_sub_model(ans, div, sub_model, sub_model_id, img, odoo_model):
    """
        Get image path
        :param ans: dict
        :param div: div_name
        :param sub_model: sub_model_name
        :param sub_model_id: ID of the sub_model
        :param img: array of img_field name
        :param odoo_model: odoo object of the div
        :return: dict
            {
                'img_field': 'img_path'
            }
    """
    for img_name in img:
        ans[img_name] = f'/tomishow/static/imgs/{div}/{sub_model}/{sub_model_id}/{img_name}.png'




