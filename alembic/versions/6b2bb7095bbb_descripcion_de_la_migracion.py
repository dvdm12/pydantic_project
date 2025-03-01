"""descripcion de la migracion

Revision ID: 6b2bb7095bbb
Revises: f5ed57ab945e
Create Date: 2024-09-07 13:03:06.592983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6b2bb7095bbb'
down_revision: Union[str, None] = 'f5ed57ab945e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'first_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('employees', 'last_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('employees', 'email',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.drop_index('email', table_name='employees')
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=True)
    op.create_index(op.f('ix_employees_first_name'), 'employees', ['first_name'], unique=False)
    op.create_index(op.f('ix_employees_id'), 'employees', ['id'], unique=False)
    op.create_index(op.f('ix_employees_last_name'), 'employees', ['last_name'], unique=False)
    op.alter_column('tasks', 'task_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('tasks', 'status',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.create_index(op.f('ix_tasks_id'), 'tasks', ['id'], unique=False)
    op.create_index(op.f('ix_tasks_status'), 'tasks', ['status'], unique=False)
    op.create_index(op.f('ix_tasks_task_name'), 'tasks', ['task_name'], unique=False)
    op.drop_constraint('fk_employee', 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key('fk_employee', 'tasks', 'employees', ['employee_id'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_tasks_task_name'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_status'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_id'), table_name='tasks')
    op.alter_column('tasks', 'status',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('tasks', 'task_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.drop_index(op.f('ix_employees_last_name'), table_name='employees')
    op.drop_index(op.f('ix_employees_id'), table_name='employees')
    op.drop_index(op.f('ix_employees_first_name'), table_name='employees')
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.create_index('email', 'employees', ['email'], unique=True)
    op.alter_column('employees', 'email',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('employees', 'last_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('employees', 'first_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###
