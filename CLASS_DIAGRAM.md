# Class Diagram - Sistem Manajemen Perpustakaan

## ASCII Class Diagram

```
                              ┌────────────────────────────────────┐
                              │   <<abstract>>                     │
                              │      LibraryItem                   │
                              ├────────────────────────────────────┤
                              │ - __id: int                        │
                              │ - __title: str                     │
                              │ # _author: str                     │
                              │ # _publication_year: int           │
                              │ # _is_available: bool              │
                              │ # _borrowed_date: datetime         │
                              │ - _id_counter: int (class var)     │
                              ├────────────────────────────────────┤
                              │ + __init__(title, author, year)    │
                              │ + property id() -> int             │
                              │ + property title() -> str          │
                              │ + property author() -> str         │
                              │ + property is_available() -> bool  │
                              │ + get_item_type()* -> str          │
                              │ + get_description()* -> str        │
                              │ + get_info() -> str                │
                              │ + borrow() -> bool                 │
                              │ + return_item() -> bool            │
                              │ + __str__() -> str                 │
                              └──────────────┬─────────────────────┘
                                             │
                                             │ inherits
                     ┌───────────────────────┴───────────────────────┐
                     │                                               │
         ┌───────────▼──────────────┐                  ┌─────────────▼────────────────┐
         │         Book             │                  │         Magazine             │
         ├──────────────────────────┤                  ├──────────────────────────────┤
         │ - __isbn: str            │                  │ - __issue_number: int        │
         │ # _pages: int            │                  │ # _month: str                │
         │ # _genre: str            │                  │ # _topic: str                │
         ├──────────────────────────┤                  ├──────────────────────────────┤
         │ + __init__(...)          │                  │ + __init__(...)              │
         │ + property isbn() -> str │                  │ + property issue_number()    │
         │ + property pages() -> int│                  │ + property month() -> str    │
         │ + property genre() -> str│                  │ + property topic() -> str    │
         │ + get_item_type() -> str │                  │ + property publisher() -> str│
         │ + get_description() -> str│                 │ + get_item_type() -> str     │
         │ + get_info() -> str      │                  │ + get_description() -> str   │
         │ + __str__() -> str       │                  │ + get_info() -> str          │
         └──────────────────────────┘                  │ + __str__() -> str           │
                     │                                 └──────────────────────────────┘
                     │                                               │
                     │                                               │
                     │          manages multiple                    │
                     └───────────────┐           ┌───────────────────┘
                                     │           │
                           ┌─────────▼───────────▼──────────┐
                           │         Library                │
                           ├────────────────────────────────┤
                           │ - __name: str                  │
                           │ - __items: List[LibraryItem]   │
                           │ - __total_borrowed: int        │
                           ├────────────────────────────────┤
                           │ + __init__(name: str)          │
                           │ + property name() -> str       │
                           │ + property total_items() -> int│
                           │ + property available_items()   │
                           │ + property borrowed_items()    │
                           │ + add_item(item) -> bool       │
                           │ + remove_item(id) -> bool      │
                           │ + display_all_items() -> None  │
                           │ + display_available_items()    │
                           │ + search_by_title(title)       │
                           │ + search_by_id(id)             │
                           │ + search_by_author(author)     │
                           │ + borrow_item(id) -> bool      │
                           │ + return_item(id) -> bool      │
                           │ + get_statistics() -> None     │
                           │ - __display_search_results()   │
                           │ + __str__() -> str             │
                           └────────────────────────────────┘
```

## Relationships

### Inheritance (IS-A Relationship)
- `Book` **IS-A** `LibraryItem`
- `Magazine` **IS-A** `LibraryItem`

### Composition (HAS-A Relationship)
- `Library` **HAS-MANY** `LibraryItem` objects

### Dependency
- `Library` depends on `LibraryItem` (and its subclasses)
- Methods in `Library` accept `LibraryItem` type

## Legend

| Symbol | Meaning |
|--------|---------|
| `-`    | Private attribute/method |
| `#`    | Protected attribute/method |
| `+`    | Public attribute/method |
| `*`    | Abstract method (must be implemented by subclass) |
| `▼`    | Inheritance arrow (points to parent) |

## Method Categories

### LibraryItem (Abstract Base Class)
**Abstract Methods** (must be implemented):
- `get_item_type()` - Returns type of item
- `get_description()` - Returns detailed description

**Concrete Methods** (inherited by subclasses):
- `get_info()` - Returns formatted information (can be overridden)
- `borrow()` - Mark item as borrowed
- `return_item()` - Mark item as returned

**Properties**:
- `id` (read-only)
- `title` (read-write with validation)
- `author` (read-only)
- `is_available` (read-only)

### Book (Concrete Class)
**Implements abstract methods**:
- `get_item_type()` → "Book"
- `get_description()` → Detailed book description

**Overrides**:
- `get_info()` - Adds book-specific information

**Additional properties**:
- `isbn` (read-only)
- `pages` (read-only)
- `genre` (read-only)

### Magazine (Concrete Class)
**Implements abstract methods**:
- `get_item_type()` → "Magazine"
- `get_description()` → Detailed magazine description

**Overrides**:
- `get_info()` - Adds magazine-specific information

**Additional properties**:
- `issue_number` (read-only)
- `month` (read-only)
- `topic` (read-only)
- `publisher` (alias for author)

### Library (Manager Class)
**Item Management**:
- `add_item()` - Add new item to collection
- `remove_item()` - Remove item from collection

**Display Methods**:
- `display_all_items()` - Show all items grouped by type
- `display_available_items()` - Show only available items

**Search Methods**:
- `search_by_title()` - Search by title (partial match)
- `search_by_id()` - Search by unique ID
- `search_by_author()` - Search by author/publisher

**Transaction Methods**:
- `borrow_item()` - Borrow an item
- `return_item()` - Return an item

**Analytics**:
- `get_statistics()` - Display library statistics

**Properties**:
- `name` (read-only)
- `total_items` (computed)
- `available_items` (computed)
- `borrowed_items` (computed)

## Design Patterns Used

### 1. Template Method Pattern
`LibraryItem` defines the template with abstract methods that subclasses must implement.

### 2. Factory-like Behavior
Library can work with any `LibraryItem` subclass through polymorphism.

### 3. Information Expert
Each class manages its own data and behavior:
- `LibraryItem` manages item state
- `Book` manages book-specific data
- `Magazine` manages magazine-specific data
- `Library` manages collection

### 4. Encapsulation
All data is protected with private/protected access modifiers and accessed through properties.

## Object Interaction Example

```
User Program (main.py)
        |
        | creates
        ▼
    Library("Perpustakaan Universitas")
        |
        | add_item()
        ▼
    Book("Python Programming", "John Smith", 2022, "978-123", 350, "Programming")
        |
        | inherits from
        ▼
    LibraryItem
        |
        | implements abstract methods
        | get_item_type() → "Book"
        | get_description() → "Buku 'Python Programming'..."
        |
        ▼
    Library manages List[LibraryItem]
        |
        | polymorphic calls
        ▼
    item.get_info()  # Calls Book.get_info() or Magazine.get_info()
```

## Key OOP Principles Demonstrated

1. **Abstraction**: Abstract base class `LibraryItem`
2. **Inheritance**: `Book` and `Magazine` extend `LibraryItem`
3. **Encapsulation**: Private/protected attributes with properties
4. **Polymorphism**: Different behavior for same method call

---

This diagram represents the complete structure of the Library Management System.
