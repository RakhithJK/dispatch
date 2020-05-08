"""Alters email colum in DispatchUser model

Revision ID: 734feb50c4ce
Revises: d1e66a4ef671
Create Date: 2020-05-08 10:16:07.414543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "734feb50c4ce"
down_revision = "d1e66a4ef671"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("dispatch_user", "email", existing_type=sa.VARCHAR(), nullable=True)
    op.create_unique_constraint(None, "dispatch_user", ["email"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "dispatch_user", type_="unique")
    op.alter_column("dispatch_user", "email", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###