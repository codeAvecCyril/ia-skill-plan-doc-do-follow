# UI Map

> **Last Updated**: {date}

<!-- LIVING DOC — the single global truth for how users navigate the application.
     Every UI feature MUST register its entry point here when its PRD is written
     (plan/feat step 3); do/verify checks the shipped feature matches this map. -->

## Navigation Structure

```
{Root / main menu}
├── {Section}
│   ├── {Screen} — {route}
│   └── {Screen} — {route}
└── {Section}
```

## Screens

| Screen | Route/URL | Entry point (how users get there) | Feature | Status |
| ------ | --------- | --------------------------------- | ------- | ------ |
| {name} | {path}    | {menu item / button / link}       | E{n} F{n} | ⚪    |

## Global UI Conventions

- {where primary actions live, how sub-navigation works, modal vs page policy, …}

## Change Log

- {date} — E{n} F{n}: {what was added/moved, one sentence}
