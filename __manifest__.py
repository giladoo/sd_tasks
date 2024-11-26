# -*- coding: utf-8 -*-
{
    'name': "sd_tasks",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://gilaneh.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': True,
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'project'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sd_tasks/static/src/components/**/*',

        ],

    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png'
    ],

    'license': 'LGPL-3',

}
