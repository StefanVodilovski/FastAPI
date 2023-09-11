"""create users table again

Revision ID: 079e705d82bc
Revises: e18b8c369e03
Create Date: 2023-08-31 17:59:08.213780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '079e705d82bc'
down_revision: Union[str, None] = 'e18b8c369e03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        # op.create_table('users', sa.Column('id',sa.Integer(), primary_key=True, nullable = False),
        #             sa.Column('email',sa.String(50), nullable = False, unique=True),
        #             sa.Column('password',sa.String(100), nullable = False),
        #             sa.Column('created_at',sa.TIMESTAMP(timezone=True), server_default= sa.text('CURRENT_TIMESTAMP')))
        pass


def downgrade() -> None:
#     op.drop_table('users')
    pass
