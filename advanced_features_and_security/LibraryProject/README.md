# LibraryProject
This is a basic Django project created for learning purposes.

# Permissions and Groups Setup

## Custom Permissions
The `Book` model (`LibraryProject/bookshelf/models.py`) defines:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Groups are automatically created via signals (`LibraryProject/bookshelf/signals.py`):
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → can_view, can_create, can_edit, can_delete

## Views
Views in `LibraryProject/bookshelf/views.py` use `@permission_required`:
- `book_list` → requires `can_view`
- `book_create` → requires `can_create`
- `book_edit` → requires `can_edit`
- `book_delete` → requires `can_delete`

## Testing
1. Create users and assign them to groups in the admin.
2. Log in with different users to verify access:
   - Viewers can only see the list.
   - Editors can add/edit books.
   - Admins can add/edit/delete books.


