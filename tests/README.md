# Tests

Regression tests pinning the behavior of helpers extracted during the 2026
cleanup. They exist because a live OBP/HBP network with real DMR audio cannot be
reproduced in a dev environment, so the routing helpers are validated in
isolation instead.

- `test_acl.py` — `HBSYSTEM.dmrd_acl_check()` (the shared master/peer ACL logic):
  PERMIT/DENY matching, per-timeslot scoping, and the once-per-stream drop logging.
- `test_lc.py` — `gen_lcs()` and `embed_lc()` from `bridge.py`: Link Control
  generation and the DMR payload LC rewrite used by all four group-routing paths.
- `test_xlx_link.py` — the XLX reflector module link: packet construction
  (`send_xlx_link`/`xlx_link_module`), `expand_xlx_bridges()` and its guards, and
  `XLX_MODULE` config validation. The acceptance gates asserted here are
  transcribed from xlxd's own parser, because a reflector never acknowledges a
  link and puts no module identity on the wire — a malformed packet is silently
  discarded, so there is no runtime signal to fall back on. One test reproduces
  the field-proven 2019 reference bursts byte for byte.

## Running

From the repo root, using the project virtualenv (which has `twisted`,
`dmr_utils3`, and `bitarray`):

```
venv/bin/python -m unittest discover -s tests -v
```

Pure stdlib `unittest` — no extra dependencies. They also run under `pytest` if
you have it installed (`venv/bin/python -m pytest tests`).
