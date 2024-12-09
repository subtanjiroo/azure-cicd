from odoo import http
from odoo import models, fields, api
from odoo.http import Controller, route, request
import logging

# Tạo một logger
_logger = logging.getLogger(__name__)

class CustomerInfo(models.Model):
    _name = 'tomishow'
    _description = 'tomishow Render'


class HomePage(Controller):
    @route(['/home'], type='http', auth='public', website=True)
    def HomePage(self):
        return request.render('tomishow.Home_Page')
class Details(Controller):
    @route(['/details'], type='http', auth='public', website=True)
    def Details(self):
        return request.render('tomishow.Details_Page')
        """
        Handle requests to fetch a project by ID.
        """
        project_id = kwargs.get('id')
        
        if not project_id:
            return {
                'status': 'error',
                'message': 'Missing "id" in request'
            }
        
        try:
            project_id = int(project_id)
            # Gọi service để tìm kiếm project
            project_data = request.env['cms.div4.project'].get_project_data_by_id(project_id)
            if project_data:
                return {
                    'status': 'success',
                    'data': project_data
                }
            else:
                return {
                    'status': 'error',
                    'message': f'No project found with ID {project_id}'
                }
        except ValueError:
            return {
                'status': 'error',
                'message': '"id" must be an integer'
            }
        except Exception as e:
            _logger.exception(f"Error fetching project by ID: {e}")
            return {
                'status': 'error',
                'message': 'An error occurred while processing the request'
            }