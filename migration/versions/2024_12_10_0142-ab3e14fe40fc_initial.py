"""initial

Revision ID: ab3e14fe40fc
Revises: 8ec81ca07529
Create Date: 2024-12-10 01:42:46.358465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab3e14fe40fc'
down_revision: Union[str, None] = '8ec81ca07529'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accommodations_usage', 'room_type')
    op.drop_column('accommodations_usage', 'capacity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accommodations_usage', sa.Column('capacity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('accommodations_usage', sa.Column('room_type', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
