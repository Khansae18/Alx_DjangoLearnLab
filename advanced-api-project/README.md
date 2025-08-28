## Book API Advanced Queries

### Filtering
- Filter by exact match:
  `/api/books/?title=Python 101`
  `/api/books/?author=John Doe`
  `/api/books/?publication_year=2022`

### Searching
- Partial match search on `title` or `author`:
  `/api/books/?search=Python`

### Ordering
- Order by fields:
  `/api/books/?ordering=title`  (ascending)
  `/api/books/?ordering=-publication_year` (descending)
