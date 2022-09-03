"""empty message

Revision ID: c9deb40d404d
Revises: 77662e65cb70
Create Date: 2022-09-03 15:07:10.807198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9deb40d404d'
down_revision = '77662e65cb70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('services', sa.String(length=3), nullable=True))
    op.add_column('contact', sa.Column('budget', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'budget')
    op.drop_column('contact', 'services')
    # ### end Alembic commands ###