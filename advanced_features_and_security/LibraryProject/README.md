# Advanced Features and Security

## Task 1: Permissions and Groups Setup

This project utilizes Django's groups and permissions system to manage access control for the `bookshelf` application.

### Groups Configuration

The following groups are intended to be set up in the Django Admin panel:

-   **Viewers**: Assigned the `can_view_book` permission. Can only see the list of books.
-   **Editors**: Assigned `can_view_book`, `can_create_book`, and `can_edit_book` permissions. Can manage book entries but cannot delete them.
-   **Admins**: Assigned all custom book permissions, giving them full control.

### Custom Permissions

The `bookshelf.Book` model defines the following custom permissions in its `Meta` class:

-   `can_view_book`
-   `can_create_book`
-   `can_edit_book`
-   `can_delete_book`

### View Enforcement

Access to views in `bookshelf/views.py` is restricted using the `@permission_required` decorator. This ensures that only users with the appropriate permissions, either directly or through a group, can perform certain actions like creating or editing books.