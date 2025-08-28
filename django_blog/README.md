## Comment System
- Each post can have multiple comments.
- Authenticated users can add, edit, and delete their own comments.
- Non-authenticated users can only read comments.
- URLs:
  - /post/<post_id>/comment/ → Add comment
  - /comment/<comment_id>/update/ → Edit comment
  - /comment/<comment_id>/delete/ → Delete comment

# Tagging & Search Features

## Add Tags
- When creating/editing a post, enter tags separated by commas (e.g., `django, python, web`).

## View Tags
- Tags appear under each post.
- Clicking a tag shows all posts with that tag.

## Search Posts
- Use the search bar at the top of the post list.
- Searches across titles, content, and tags.
