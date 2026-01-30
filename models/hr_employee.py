from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    arabic_name = fields.Char(string="Arabic Name")

    asset_count = fields.Integer(compute='_compute_asset_count', string="Assets", store=True)

    def _compute_asset_count(self):
        for employee in self:
            employee.asset_count = self.env['asset.asset'].search_count([('employee_id', '=', employee.id)])

    def action_view_assets(self):
        return {
            'name': 'Assigned Assets',
            'type': 'ir.actions.act_window',
            'res_model': 'asset.asset',
            'view_mode': 'list,form',
            'domain': [('employee_id', '=', self.id)],
        }
