from behave import *
from todo_list import ToDoList, Task

@given('the to-do list is empty')
def step_impl(context):
    context.todo = ToDoList()

@when('the user adds a task "{title}"')
def step_impl(context, title):
    context.todo.add_task(title)

@then('the to-do list should contain "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert title in titles

@given('the to-do list contains the following tasks:')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.output = [task.title for task in context.todo.list_tasks()]

@then('the output should contain:')
def step_impl(context):
    for row in context.table:
        assert row['Task'] in context.output

# MARK COMPLETED - Paso específico con estado
@given('the to-do list contains a task "{title}" with status "{status}"')
def step_impl(context, title, status):
    context.todo = ToDoList()
    task = Task(title, status=status)
    context.todo.tasks.append(task)

@when('the user marks task "{title}" as completed')
def step_impl(context, title):
    context.todo.mark_completed(title)

@then('the to-do list should show task "{title}" as completed')
def step_impl(context, title):
    for t in context.todo.tasks:
        if t.title == title:
            assert t.status == "Completed"

# CLEAR LIST - Usa el mismo paso que LIST TASKS pero sin tabla
@given('the to-do list has some tasks')
def step_impl(context):
    context.todo = ToDoList()
    context.todo.add_task("Buy groceries")
    context.todo.add_task("Pay bills")

@when('the user clears the to-do list')
def step_impl(context):
    context.todo.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo.tasks) == 0

# DELETE TASK
@when('the user deletes the task "{title}"')
def step_impl(context, title):
    context.todo.delete_task(title)

@then('the to-do list should not contain "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.todo.tasks]
    assert title not in titles