# -*- coding: utf-8 -*-
{
    'name': "Pricelist Report PDF",

    'summary': """
        Price list report (PDF)  """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Luis Auyadermont",
    'website': "https://www.instagram.com/yurpro_21/?hl=es-la",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'report/pricelist_report.xml',
        'views/product_category.xml',
        
    ],
    # only loaded in demonstration mode
    # ~ 'data': [
        # ~ 'demo/demo.xml',
    # ~ ],
}
