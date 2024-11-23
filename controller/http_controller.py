import json

from odoo import http


class Tomishow(http.Controller):



    @http.route('/get_div_1', type='http', auth='public', methods=['GET'])
    def get_div_1(self):
        div_1 = http.request.env['cms.div1'].sudo().get_div_1()
        return http.request.make_response(
            json.dumps(div_1),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/get_div_2', type='http', auth='public', methods=['GET'])
    def get_div_2(self):
        div_2 = http.request.env['cms.div2'].sudo().get_div_2()
        return http.request.make_response(
            json.dumps(div_2),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/get_div_3', type='http', auth='public', methods=['GET'])
    def get_div_3(self):
        div_3 = http.request.env['cms.div3'].sudo().get_div_3()
        return http.request.make_response(
            json.dumps(div_3),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/get_div_4', type='http', auth='public', methods=['GET'])
    def get_div_4(self):
        div_4 = http.request.env['cms.div4'].sudo().get_div_4()
        return http.request.make_response(
            json.dumps(div_4),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/get_div_5', type='http', auth='public', methods=['GET'])
    def get_div_5(self):
        div_5 = http.request.env['cms.div5'].sudo().get_div_5()
        return http.request.make_response(
            json.dumps(div_5),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/get_div_6', type='http', auth='public', methods=['GET'])
    def get_div_6(self):
        div_6 = http.request.env['cms.div6'].sudo().get_div_6()
        return http.request.make_response(
            json.dumps(div_6),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/get_div_7', type='http', auth='public', methods=['GET'])
    def get_div_7(self):
        div_7 = http.request.env['cms.div7'].sudo().get_div_7()
        return http.request.make_response(
            json.dumps(div_7),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/get_div_8', type='http', auth='public', methods=['GET'])
    def get_div_8(self):
        div_8 = http.request.env['cms.div8'].sudo().get_div_8()
        return http.request.make_response(
            json.dumps(div_8),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/get_header', type='http', auth='public', methods=['GET'])
    def get_header(self):
        get_header = http.request.env['cms.header'].sudo().get_header()
        return http.request.make_response(
            json.dumps(get_header),
            headers=[('Content-Type', 'application/json')]
        )
