"""added unique constraint for User

Revision ID: e2435b397eb6
Revises: 7a2319e24752
Create Date: 2023-11-29 19:41:24.408395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2435b397eb6'
down_revision: Union[str, None] = '7a2319e24752'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'UserAccount', ['user_email'])
    op.create_unique_constraint(None, 'UserAccount', ['user_name'])
    op.create_unique_constraint('uq_user_mobile_question', 'review', ['user_ID', 'mobile_ID', 'question_ID'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_user_mobile_question', 'review', type_='unique')
    op.drop_constraint(None, 'UserAccount', type_='unique')
    op.drop_constraint(None, 'UserAccount', type_='unique')
    # ### end Alembic commands ###