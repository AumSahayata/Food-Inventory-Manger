"""updated inventory table

Revision ID: ab4a914766d3
Revises: 901e895816f9
Create Date: 2025-01-10 06:26:08.990866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ab4a914766d3'
down_revision: Union[str, None] = '901e895816f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sales',
    sa.Column('sale_id', sa.UUID(), nullable=False),
    sa.Column('product_id', sa.Uuid(), nullable=False),
    sa.Column('sale_date', sa.Date(), nullable=False),
    sa.Column('is_holiday', sa.Boolean(), nullable=False),
    sa.Column('sale_day', sa.Integer(), nullable=False),
    sa.Column('quantity_sold', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.p_id'], ),
    sa.PrimaryKeyConstraint('sale_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales')
    # ### end Alembic commands ###
