"""empty message

Revision ID: e8cdcdccdecb
Revises: 6315334d98ea
Create Date: 2020-06-12 15:36:32.255596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8cdcdccdecb'
down_revision = '6315334d98ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('created_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('score', 'created_at')
    # ### end Alembic commands ###
