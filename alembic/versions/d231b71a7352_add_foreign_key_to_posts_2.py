"""add foreign key to posts 2

Revision ID: d231b71a7352
Revises: ecbf6b446680
Create Date: 2023-08-31 18:12:08.007006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd231b71a7352'
down_revision: Union[str, None] = 'ecbf6b446680'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users"
                          , local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass

def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts','owner_id')
    pass
