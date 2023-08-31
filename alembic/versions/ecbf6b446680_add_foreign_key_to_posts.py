"""add foreign key to posts

Revision ID: ecbf6b446680
Revises: 079e705d82bc
Create Date: 2023-08-31 18:03:34.844537

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecbf6b446680'
down_revision: Union[str, None] = '079e705d82bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.column("users_id", sa.Integer(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users"
                          , local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass

def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts','owner_id')
    pass
