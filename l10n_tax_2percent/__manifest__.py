# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "2% Tax",
    'summary': """
        Adds a 2% tax configuration""",
    'description': """
        This module adds a 2% tax rate that can be used in invoices and sales orders.
    """,
    'author': "Your Company",
    'website': "https://www.yourcompany.com",
    'category': 'Accounting/Taxes',
    'version': '1.0',
    'depends': ['account'],
    'data': [
        'data/account_tax_data.xml',
    ],
    'installable': True,
    'application': False,
} 