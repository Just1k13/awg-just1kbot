# Roadmap

## Current phase
Foundation scaffold + backend boundary + single-node preflight + read-only helper protocol draft + deterministic adapter stub + helper-facing client boundary + runtime inspection foundation.

## Planned phases
1. Real helper transport boundary design behind helper client/gateway (still without runtime execution in product paths).
2. Subscription flows.
3. Profile generation/export.
4. Second node support.
5. Anti-abuse controls.
6. Referrals.
7. Hardening and operations.

## Phase notes
- Current phase includes backend interfaces/stubs, helper command contract, read-only protocol DTOs, deterministic adapter stub + helper-facing client boundary, and runtime inspection service.
- Real kernel integration is not implemented yet.
- Node-helper implementation is not started yet.
- Runtime commands are still not invoked by the app.
- Peer lifecycle operations are not implemented yet.
