"""perubahan ukuran

Revision ID: 006dc6dfce57
Revises: 8fc8a72192bb
Create Date: 2024-05-05 04:56:31.542197

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '006dc6dfce57'
down_revision = '8fc8a72192bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=128),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=False)

    # ### end Alembic commands ###