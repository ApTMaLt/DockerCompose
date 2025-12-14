"""init tasks

Revision ID: 20251214_init_tasks
Revises:
Create Date: 2025-12-14 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20251214_init_tasks'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('tasks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('tasks')