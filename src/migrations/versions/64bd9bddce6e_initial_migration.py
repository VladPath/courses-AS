"""initial migration

Revision ID: 64bd9bddce6e
Revises: 
Create Date: 2026-10-20 17:05:02.370514

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '64bd9bddce6e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Hotels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('Hotels')
