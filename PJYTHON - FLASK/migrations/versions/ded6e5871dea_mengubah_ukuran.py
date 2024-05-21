"""mengubah ukuran

Revision ID: ded6e5871dea
Revises: 006dc6dfce57
Create Date: 2024-05-05 11:43:11.669056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ded6e5871dea'
down_revision = '006dc6dfce57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=60),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=250),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=250),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=250),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###