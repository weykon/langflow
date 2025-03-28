"""Add unique constraints per user in folder table

Revision ID: 1c79524817ed
Revises: 3bb0ddf32dfb
Create Date: 2024-05-29 23:12:09.146880

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision: str = "1c79524817ed"
down_revision: Union[str, None] = "3bb0ddf32dfb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)  # type: ignore
    constraints_names = [constraint["name"] for constraint in inspector.get_unique_constraints("folder")]
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("folder", schema=None) as batch_op:
        if "unique_folder_name" not in constraints_names:
            batch_op.create_unique_constraint("unique_folder_name", ["user_id", "name"])

    # ### end Alembic commands ###


def downgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)  # type: ignore
    constraints_names = [constraint["name"] for constraint in inspector.get_unique_constraints("folder")]
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("folder", schema=None) as batch_op:
        if "unique_folder_name" in constraints_names:
            batch_op.drop_constraint("unique_folder_name", type_="unique")

    # ### end Alembic commands ###
