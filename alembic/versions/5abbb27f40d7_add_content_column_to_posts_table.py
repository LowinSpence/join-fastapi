"""add content column to posts table

Revision ID: 5abbb27f40d7
Revises: 3f7a59356c0a
Create Date: 2021-11-08 12:56:23.204653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5abbb27f40d7'
down_revision = '3f7a59356c0a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
