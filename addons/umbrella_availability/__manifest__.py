{
    'name': 'Umbrella Availability',
    'version': '1.0',
    'summary': 'Gestione della disponibilità e prenotazione degli ombrelloni',
    'description': """
        Questo modulo gestisce la disponibilità degli ombrelloni negli stabilimenti, 
        consentendo ai clienti di prenotare gli ombrelloni tramite il sito e-commerce.
    """,
    'author': 'UmbrellaAdvisor',
    'website': 'http://www.tuosito.com',
    'category': 'Sales',
    'depends': ['base', 'website_sale', 'product', 'product_custom'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/stabilimento_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
