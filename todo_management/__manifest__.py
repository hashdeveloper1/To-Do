{
    'name': 'To-Do List',
    'author': 'Hashem Ahmed',
    'category': '',
    'description':
    """
      Odoo Task Management Addon :
          This addon enhances Odoo's project management capabilities by providing advanced features for task tracking,
          prioritization, and collaboration.
          Designed for teams of all sizes, it helps streamline workflows,
          improve task visibility, and boost productivity.
    """,
    'version': '16.0.0.1.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'views/todo_project_view.xml',
    ],
    'application': True,
}
