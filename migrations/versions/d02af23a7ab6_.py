"""empty message

Revision ID: d02af23a7ab6
Revises: 
Create Date: 2021-06-01 11:16:22.390162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd02af23a7ab6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audio',
    sa.Column('danceability', sa.FLOAT(), nullable=True),
    sa.Column('energy', sa.FLOAT(), nullable=True),
    sa.Column('acousticness', sa.FLOAT(), nullable=True),
    sa.Column('instrumentalness', sa.FLOAT(), nullable=True),
    sa.Column('valence', sa.FLOAT(), nullable=True),
    sa.Column('track_id', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('track_id')
    )
    op.create_table('playlist',
    sa.Column('artist_id', sa.VARCHAR(), nullable=False),
    sa.Column('artist_name', sa.VARCHAR(), nullable=False),
    sa.Column('track_id', sa.VARCHAR(), nullable=True),
    sa.Column('track_name', sa.VARCHAR(), nullable=False),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.Column('images', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['track_id'], ['audio.track_id'], ),
    sa.PrimaryKeyConstraint('artist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playlist')
    op.drop_table('audio')
    # ### end Alembic commands ###
