"""Persist the authored form assigned to each graded attempt."""

import sqlalchemy as sa

from alembic import op

revision = "0009"
down_revision = "0008"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "graded_assessment_assignments",
        sa.Column("id", sa.String(64), primary_key=True),
        sa.Column("enrollment_id", sa.String(36), sa.ForeignKey("enrollments.id", ondelete="CASCADE"), nullable=False),
        sa.Column(
            "assessment_instance_id", sa.String(36),
            sa.ForeignKey("assessment_instances.id", ondelete="CASCADE"), nullable=False,
        ),
        sa.Column("attempt_number", sa.Integer(), nullable=False),
        sa.Column("content_version", sa.String(100), nullable=False),
        sa.Column("source_sha256", sa.String(64), nullable=False),
        sa.Column("variant_ids_json", sa.JSON(), nullable=False),
        sa.Column("question_spec_sha256", sa.String(64), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint(
            "enrollment_id", "assessment_instance_id", "attempt_number",
            name="uq_graded_assessment_assignment_attempt",
        ),
        sa.CheckConstraint("attempt_number >= 1", name="ck_graded_assessment_assignment_attempt_positive"),
    )
    op.create_index("ix_graded_assessment_assignments_enrollment_id", "graded_assessment_assignments", ["enrollment_id"])
    op.create_index(
        "ix_graded_assessment_assignments_assessment_instance_id",
        "graded_assessment_assignments", ["assessment_instance_id"],
    )


def downgrade():
    op.drop_index(
        "ix_graded_assessment_assignments_assessment_instance_id",
        table_name="graded_assessment_assignments",
    )
    op.drop_index("ix_graded_assessment_assignments_enrollment_id", table_name="graded_assessment_assignments")
    op.drop_table("graded_assessment_assignments")
