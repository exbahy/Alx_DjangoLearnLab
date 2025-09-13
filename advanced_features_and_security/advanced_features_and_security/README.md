
# Advanced Features and Security - Permissions Setup

This project uses Django's built-in groups and permissions system to control access to the blog.

## Groups

The following groups are configured in the Django Admin panel:

- **Viewers**: Can only view posts.
- **Editors**: Can view, create, and edit posts.
- **Admins**: Can perform all actions on posts (view, create, edit, delete).

## Custom Permissions

The `blog.Post` model defines the following custom permissions:

- `can_view_post`: Allows viewing a post.
- `can_create_post`: Allows creating a new post.
- `can_edit_post`: Allows editing an existing post.
- `can_delete_post`: Allows deleting a post.

## View Enforcement

Views in `blog/views.py` are protected using the `@permission_required` decorator to ensure only users with the appropriate permissions can access them.