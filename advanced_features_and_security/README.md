
# Advanced Features and Security - Permissions Setup

This project uses Django's built-in groups and permissions system to control access to the bookshelf application.

## Groups


The following groups should be configured in the Django Admin panel:

- **Viewers**: Can only view books. (Permission: `can_view_book`)
- **Editors**: Can view, create, and edit books. (Permissions: `can_view_book`, `can_create_book`, `can_edit_book`)
- **Admins**: Can perform all actions on books. (All `book` permissions)

## Custom Permissions


The `bookshelf.Book` model defines the following custom permissions:

- `can_view_book`: Allows viewing a book.
- `can_create_book`: Allows creating a new book.
- `can_edit_book`: Allows editing an existing book.
- `can_delete_book`: Allows deleting a book.

## View Enforcement

Views in `bookshelf/views.py` are protected using the `@permission_required` decorator to ensure only users with the appropriate permissions can access them.