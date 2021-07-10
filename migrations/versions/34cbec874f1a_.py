"""empty message

Revision ID: 34cbec874f1a
Revises: 
Create Date: 2021-07-10 10:52:30.530677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34cbec874f1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shell_model', sa.Column('address', sa.String(length=128), nullable=True))
    op.drop_column('shell_model', 'adress')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shell_model', sa.Column('adress', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('shell_model', 'address')
    # ### end Alembic commands ###