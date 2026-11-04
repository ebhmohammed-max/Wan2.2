# INSERT C02-S005-A — the sourced Met bulla (the one asset that must NOT be generated)

## Object, confirmed from the Met's own API on 2026-11-04

`https://collectionapi.metmuseum.org/public/collection/v1/objects/326457`

- objectID **326457** · objectName **Bulla** · title "Bulla" · culture/period **Parthian**
- date 2nd century BC – 1st century AD · medium **Un-baked clay** · 5.31 × 2.9 cm
- accession **1978.93.29** · credit line "Purchase, H. Dunscombe Colt Gift, 1978"
- region **Iran — Shahr-i Qumis (ancient Hecatompylos)**
- `isPublicDomain: **true**`
- primary image: `https://images.metmuseum.org/CRDImages/an/original/DP-40309-001.jpg`
- record page: `https://www.metmuseum.org/art/collection/search/326457`

## The blocker

The sandbox has no outbound access to `images.metmuseum.org` (`SSL_ERROR_SYSCALL`), so the public-domain file cannot be
pulled in here. Metadata is readable (the API host is reachable through the page-fetch tool); the binary is not.

Two routes that work:

1. **You drop the file in.** Right-click → Save image as `DP-40309-001.jpg` from the record page, then upload it to the v2 root
   or into `v2 · Batch 2 — Chapter 2 edits`. I will grade it to the film's look, letter it as a documentary panel, and slot it
   into INSERT C02-S005-A at the shot map's duration.
2. **Give me a Drive copy** of the same JPEG if you already have one in the research pack.

## Resolution (founder decision, 2026-11-04)

Rather than ship the INSERT empty, the founder directed the use of a **neighbouring Met bulla**. Delivered:

- object **326458 / accession 1978.93.30** — also a Parthian un-baked clay bulla, same excavation (Shahr-i Qumis),
  same 1978 Colt Gift, public domain. Photo `DP-40310-001.jpg`, obtained at 1200 x 899.
- Files: `stills/v2_insert/C02-S005-A_original_1200x899.jpg` (untouched) and `C02-S005-A_3840x2160_frame.png`.
- **The accession in MG-011's overlay must change to 1978.93.30** — see `docs/C02-S005-A_insert_caption.md`.

## What I will not do

Substitute a neighbouring object. The Met's own search surfaces Parthian/Sasanian sealings from other accessions
(e.g. object 326458, a different bulla), and using one of those would put a photograph of the wrong object under an
evidence label — the exact failure the evidence rule exists to prevent. Generated imagery can illustrate the sealing world,
but it can never sit in the INSERT.
