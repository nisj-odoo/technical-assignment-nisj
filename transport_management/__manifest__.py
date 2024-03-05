# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Transport',
    'depends':[
        'fleet','stock_picking_batch',
    ],
    'installable':True,
    'application':True,

    'data':[
        'security/ir.model.access.csv',
        'views/transport_management_type.xml',
        'views/transport_management_dock.xml',
        'views/transport_management_inventory.xml',
        'views/transport_manageent_transfers.xml',
    ],
}