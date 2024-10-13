{
    'name': 'umbrella_availability',
    'version': '1.0',
    'depends': ['product', 'website_sale'],
    'category': 'Custom',
    'summary': 'Gestione della disponibilità degli ombrelloni',
    'description': """
        Aggiunge la disponibilità degli ombrelloni e un calendario per visualizzare le disponibilità in base alla data.
    """,
    'data': [
        'views/umbrella_availability_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
