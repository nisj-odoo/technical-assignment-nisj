# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api


class TransportManagementType(models.Model):
    _inherit = "stock.picking"

    weight = fields.Float(compute="_compute_weight_volume_transfers")
    volume = fields.Float(compute="_compute_weight_volume_transfers")

    @api.depends('move_ids')
    def _compute_weight_volume_transfers(self):
        for record in self:
            record.weight = sum(move.product_id.weight*move.product_qty for move in record.move_ids)
            record.volume = sum(move.product_id.volume*move.product_qty for move in record.move_ids)
