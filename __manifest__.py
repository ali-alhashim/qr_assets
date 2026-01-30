{
    'name': 'QR Assets Management',
    'version': '1.0',
    'category': 'Operations/Assets',
    'summary': 'Manage company assets with QR code tracking and assignments',
    'author': 'Ali Alhashim',
    'depends': ['base', 'hr', 'mail', 'web'],
    'data': [
        'security/qr_assets_security.xml',
        'security/ir.model.access.csv',
        'report/asset_report.xml',
        'views/asset_views.xml',
        'views/hr_employee_view.xml',
        
    ],
    'assets': {
        'web.assets_backend': [],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
