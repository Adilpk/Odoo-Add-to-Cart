{
    'name': 'Add To Cart',
    'version': '17.0.1.0.0',
    'summary': 'Select Quantity and Add To Cart',
    'category': 'website',
    'author': 'Adil P K',
    'description': """ Add option Add to Cart and Select Quantity into
                      front of all products displayed in the website""",
    'depends': ['website_sale'],
    'data': [
        'views/select_quantity.xml',
        'views/select_quantity_option.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
