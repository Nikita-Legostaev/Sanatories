"""initial

Revision ID: 6ed06dd7cbc5
Revises: 
Create Date: 2024-09-23 12:46:11.183749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ed06dd7cbc5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accommodations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_type', sa.String(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('daily_rate', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('procedures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('procedure_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purpose', sa.String(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=False),
    sa.Column('position', sa.String(), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accommodations_usage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('accommodations_id', sa.Integer(), nullable=False),
    sa.Column('room_type', sa.String(), nullable=False),
    sa.Column('start_data', sa.Date(), nullable=False),
    sa.Column('end_data', sa.Date(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['accommodations_id'], ['accommodations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('accommodation_id', sa.Integer(), nullable=False),
    sa.Column('check_in_date', sa.Date(), nullable=False),
    sa.Column('check_out_date', sa.Date(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodations.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('procedure_appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('procedure_id', sa.Integer(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedures.id'], ),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room_usage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('procedure_id', sa.Integer(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedures.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('room_usage')
    op.drop_table('procedure_appointment')
    op.drop_table('bookings')
    op.drop_table('accommodations_usage')
    op.drop_table('staff')
    op.drop_table('rooms')
    op.drop_table('procedures')
    op.drop_table('clients')
    op.drop_table('accommodations')
    # ### end Alembic commands ###
