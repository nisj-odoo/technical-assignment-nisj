# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    module_transport_management = fields.Boolean(string="Dispatch Management System")
