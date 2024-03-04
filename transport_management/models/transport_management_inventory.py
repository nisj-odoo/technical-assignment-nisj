# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api
from odoo import Command


class TransportManagementInventory(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("transport.management.dock", string="Dock" )
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")
    weight = fields.Float(string="Weight",compute="_compute_weight")
    volume = fields.Float(string="Volume",compute="_compute_volume")

    @api.depends("vehicle_category_id")
    def _compute_weight(self):
        for record in self:
            total_weight = 0
            for move in record.move_ids:
                total_weight += move.product_id.weight*move.product_qty
            if record.vehicle_category_id or record.vehicle_category_id.max_weight != 0:
                record.weight = total_weight*100/record.vehicle_category_id.max_weight
            else:
                record.weight=total_weight

    @api.depends("vehicle_category_id.max_volume")
    def _compute_volume(self):
        for record in self:
            total_volume = 0
            for move in record.move_ids:
                total_volume += move.product_id.volume*move.product_qty
            if record.vehicle_category_id or record.vehicle_category_id.max_volume != 0:
                record.volume = total_volume*100/record.vehicle_category_id.max_volume
            else:
                record.volume=total_volume

