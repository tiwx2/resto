"""Added a boolean confirmation flag

Revision ID: 2145945551a9
Revises: 6903e32b3b94
Create Date: 2018-09-09 03:10:54.978795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2145945551a9'
down_revision = '6903e32b3b94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed')
    # ### end Alembic commands ###