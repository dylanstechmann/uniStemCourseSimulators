"""Preserve exact graded sources for historical appeal review."""

import sqlalchemy as sa

from alembic import op

revision = "0010"
down_revision = "0009"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "assessment_source_archives",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("course_id", sa.String(100), nullable=False),
        sa.Column("content_version", sa.String(100), nullable=False),
        sa.Column("assessment_id", sa.String(120), nullable=False),
        sa.Column("source_sha256", sa.String(64), nullable=False),
        sa.Column("source_bytes", sa.LargeBinary(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint(
            "course_id", "content_version", "assessment_id", "source_sha256",
            name="uq_assessment_source_archive_version_digest",
        ),
    )
    op.create_index(
        "ix_assessment_source_archives_lookup",
        "assessment_source_archives",
        ["course_id", "content_version", "assessment_id"],
    )


def downgrade():
    op.drop_index("ix_assessment_source_archives_lookup", table_name="assessment_source_archives")
    op.drop_table("assessment_source_archives")
