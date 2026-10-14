"""Private, version-bound case responses and learner self-checks."""

import sqlalchemy as sa

from alembic import op

revision = "0012"
down_revision = "0011"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "case_drafts",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("user_id", sa.String(36), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("course_id", sa.String(100), nullable=False),
        sa.Column("case_id", sa.String(120), nullable=False),
        sa.Column("content_version", sa.String(100), nullable=False),
        sa.Column("case_sha256", sa.String(64), nullable=False),
        sa.Column("case_snapshot_json", sa.JSON(), nullable=False),
        sa.Column("response", sa.Text(), nullable=False),
        sa.Column("checked_criteria_json", sa.JSON(), nullable=False),
        sa.Column("revision", sa.Integer(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint("user_id", "course_id", "case_id", "content_version", "case_sha256",
                            name="uq_case_draft_source"),
        sa.CheckConstraint("revision >= 1", name="ck_case_draft_revision_positive"),
    )
    op.create_index("ix_case_drafts_user_id", "case_drafts", ["user_id"])


def downgrade():
    op.drop_index("ix_case_drafts_user_id", table_name="case_drafts")
    op.drop_table("case_drafts")
