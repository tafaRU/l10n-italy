# Copyright 2025 Giuseppe Borruso - Dinamiche Aziendali srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import Command, fields, models


class AccountMoveLineInherit(models.Model):
    _inherit = "account.move.line"

    l10n_it_edi_admin_ref = fields.Char(string="Admin. ref.", size=20, copy=False)

    def adjust_accounting_data(self, product):
        message_to_log = []
        # get its default expense account
        template = product.product_tmpl_id
        prod_accounts = template.with_company(self.company_id)._get_product_accounts()
        # accounts_dict = template.get_product_accounts()
        account = prod_accounts["expense"]
        self.account_id = account.id

        new_tax = self.env["account.tax"]
        if len(template.supplier_taxes_id) == 1:
            new_tax = template.supplier_taxes_id[0]
        elif len(account.tax_ids) == 1:
            new_tax = account.tax_ids[0]
        line_tax = self.tax_ids[0]
        if new_tax and line_tax and new_tax != line_tax:
            if new_tax.amount != line_tax.amount:
                message = self.env._(
                    "XML contains tax %(line_tax)s. "
                    "Product %(product)s has tax %(new_tax)s. Using "
                    "the XML one"
                ) % {
                    "line_tax": line_tax.name,
                    "product": product.name,
                    "new_tax": new_tax.name,
                }
                message_to_log.append(message)
            else:
                # If product has the same amount of the one in XML,
                # I use it. Typical case: 22% det 50%
                self.tax_ids = [Command.set([new_tax.id])]
        return message_to_log
