"""empty message

Revision ID: e09b8388b722
Revises: bb2af92575be
Create Date: 2022-09-02 18:05:19.320791

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e09b8388b722'
down_revision = 'bb2af92575be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('services', sa.String(length=3), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('contact__')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact__',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('full_name', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('services', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('budget', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('message', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('contact')
    # ### end Alembic commands ###
