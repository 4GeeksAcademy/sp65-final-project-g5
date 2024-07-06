"""empty message

Revision ID: 0748a9db0d96
Revises: 
Create Date: 2024-07-04 01:07:52.790794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0748a9db0d96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('criminals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('nationality', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('caution', sa.String(), nullable=True),
    sa.Column('race', sa.String(), nullable=True),
    sa.Column('remarks', sa.Text(), nullable=True),
    sa.Column('hair_raw', sa.String(), nullable=True),
    sa.Column('possible_countries', sa.Text(), nullable=True),
    sa.Column('aliases', sa.Text(), nullable=True),
    sa.Column('place_of_birth', sa.Text(), nullable=True),
    sa.Column('dates_of_birth_used', sa.String(), nullable=True),
    sa.Column('eyes', sa.String(), nullable=True),
    sa.Column('subjects', sa.Text(), nullable=True),
    sa.Column('images', sa.Text(), nullable=True),
    sa.Column('field_offices', sa.Text(), nullable=True),
    sa.Column('reward_text', sa.String(), nullable=True),
    sa.Column('weight', sa.String(), nullable=True),
    sa.Column('favourites_amount', sa.Integer(), nullable=True),
    sa.Column('poster_classification', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('missing_persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('nationality', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('race', sa.String(), nullable=True),
    sa.Column('remarks', sa.String(), nullable=True),
    sa.Column('hair_raw', sa.String(), nullable=True),
    sa.Column('possible_countries', sa.Text(), nullable=True),
    sa.Column('place_of_birth', sa.Text(), nullable=True),
    sa.Column('dates_of_birth_used', sa.String(), nullable=True),
    sa.Column('eyes', sa.String(), nullable=True),
    sa.Column('subjects', sa.Text(), nullable=True),
    sa.Column('details', sa.String(), nullable=True),
    sa.Column('images', sa.Text(), nullable=True),
    sa.Column('field_offices', sa.Text(), nullable=True),
    sa.Column('reward_text', sa.String(), nullable=True),
    sa.Column('weight', sa.String(), nullable=True),
    sa.Column('favourites_amount', sa.Integer(), nullable=True),
    sa.Column('poster_classification', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('comments_criminals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('criminal_id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('comment_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['criminal_id'], ['criminals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments_missing_persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('missing_person_id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('comment_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['missing_person_id'], ['missing_persons.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('saved_criminals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('criminal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['criminal_id'], ['criminals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('saved_missing_persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('missing_person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['missing_person_id'], ['missing_persons.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stories_criminals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('prompt', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('creation_date', sa.Date(), nullable=True),
    sa.Column('modification_date', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('criminal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['criminal_id'], ['criminals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stories_missing_persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('prompt', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('creation_date', sa.Date(), nullable=True),
    sa.Column('modification_date', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('missing_person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['missing_person_id'], ['missing_persons.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stories_missing_persons')
    op.drop_table('stories_criminals')
    op.drop_table('saved_missing_persons')
    op.drop_table('saved_criminals')
    op.drop_table('comments_missing_persons')
    op.drop_table('comments_criminals')
    op.drop_table('users')
    op.drop_table('missing_persons')
    op.drop_table('criminals')
    # ### end Alembic commands ###