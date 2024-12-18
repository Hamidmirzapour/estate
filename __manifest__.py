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
    'category': 'Sales',
    'website': 'https://hamidmirzapour.ir',
    'depends': ['base', 'mail', 'sale'],
    'assets': {},
    'data': [
        'security/ir.model.access.csv',
        # 'data/estate.property.csv',
        'data/estate_property_cron.xml',
        'data/mail_template_data.xml',
        'views/estate_property.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_report.xml',
        'views/menu.xml',
    ],
    'demo': [
        'data/estate_property_tag_demo.xml',
        'data/estate_property_type_demo.xml',
        'data/estate_property_demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}