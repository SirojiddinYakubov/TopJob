"""add required for some tables

Revision ID: 3a86d95a24ea
Revises: ce80f38b0d75
Create Date: 2023-08-22 12:20:19.524616

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import app # custom added
from typing import Text # custom added


# revision identifiers, used by Alembic.
revision = '3a86d95a24ea'
down_revision = 'ce80f38b0d75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('profession_translation', 'profession_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('resume', 'profession_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('sphere_translation', 'sphere_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sphere_translation', 'sphere_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('resume', 'profession_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('profession_translation', 'profession_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###