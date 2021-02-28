# -*- coding: utf-8 -*-
{
    'name': "Website Sale Fancy",

    'summary': """
        Add visual features to Odoo Website Sale""",

    'description': """
        Add visual features to Odoo Website Sale
    """,

    'author': "Moldeo Interactive",
    'website': "https://www.moldeointeractive.com.ar",

    'category': 'Website',
    'version': '0.1',

    'depends': ['base', 'website_sale'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [],
}
