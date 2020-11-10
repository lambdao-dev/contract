# Copyright 2020 ACSONE SA/NV.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase

PCTI = "property_contract_template_id"


class TestProductVariant(TransactionCase):
    def setUp(self):
        super(TestProductVariant, self).setUp()
        self.contract = self.env["contract.template"].create({"name": "Test"})
        self.attribute = self.env["product.attribute"].create({"name": "Brol"})
        atid = self.attribute.id
        pav = self.env["product.attribute.value"]
        self.attr_value_plic = pav.create({"name": "Plic", "attribute_id": atid})
        self.attr_value_ploc = pav.create({"name": "Ploc", "attribute_id": atid})
        atvids = [self.attr_value_plic.id, self.attr_value_ploc.id]
        self.product_template = self.env["product.template"].create(
            {
                "name": "Potiquet",
                "type": "service",
                "is_contract": True,
                PCTI: self.contract.id,
                "attribute_line_ids": [
                    (0, 0, {"attribute_id": atid, "value_ids": [(6, 0, atvids)]})
                ],
            }
        )

    def test_change_contract_on_variants(self):
        """The contract on variant should be the one on the template, unless
           manually changed.
        """
        contract_model = self.env["contract.template"]
        contract_plic = contract_model.create({"name": "Plic"})
        contract_ploc = contract_model.create({"name": "Ploc"})
        template = self.product_template
        plic, ploc = self.product_template.product_variant_ids

        for variant in self.product_template.product_variant_ids:
            self.assertEqual(variant[PCTI], contract_model)

        # editing a variant only edits the variant itself
        plic[PCTI] = contract_plic
        self.assertEqual(plic[PCTI], contract_plic)
        self.assertEqual(template[PCTI], self.contract)
        self.assertEqual(ploc[PCTI], contract_model)

        # editing the template has no impact
        template[PCTI] = contract_ploc
        self.assertEqual(plic[PCTI], contract_plic)
        self.assertEqual(template[PCTI], contract_ploc)
        self.assertEqual(ploc[PCTI], contract_model)

        # removing the template contract does not impact the variants
        template[PCTI] = False
        self.assertEqual(plic[PCTI], contract_plic)
        self.assertEqual(template[PCTI], contract_model)
        self.assertEqual(ploc[PCTI], contract_model)
