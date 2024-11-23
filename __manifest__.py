{
    'name': 'Tomishow',
    'version': '1.0',
    'depends': ['base','website'],
    'data': [
        'security/ir.model.access.csv',
        'views/Home.xml',
        'views/Details.xml',
        'views/cms/div_1.xml',
        'views/cms/div_2.xml',
        'views/cms/div_3.xml',
        'views/cms/div_3_iconandtext.xml',
        'views/cms/div_4.xml',
        'views/cms/div_4_project.xml',
        'views/cms/div_5.xml',
        'views/cms/div_6.xml',
        'views/cms/div_6_people.xml',
        'views/cms/div_7.xml',
        'views/cms/div_7_process.xml',
        'views/cms/div_7_rule.xml',
        'views/cms/div_7_image.xml',
        'views/cms/div_8.xml',
        'views/cms/div_8_connection.xml',
        'views/cms/header.xml',
        'views/cms/menu_items.xml',
        'data/cms_record.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.0-beta3/css/all.min.css',
            'tomishow/static/src/css/cms.css',
        ],
        'web.assets_frontend': [
            # Font Awesome for frontend
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.0-beta3/css/all.min.css',
        ],
    },

    'installable': True,
    'application': True,
    "license": "LGPL-3"
}
