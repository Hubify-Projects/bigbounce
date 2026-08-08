# P4 strict-primary release overlay — v1.0.259

This overlay changes the **primary analysis contract**, not the 8,474,531-row
catalog bytes. It consumes the immutable catalog identified in `SCHEMA.json`
and requires:

```text
primary_hc == true and raw_flip_qc_unsafe == false
```

The retained 10,000-draw array uses fixed-occupancy galaxy-label randomization
on that exact strict selection. The result is `z_moment=+0.6346508534` and
one-sided add-one rank `p=0.2376762324`.

The unsafe predicate was finalized during post-review corrective work after the
earlier result had been inspected. This is not represented as preregistered or
blinded. The result is an observed-label descriptive isotropy null, not a
physical or primordial amplitude bound.
