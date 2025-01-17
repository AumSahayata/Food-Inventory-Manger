"""added sales table

Revision ID: 6e0d8155d4ac
Revises: a80e230c9f7b
Create Date: 2025-01-10 01:28:30.303009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6e0d8155d4ac'
down_revision: Union[str, None] = 'a80e230c9f7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sales',
    sa.Column('sale_id', sa.UUID(), nullable=False),
    sa.Column('product_id', sa.Uuid(), nullable=False),
    sa.Column('sale_date', sa.Date(), nullable=False),
    sa.Column('is_holiday', sa.Boolean(), nullable=False),
    sa.Column('sale_day', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('quantity_sold', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.p_id'], ),
    sa.PrimaryKeyConstraint('sale_id')
    )
    op.alter_column('inventory', 'expiry_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('inventory', 'expiry_date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    op.drop_table('sales')
    # ### end Alembic commands ###
