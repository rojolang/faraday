"""Update risk value

Revision ID: 699402156cf4
Revises: 3eb96406e88d
Create Date: 2022-11-15 19:09:54.669437+00:00

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '699402156cf4'
down_revision = '3eb96406e88d'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    # Critical
    conn.execute("UPDATE vulnerability SET risk = 70 WHERE severity = 'critical' and risk is NULL")
    # High
    conn.execute("UPDATE vulnerability SET risk = 62 WHERE severity = 'high' and risk is NULL")
    # Medium
    conn.execute("UPDATE vulnerability SET risk = 48 WHERE severity = 'medium' and risk is NULL")
    # Low
    conn.execute("UPDATE vulnerability SET risk = 27 WHERE severity = 'low' and risk is NULL")
    # Info and Unclassified
    conn.execute("UPDATE vulnerability SET risk = 0 WHERE severity in ('informational', 'unclassified') and risk is NULL")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    ...
    # ### end Alembic commands ###