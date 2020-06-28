"""Add TodoList table.

Revision ID: 8e895ad07906
Revises: 3767e39832f7
Create Date: 2020-06-28 04:15:56.904503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e895ad07906'
down_revision = '3767e39832f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # change the nullable to True to force the Foreign key to accept NULL
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.create_foreign_key(None, 'todos', 'lists', ['list_id'], ['id'])
    # Insert a new list, 'My Tasks', to map all existing tasks
    op.execute('INSERT INTO lists(id, name) VALUES (1, \'My Tasks\');')
    # update the todos.list_id of current tasks to map to 1
    op.execute('UPDATE todos SET list_id = 1 WHERE list_id IS NULL;')
    # Alter the nullable attribute of the todos.list_id to False
    op.alter_column('todos', sa.Column('list_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column('todos', 'list_id')
    op.drop_table('lists')
    # ### end Alembic commands ###
