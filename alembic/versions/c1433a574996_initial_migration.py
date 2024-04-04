"""Initial migration

Revision ID: c1433a574996
Revises: 
Create Date: 2024-04-04 23:21:12.263015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1433a574996'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('directors')
    op.drop_table('bank_accounts')
    op.drop_table('actors_movies')
    op.drop_table('actors')
    op.drop_table('movies')
    op.drop_table('actors_2')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors_2',
    sa.Column('actors_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('surname', sa.TEXT(), nullable=True),
    sa.Column('age', sa.TEXT(), nullable=True),
    sa.Column('sex', sa.TEXT(), nullable=True),
    sa.CheckConstraint("sex IN ('m', 'f')"),
    sa.PrimaryKeyConstraint('actors_id')
    )
    op.create_table('movies',
    sa.Column('movie_id', sa.INTEGER(), nullable=True),
    sa.Column('name_movie', sa.TEXT(), nullable=True),
    sa.Column('release', sa.INTEGER(), nullable=True),
    sa.Column('budget', sa.INTEGER(), nullable=True),
    sa.Column('director_id', sa.INTEGER(), nullable=True),
    sa.Column('rating', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['director_id'], ['directors.director_id'], ),
    sa.PrimaryKeyConstraint('movie_id')
    )
    op.create_table('actors',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('surname', sa.TEXT(), nullable=False),
    sa.Column('age', sa.INTEGER(), nullable=False),
    sa.Column('movie_name', sa.TEXT(), nullable=True),
    sa.Column('budget', sa.INTEGER(), server_default=sa.text('(10000000)'), nullable=True),
    sa.Column('manager', sa.TEXT(), nullable=True),
    sa.Column('release_year', sa.INTEGER(), nullable=True),
    sa.Column('sex', sa.TEXT(), nullable=False),
    sa.Column('fee_actors', sa.REAL(), nullable=True),
    sa.Column('city', sa.TEXT(), nullable=True),
    sa.CheckConstraint("sex IN ('male', 'female')"),
    sa.CheckConstraint('age >= 5 AND age <= 99'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('actors_movies',
    sa.Column('actors_movies_id', sa.INTEGER(), nullable=True),
    sa.Column('movie_id', sa.INTEGER(), nullable=True),
    sa.Column('actors_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['actors_id'], ['actors_2.actors_id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.movie_id'], ),
    sa.PrimaryKeyConstraint('actors_movies_id')
    )
    op.create_table('bank_accounts',
    sa.Column('bank_account_id', sa.INTEGER(), nullable=True),
    sa.Column('director_id', sa.INTEGER(), nullable=True),
    sa.Column('actors_id', sa.INTEGER(), nullable=True),
    sa.Column('account_number', sa.TEXT(), nullable=True),
    sa.Column('finance', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['actors_id'], ['actors_2.actors_id'], ),
    sa.ForeignKeyConstraint(['director_id'], ['directors.director_id'], ),
    sa.PrimaryKeyConstraint('bank_account_id')
    )
    op.create_table('directors',
    sa.Column('director_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('surname', sa.TEXT(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('sex', sa.TEXT(), nullable=True),
    sa.CheckConstraint("sex IN ('m', 'f')"),
    sa.PrimaryKeyConstraint('director_id')
    )
    # ### end Alembic commands ###
