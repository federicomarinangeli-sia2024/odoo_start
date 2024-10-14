{
    'name': 'Umbrella Availability',
    'summary': 'Manage the availability of umbrellas',
    'description': """Manage availability per row and quantity of umbrellas""",
    'author': 'Your Company',
    'website': 'http://www.yourcompany.com',
    'category': 'Website',
    'version': '14.0.1.0',
    'depends': ['website_sale', 'product', 'product_custom'],  # Aggiunte dipendenze da product e product_custom
    'data': [
        'security/ir.model.access.csv',
        'views/umbrella_availability_views.xml',
        'i18n/it.po',  # Questo carica la traduzione in italiano
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
