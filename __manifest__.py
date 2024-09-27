{
    'name' : 'Real Estate',
    'version' : '1.0',
    'summary': 'Real Estate Management Application',
    'sequence': 0,
    'description': """
        The Estate Management module for Odoo is designed to streamline the process of managing real estate properties, 
        including residential, commercial, and rental properties. 
        It allows users to handle key aspects like property listings, tenant management, lease agreements, maintenance requests, and financial transactions. 
        With this module, real estate agents, property managers, and landlords can efficiently track their portfolio, manage tenant communications, and monitor 
        lease terms, all within the Odoo platform. 
        This module supports multi-property management, reporting, and seamless integration with Odoo's accounting and CRM modules for a comprehensive business solution.
    """,
    'author': 'Hamid Mirzapour',
    'category': 'Estate',
    'website': 'https://hamidmirzapour.ir',
    'depends': ['base'],
    'assets': {},
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'demo': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}