# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class CouponReport(models.AbstractModel):
    _name = 'report.sale_coupon.report_coupon'

    @api.model
    def get_report_values(self, docids, data=None):
        docs = self.env['sale.coupon'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.coupon',
            'data': data,
            'docs': docs,
        }
