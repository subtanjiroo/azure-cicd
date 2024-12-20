{
    'name': 'Tomishow',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/Home.xml',
        'views/Details.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',
        ],
        'web.assets_frontend': [
            # Font Awesome for frontend
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',
        ],
    },

    'installable': True,
    'application': True,
    "license": "LGPL-3"
}
