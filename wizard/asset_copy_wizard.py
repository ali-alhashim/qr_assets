from odoo import models, fields, api

class AssetCopyWizard(models.TransientModel):
    _name = 'asset.copy.wizard'
    _description = 'Copy Data from Existing Asset'

    # Filtered to make sure you don't copy an asset onto itself
    asset_id = fields.Many2one(
        'asset.asset', 
        string="Select Asset to Copy From", 
        required=True,
        domain="[('id', '!=', context.get('active_id'))]"
    )

    def action_copy_data(self):
        self.ensure_one()
        active_asset_id = self.env.context.get('active_id')
        if not active_asset_id:
            return {'type': 'ir.actions.act_window_close'}

        new_asset = self.env['asset.asset'].browse(active_asset_id)
        source = self.asset_id

        # Use .id safely for Many2one fields
        vals = {
            'model': source.model,
            'type_id': source.type_id.id if source.type_id else False,
            'subtype_id': source.subtype_id.id if source.subtype_id else False,
            'style_id': source.style_id.id if source.style_id else False,
            'shape_id': source.shape_id.id if source.shape_id else False,
            'vendor_id': source.vendor_id.id if source.vendor_id else False,
            'department_id': source.department_id.id if source.department_id else False,
            'location_id': source.location_id.id if source.location_id else False,
            'value': source.value,
            'color': source.color,
            'name': source.name,
            'dimension': source.dimension,
            'description': source.description,
            'employee_id': source.employee_id.id if source.employee_id else False,
        }
        
        # We generally DON'T copy name/serial/QR to keep the new record unique
        new_asset.write(vals)
        
        return {'type': 'ir.actions.act_window_close'}