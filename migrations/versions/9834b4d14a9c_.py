"""empty message

Revision ID: 9834b4d14a9c
Revises: 204973fb4313
Create Date: 2022-04-07 13:37:03.912766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9834b4d14a9c'
down_revision = '204973fb4313'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_posts')
    # ### end Alembic commands ###
