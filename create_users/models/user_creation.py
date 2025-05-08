from odoo import models, api

class UserCreation(models.Model):
    _inherit = 'res.users'

    @api.model_create_multi
    def create_user_as_sudo(self, values):
        """Permite crear usuarios desde una app externa usando sudo."""
        return self.env['res.users'].sudo().create(values)
