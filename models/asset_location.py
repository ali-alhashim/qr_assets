from odoo import models, fields

class AssetLocation(models.Model):
    _name = 'asset.location'
    _description = 'Asset Location'
    _parent_name = "parent_id"

    name = fields.Char(string="Location Name", required=True)
    parent_id = fields.Many2one('asset.location', string="Parent Location", ondelete='cascade')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    note = fields.Text(string="Notes")