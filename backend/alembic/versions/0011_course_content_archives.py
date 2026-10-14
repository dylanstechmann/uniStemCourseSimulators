"""Store complete public course packages at enrollment version pinning."""

import sqlalchemy as sa

from alembic import op

revision = "0011"
down_revision = "0010"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "course_content_archives",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("course_id", sa.String(100), nullable=False),
        sa.Column("content_version", sa.String(100), nullable=False),
        sa.Column("archive_sha256", sa.String(64), nullable=False),
        sa.Column("archive_bytes", sa.LargeBinary(), nullable=False),
        sa.Column("files_sha256_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint(
            "course_id", "content_version", name="uq_course_content_archive_version"
        ),
    )
    op.create_index(
        "ix_course_content_archives_lookup",
        "course_content_archives",
        ["course_id", "content_version"],
    )


def downgrade():
    op.drop_index("ix_course_content_archives_lookup", table_name="course_content_archives")
    op.drop_table("course_content_archives")
