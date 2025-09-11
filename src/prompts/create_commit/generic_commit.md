# Git Commit Template

## Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

## Components

### Type (Required)
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, semicolons, etc.)
- **refactor**: Code refactoring without changing functionality
- **test**: Adding or updating tests
- **chore**: Maintenance tasks, build changes, dependency updates

### Scope (Optional)
- Component, module, or area affected (e.g., auth, api, ui)

### Subject (Required)
- Brief description (50 chars max)
- Use imperative mood ("add" not "added")
- No period at the end
- Lowercase first letter

### Body (Optional)
- Detailed explanation of what and why
- Wrap at 72 characters
- Use imperative mood

### Footer (Optional)
- Breaking changes: `BREAKING CHANGE: description`
- Issue references: `Closes #123`, `Fixes #456`

## Examples

### Simple fix
```
fix: resolve login validation error
```

### Feature with scope
```
feat(auth): add two-factor authentication

Implement TOTP-based 2FA for enhanced security.
Users can now enable 2FA in account settings.

Closes #234
```

### Breaking change
```
refactor(api): update user endpoint response format

Change user object structure to include nested profile data.
This improves consistency across all user-related endpoints.

BREAKING CHANGE: user.name is now user.profile.name
```