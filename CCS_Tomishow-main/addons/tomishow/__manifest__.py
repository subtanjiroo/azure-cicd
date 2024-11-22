{
    'name': 'Tomishow',
    'version': '1.0',
    'depends': ['base','website'],
    'data': [
        'security/ir.model.access.csv',
        'views/Home.xml',
        'views/Details.xml',
        'views/cms/div3_iconandtext.xml',
        'views/cms/div_1.xml',
        'views/cms/div_2.xml',
        'views/cms/div_3.xml',
        'views/cms/div_4.xml',
        'views/cms/div_4_project.xml',
        'views/cms/div_5.xml',
        'views/cms/div_6.xml',
        'views/cms/div_6_people.xml',
        'views/cms/div_7.xml',
        'views/cms/div_7_process.xml',
        'views/cms/div_7_rule.xml',
        'views/cms/header.xml',
        'views/cms/menu_items.xml',
        'data/cms_record.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/js/all.min.js',
            'https://unpkg.com/swiper/swiper-bundle.min.js',
            'https://unpkg.com/swiper/swiper-bundle.min.css',
            'tomishow/static/src/css/cms.css',
        ],
        'web.assets_frontend': [
            # Font Awesome for frontend
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/js/all.min.js',
        ],
    },

    'installable': True,
    'application': True,
    "license": "LGPL-3"
}
