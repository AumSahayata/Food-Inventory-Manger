"""updated expiry table

Revision ID: 9e93d6a61aaf
Revises: 8b5e2c6fccf9
Create Date: 2025-01-10 04:43:57.976500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '9e93d6a61aaf'
down_revision: Union[str, None] = '8b5e2c6fccf9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expiry', sa.Column('vendor_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('expiry', 'vendor_id')
    # ### end Alembic commands ###
