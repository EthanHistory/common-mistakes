# Common Mistakes in Pytest Mock Patch

> ⚠️ **Summary**: When mocking a class with `@patch`, always use the path where the class is *imported*, not where it's *defined*!

## Example Scenario


In our example, we have a `UserService` class that depends on a `Database` class. The `Database` class is defined in `source.database` but is imported in `source.user_service`.

### Reproduce test

```bash
cd pytest_mock_path
poetry install
poetry run pytest
```

### Code Structure
- `UserService` imports `Database` from `source.database`
- When `UserService` is instantiated, it creates a new `Database` instance
- The `get_user` method uses the database to query user information

### The Wrong Way ❌

This test fails because we're patching the wrong path. Even though `Database` is defined in `source.database`, patching this path won't affect where the class is actually being used.

When `UserService` creates a new `Database` instance, it's using the import from `source.database`, not the original definition. As a result:

- The mock is never used
- A real `Database` instance is created instead
- The test assertions fail because the real database is used

### The Correct Way ✅

This test succeeds because:

- We patch `Database` at the location where it's imported and used
- When `UserService` creates a new `Database` instance, it uses our mock instead
- We can verify that the database query was called with the correct SQL statement

## Key Takeaway

When using `@patch` in Python tests, always patch the path where the object is *imported*, not where it's defined. This ensures that your mock actually intercepts the object creation at the point where it's being used.

In this case:

- ❌ `source.database.Database` - where the class is defined
- ✅ `source.user_service.Database` - where the class is imported and used