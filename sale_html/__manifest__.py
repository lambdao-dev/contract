# Copyright 2023 fah-mili/Lambdao
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale Html",
    "summary": """Html in sale order line description""",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "fah-mili,Lambdao",
    "website": "https://github.com/lambdao-dev",
    "depends": ["sale"],
    "data": ["views/sale_order.xml"],
    "external_dependencies": {"python": ["markdownify"]},
    "pre_init_hook": "pre_init_hook",
}
