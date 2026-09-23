import enum


class RecipeDifficulty(enum.IntEnum):
    Easy = 1
    Medium = 2
    Hard = 3
    Expert = 4


class RecipeStatus(enum.IntEnum):
    Draft = 0
    Published = 1
    Archived = 2


class UserRole(str, enum.Enum):
    Guest = "Guest"
    Author = "Author"
    Admin = "Admin"
