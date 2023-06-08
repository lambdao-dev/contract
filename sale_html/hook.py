# Copyright 2023 fah-mili/Lambdao
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def pre_init_hook(cr):
    q_exists = """
    SELECT 1 FROM information_schema.columns
    WHERE table_name='sale_order_line' AND column_name='name_txt'
"""
    cr.execute(q_exists)
    exists = cr.rowcount
    if not exists:
        q_create = """ALTER TABLE sale_order_line ADD COLUMN name_txt text"""
        cr.execute(q_create)

    # of course, this should be run only at pre_init_hook time
    # but by checking for null we avoid overwriting existing correct values
    q_update = """UPDATE sale_order_line SET name_txt = name where name_txt IS NULL"""
    cr.execute(q_update)
