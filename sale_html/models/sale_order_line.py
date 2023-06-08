# Copyright 2023 fah-mili/Lambdao
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import markdownify

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    name = fields.Html(sanitize=False)
    name_txt = fields.Text(string="Label", compute="_compute_name_txt", store=True)

    @api.depends("name")
    def _compute_name_txt(self):
        for line in self:
            txt = line.name or ""
            line.name_txt = markdownify.markdownify(txt, heading_style="ATX")
