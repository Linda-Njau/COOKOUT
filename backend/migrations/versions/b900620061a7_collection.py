"""collection

Revision ID: b900620061a7
Revises: 0006e9d5cf47
Create Date: 2023-05-31 13:29:39.343227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b900620061a7'
down_revision = '0006e9d5cf47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hidden', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('collection_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_recipe_collection_id', 'collection', ['collection_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('collection_id')
        batch_op.drop_column('hidden')

    # ### end Alembic commands ###