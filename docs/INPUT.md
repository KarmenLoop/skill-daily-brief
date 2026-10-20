# Input and output

Supply a UTF-8 JSON object (maximum 10 MiB). Use `--input PATH` for a file or `--input -` for standard input. Run `--version` to inspect the installed helper version. Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| date | Working date YYYY-MM-DD. |
| available_minutes | Nonnegative integer. |
| tasks | Objects: unique id, title, priority (1 highest to 5 lowest), minutes, status (ready/blocked/done), optional due YYYY-MM-DD. |

## Example

```json
{
  "date": "2026-10-19",
  "available_minutes": 90,
  "tasks": [
    {
      "id": "a",
      "title": "Send requested proposal",
      "priority": 1,
      "minutes": 40,
      "status": "ready",
      "due": "2026-10-18"
    },
    {
      "id": "b",
      "title": "Review notes",
      "priority": 3,
      "minutes": 60,
      "status": "ready"
    },
    {
      "id": "c",
      "title": "Wait for invoice",
      "priority": 2,
      "minutes": 20,
      "status": "blocked",
      "due": "2026-10-19"
    }
  ]
}
```

## Result

agenda, blocked, deferred, remaining_minutes, and date. Each task retains its ID and deadline class.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
