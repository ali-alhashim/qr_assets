from odoo import http
from odoo.http import request

class ZebraLabelController(http.Controller):

    @http.route('/asset/print_labels', type='http', auth='user')
    def print_labels(self, ids='', **kwargs):
        asset_ids = [int(i) for i in ids.split(',') if i]
        assets = request.env['asset.asset'].browse(asset_ids)

        return request.render('qr_assets.report_asset_zebra_page', {
            'docs': assets,
        })