"""add type

Revision ID: d7a332a59baf
Revises: 
Create Date: 2019-03-04 07:09:49.195821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import Column, Integer

revision = 'd7a332a59baf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('views', Column('type', Integer))
    op.add_column('clicks', Column('type', Integer))
    op.add_column('click2s', Column('type', Integer))


def downgrade():
    op.drop_column('views', 'type')
    op.drop_column('clicks', 'type')
    op.drop_column('click2s', 'type')
