# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api


class TransportManagementType(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight=fields.Integer(string='Maximum Weight (Kg)')
    max_volume=fields.Integer(string='Maximum Volume (m\u00b3)')

    @api.depends('max_weight','max_volume')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f'{rec.name} ({rec.max_weight} Kg, {rec.max_volume} m\u00b3 )'
    
    _sql_constraints = [
        ('check_max_weight','CHECK(max_weight > 0)','Weight must be greater than 0'),
        ('check_max_volume','CHECK(max_volume > 0)','Weight must be greater than 0')
    ]
