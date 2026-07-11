# GitHub Flow Examples

## Feature Branch PR

```bash
git checkout main && git pull
git checkout -b feat/cursor-pagination
# ... commits ...
git push -u origin HEAD
gh pr create --title "Add cursor pagination for audit events" --body "..."
```

## Update Branch With Rebase

```bash
git fetch origin
git rebase origin/main
# fix conflicts if needed
git push --force-with-lease
```

## Draft Until Ready

```bash
gh pr create --draft --title "WIP: rewrite export worker"
# later
gh pr ready
```

## Hotfix Exception

```text
Branch: hotfix/fix-token-expiry
Target: main
PR template: pr-hotfix.md
After merge: tag/patch release if the project versions releases
```
