"""Weather model.

Revision ID: 990a2d88f246
Revises: 
Create Date: 2021-07-04 12:59:42.489967
"""

from alembic import op
import sqlalchemy as sa


revision = "990a2d88f246"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "weather",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("datetime", sa.DateTime(), nullable=False),
        sa.Column("temp", sa.Integer(), nullable=False),
        sa.Column("feels_like", sa.Integer(), nullable=False),
        sa.Column("condition", sa.String(length=22), nullable=False),
        sa.Column("wind_speed", sa.Integer(), nullable=False),
        sa.Column("wind_dir", sa.String(length=2), nullable=False),
        sa.Column("pressure_mm", sa.Integer(), nullable=False),
        sa.Column("pressure_pa", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("weather")
