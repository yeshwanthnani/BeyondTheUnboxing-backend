"""first commit

Revision ID: 7a2954a4fbe6
Revises: 
Create Date: 2023-11-21 23:31:00.023666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a2954a4fbe6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserAccount',
    sa.Column('user_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=255), nullable=True),
    sa.Column('user_email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('year_of_birth', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('user_ID')
    )
    op.create_table('mobile',
    sa.Column('mobile_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('brand', sa.String(length=255), nullable=True),
    sa.Column('mobile_name', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('mobile_ID')
    )
    op.create_table('question',
    sa.Column('question_ID', sa.Integer(), nullable=False),
    sa.Column('question_text', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('question_ID'),
    sa.UniqueConstraint('question_text')
    )
    op.create_table('review',
    sa.Column('review_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_ID', sa.Integer(), nullable=False),
    sa.Column('mobile_ID', sa.Integer(), nullable=False),
    sa.Column('question_ID', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['mobile_ID'], ['mobile.mobile_ID'], ),
    sa.ForeignKeyConstraint(['question_ID'], ['question.question_ID'], ),
    sa.ForeignKeyConstraint(['user_ID'], ['UserAccount.user_ID'], ),
    sa.PrimaryKeyConstraint('review_ID')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('question')
    op.drop_table('mobile')
    op.drop_table('UserAccount')
    # ### end Alembic commands ###
