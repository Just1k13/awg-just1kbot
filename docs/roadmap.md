# Roadmap

## Current phase
Foundation scaffold + backend boundary + single-node preflight + helper protocol DTOs + deterministic adapter/client stubs + backend wiring for read-only and mutation methods + runtime inspection foundation.

## Planned phases
1. Real helper transport boundary behind helper client/gateway (still without runtime execution in app process).
2. Subscription flows.
3. Profile generation/export.
4. Second node support.
5. Anti-abuse controls.
6. Referrals.
7. Hardening and operations.

## Phase notes
- Current phase includes backend interfaces/stubs, helper command contract, read-only + mutation protocol DTOs, deterministic adapter stub, helper-facing client boundary, `KernelAwgBackend` wiring, and runtime inspection service.
- Real kernel integration is not implemented yet.
- Node-helper implementation is not started yet.
- Runtime/system commands are still not invoked by the app.
- `reconcile` is available at protocol/client/adapter level as the next operational command.
