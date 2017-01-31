# -*- coding: utf-8 -*-
# Copyright 2015 Nicola Malcontenti - Agile Business Group
# Copyright 2016 Andrea Cometa - Apulia Software
# Copyright 2016 Lorenzo Battistini - Agile Business Group
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    'name': "Account invoice report grouped by DDT",
    'version': '10.0.1.0.0',
    'author': 'Agile Business Group, Apulia Software',
    'website': 'http://www.agilebg.com',
    'license': 'GPL-3',
    'depends': [
        'account',
        'stock_picking_invoice_link',
        'l10n_it_ddt',
    ],
    "data": [
        'views/invoice_ddt.xml',
    ],
    "installable": True
}
