"""empty message

Revision ID: b253bb65435e
Revises: 
Create Date: 2020-01-29 16:42:25.146579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b253bb65435e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('client_secret', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('operation_type', sa.Enum('SELECT', 'UPDATE', 'INSERT', 'UNKNOWN', name='operationtype'), nullable=True),
    sa.Column('category', sa.Enum('READ', 'WRITE', name='operationcategory'), nullable=True),
    sa.Column('table_name', sa.String(length=512), nullable=False),
    sa.Column('count', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('operation')
    op.drop_table('client')
    # ### end Alembic commands ###
