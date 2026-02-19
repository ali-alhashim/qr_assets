import qrcode
import base64
from io import BytesIO
from datetime import date
from odoo import models, fields, api, _



class AssetType(models.Model):
    _name = 'asset.type'
    _description = 'Asset Type'

    name = fields.Char(string="Type Name", required=True)
    code = fields.Char(string="Code") # Optional, for internal reference


class AssetHistory(models.Model):
    _name = 'asset.history'
    _description = 'Asset Assignment History'
    _order = 'received_date desc'

    asset_id = fields.Many2one('asset.asset', string="Asset", ondelete='cascade')
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    received_date = fields.Date(string="Received Date", default=fields.Date.context_today)
    returned_date = fields.Date(string="Returned Date")
    note = fields.Text(string="Notes")

    @api.depends('returned_date')
    def _compute_is_current(self):
        for record in self:
            record.is_current = not record.returned_date



class AssetAsset(models.Model):
    _name = 'asset.asset'
    _description = 'Company Asset'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Asset Name", required=True, tracking=True)
    model = fields.Char(string="Model/Brand")
    serialnumber = fields.Char(string="Serial Number", tracking=True)

    type_id = fields.Many2one(
        'asset.type', 
        string="Asset Type", 
        ondelete='restrict',
        help="Select or create a new asset type"
    )

    # Assignment
    employee_id = fields.Many2one('hr.employee', string="Assigned Employee", tracking=True)

    employee_barcode = fields.Char(
        related='employee_id.barcode', 
        string="Badge ID",
        store=True,  
        readonly=True
    )

    department_id = fields.Many2one('hr.department', string="Department", tracking=True)
    location_id = fields.Many2one('asset.location', string="Location")

    # Status
    status = fields.Selection([
        ('draft', 'Draft'),
        ('assigned', 'Assigned'),
        ('damaged', 'Damaged'),
        ('sold', 'Sold'),
        ('stolen', 'Stolen'),
        ('lost', 'Lost')
    ], string="Status", default='draft', tracking=True)

    # Vendor & Financials
    vendor_id = fields.Many2one('res.partner', string="Vendor")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    value = fields.Monetary(string="Asset Value", currency_field='currency_id')

    # Physical
    color = fields.Char(string="Color")
    dimension = fields.Char(string="Dimensions")
    description = fields.Text(string="Description")
    image_ids = fields.One2many('ir.attachment', 'res_id', domain=[('res_model', '=', 'asset.asset')], string="Photos")

    # QR System
    qr_code = fields.Char(string="QR URL", compute="_compute_qr_url", store=True)
    qr_image = fields.Binary(string="QR Code Image", compute="_compute_qr_image", store=True)

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            self.department_id = self.employee_id.department_id
            self.status = 'assigned'

    @api.depends('name')
    def _compute_qr_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            if record.id:
                record.qr_code = f"{base_url}/web#id={record.id}&model=asset.asset&view_type=form"
            else:
                record.qr_code = False

    @api.depends('qr_code')
    def _compute_qr_image(self):
        for record in self:
            if record.qr_code:
                qr = qrcode.QRCode(version=1, box_size=8, border=1,error_correction=qrcode.constants.ERROR_CORRECT_H)
                qr.add_data(record.qr_code)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')
                temp = BytesIO()
                img.save(temp, format="PNG", dpi=(203, 203))
                record.qr_image = base64.b64encode(temp.getvalue())
            else:
                record.qr_image = False



    history_ids = fields.One2many('asset.history', 'asset_id', string="Assignment History")

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.employee_id:
                self.env['asset.history'].create({
                    'asset_id': record.id,
                    'employee_id': record.employee_id.id,
                    'received_date': date.today(),
                })
        return records

    def write(self, vals):
        if 'employee_id' in vals:
            for record in self:
                # 1. Close the old history record (if exists)
                old_history = self.env['asset.history'].search([
                    ('asset_id', '=', record.id),
                    ('returned_date', '=', False)
                ], limit=1)
                if old_history:
                    old_history.write({'returned_date': fields.Date.today()})
                
                # 2. Create new history if we are assigning to a new person
                if vals.get('employee_id'):
                    self.env['asset.history'].create({
                        'asset_id': record.id,
                        'employee_id': vals['employee_id'],
                        'received_date': fields.Date.today(),
                    })
        return super().write(vals)
    
    def action_view_qr_label_html(self):
        self.ensure_one()
        # This builds the URL for the HTML report
        report_url = f'/report/html/qr_assets.report_asset_zebra/{self.id}'
        return {
            'type': 'ir.actions.act_url',
            'url': report_url,
            'target': 'new', # This opens it in a new tab
        }

