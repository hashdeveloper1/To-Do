{
    'name': 'To-Do List v2',
    'author': 'Hashem Ahmed',
    'category': 'HashCustom/HashCustom',
    'description':
        """
          Odoo Task Management Addon :
              This addon enhances Odoo's project management capabilities by providing advanced features for task tracking,
              prioritization, and collaboration.
              Designed for teams of all sizes, it helps streamline workflows,
              improve task visibility, and boost productivity.
        """,
    'version': '16.0.0.2.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
    ],
    'application': True,
}
