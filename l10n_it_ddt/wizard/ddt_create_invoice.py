# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Alessandro Camilli <alessandrocamilli@openforce.it>
#    Copyright (C) 2017 Openforce di Camilli Alessandro (http://www.openforce.it)
#
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
##############################################################################


from odoo import fields, models, api, _
from odoo.exceptions import Warning as UserError


class DdtCreateInvoice(models.TransientModel):
    _name = "ddt.create.invoice"

    def _get_ddt_ids(self):
        return self.env['stock.picking.package.preparation'].browse(
            self.env.context['active_ids'])

    ddt_ids = fields.Many2many(
        'stock.picking.package.preparation', default=_get_ddt_ids)

    @api.multi
    def create_invoice(self):

        if self.ddt_ids:
            self.ddt_ids.action_invoice_create()
