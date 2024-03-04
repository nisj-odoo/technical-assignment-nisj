# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api
from odoo import Command


class TransportManagementDock(models.Model):
    _name = "transport.management.dock"
    _description = "Specific Dock"

    name = fields.Char(string="Name")