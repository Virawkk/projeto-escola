"""Criação inicial do banco de dados

Revision ID: b35e1ba069e4
Revises: 
Create Date: 2024-12-03 18:31:28.171000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b35e1ba069e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aluno')
    op.drop_table('usuario')
    op.drop_table('professor')
    op.drop_table('nota')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nota',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('disciplina', sa.VARCHAR(length=100), nullable=False),
    sa.Column('nota', sa.FLOAT(), nullable=False),
    sa.Column('aluno_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['aluno_id'], ['aluno.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professor',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=100), nullable=False),
    sa.Column('foto_url', sa.VARCHAR(length=200), nullable=True),
    sa.Column('materia', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=100), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
    sa.Column('senha', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('aluno',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=100), nullable=False),
    sa.Column('foto_url', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
