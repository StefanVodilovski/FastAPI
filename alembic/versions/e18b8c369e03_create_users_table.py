"""create users table

Revision ID: e18b8c369e03
Revises: 60652f5185f1
Create Date: 2023-08-31 15:43:22.129235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e18b8c369e03'
down_revision: Union[str, None] = '60652f5185f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# class User(Base):
#     __tablename__ = 'users'
    
#     id = Column(Integer, primary_key=True, nullable = False)
#     email = Column(String(50), nullable = False, unique=True)
#     password = Column(String(100), nullable = False)
#     created_at = Column(TIMESTAMP(timezone=True), server_default= text('CURRENT_TIMESTAMP'))


def upgrade() -> None:
        op.create_table('users', sa.Column('id',sa.Integer(), primary_key=True, nullable = False),
                    sa.Column('email',sa.String(50), nullable = False, unique=True),
                    sa.Column('password',sa.String(100), nullable = False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True), server_default= sa.text('CURRENT_TIMESTAMP')))
        pass


def downgrade() -> None:
    op.drop_table('users')
    pass
