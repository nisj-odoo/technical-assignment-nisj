# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api


class TransportManagementInventory(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("transport.management.dock", string="Dock" )
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")
    weight = fields.Float(string="Weight",compute="_compute_weight", store='1')
    volume = fields.Float(string="Volume",compute="_compute_volume", store='1')
    no_of_transfers = fields.Integer(string="No of Transfer Line",compute="_compute_transfer_lines", store=1)

    @api.depends("vehicle_category_id.max_volume")
    def _compute_weight(self):
        for record in self:
            if record.vehicle_category_id or record.vehicle_category_id.max_weight != 0:
                record.weight = (sum(record.picking_id.mapped('weight'))*100/record.vehicle_category_id.max_weight)
            else:
                record.weight=0

    @api.depends("vehicle_category_id.max_volume")
    def _compute_volume(self):
        for record in self:
            if record.vehicle_category_id or record.vehicle_category_id.max_volume != 0:
                record.volume = (sum(record.picking_id.mapped('volume'))*100/record.vehicle_category_id.max_volume)
            else:
                record.volume=0
    
    @api.depends("move_line_ids")
    def _compute_transfer_lines(self):
        for record in self:
            record.no_of_transfers = len(record.move_line_ids)
