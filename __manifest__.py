# -*- coding: utf-8 -*-
{
    'name': "AL-ITKAN Extension",

    'summary': """
        Itkan Extension
    """,

    'description': """
        A Module Developed by Integerated Path
    """,

    'author': "Integerated Path",
    'website': "https://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_recruitment', 'product', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_view.xml',
        "views/employee_view.xml",
        "views/jobs_view.xml",
        "report/recruitment_report.xml",
    ],
}
