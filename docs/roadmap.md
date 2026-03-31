# Roadmap

## Current phase
Foundation scaffold + backend boundary + single-node preflight + read-only helper protocol + adapter stub.

## Planned phases
1. Real helper-facing execution boundary replacing stub adapter (same protocol DTO contract).
2. Subscription flows.
3. Profile generation/export.
4. Second node support.
5. Anti-abuse controls.
6. Referrals.
7. Hardening and operations.

## Phase notes
- Current phase includes backend interfaces/stubs, helper command contract, read-only protocol DTOs,
  and deterministic adapter stub behavior.
- Real kernel integration is not implemented yet.
- Node-helper implementation is not started yet.
- Runtime/system commands are still not invoked by the app.
- Peer lifecycle operations are not implemented yet.
