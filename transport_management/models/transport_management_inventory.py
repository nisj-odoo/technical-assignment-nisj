# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api


class TransportManagementInventory(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("transport.management.dock", string="Dock" )
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")
    weight = fields.Float(string="Weight",compute="_compute_weight_volume", store='1')
    volume = fields.Float(string="Volume",compute="_compute_weight_volume", store='1')
    no_of_transfers = fields.Integer(string="No of Transfer Lines",compute="_compute_transfer_lines", store=1)
    no_of_lines = fields.Integer(string="No of Lines",compute="_compute_lines", store=1)
    display_name = fields.Char(string="Driver Name",compute="_compute_display_name", store=1)

    @api.depends("vehicle_category_id.max_weight","vehicle_category_id.max_volume","picking_ids")
    def _compute_weight_volume(self):
        for record in self:
            if record.vehicle_category_id and record.vehicle_category_id.max_weight != 0 and record.vehicle_category_id.max_volume != 0:
                record.weight = round(sum(record.picking_ids.mapped('weight'))*100/record.vehicle_category_id.max_weight,2)
                record.volume = round(sum(record.picking_ids.mapped('volume'))*100/record.vehicle_category_id.max_volume,2)
            else:
                record.weight=0
                record.volume=0
                
    @api.depends("picking_ids")
    def _compute_transfer_lines(self):
        for record in self:
            record.no_of_transfers = len(record.picking_ids)
    
    @api.depends("move_ids")
    def _compute_lines(self):
        for record in self:
            record.no_of_lines = len(record.move_ids)

    @api.depends('weight', 'volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}: {record.weight}kg, {record.volume}m\u00b3 {record.vehicle_id.driver_id.name}"