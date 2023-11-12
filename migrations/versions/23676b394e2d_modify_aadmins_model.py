"""Modify aAdmins model

Revision ID: 23676b394e2d
Revises: dd3650221401
Create Date: 2023-11-12 13:13:04.358718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23676b394e2d'
down_revision = 'dd3650221401'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_id', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.drop_column('admin_id')

    # ### end Alembic commands ###
