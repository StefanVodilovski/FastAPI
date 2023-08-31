"""create posts table 

Revision ID: 60652f5185f1
Revises: 
Create Date: 2023-08-31 15:26:39.784514

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60652f5185f1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

    # __tablename__ = "posts"
    
    # id = Column(Integer, primary_key=True, nullable = False)
    # title = Column(String(50), nullable = False)
    # content = Column(String(100), nullable = False)
    # published = Column(Boolean, server_default='1', nullable = False)
    # created_at = Column(TIMESTAMP(timezone=True), server_default= text('CURRENT_TIMESTAMP'))
    # owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False)
    
    # owner = relationship('User')

def upgrade() -> None:
    op.create_table('posts', sa.Column('id',sa.Integer, primary_key=True, nullable = False),
                    sa.Column('title',sa.String(50), nullable = False),
                    sa.Column('content',sa.String(100), nullable = False),
                    sa.Column('published',sa.Boolean, server_default='1', nullable = False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True), server_default= sa.text('CURRENT_TIMESTAMP'))
                    )



def downgrade() -> None:
    op.drop_table('posts')
    pass
