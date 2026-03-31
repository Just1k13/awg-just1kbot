# TODO

## Current: backend/helper foundation with deterministic mutation wiring
- [x] Keep backend/helper boundary explicit and typed.
- [x] Add application-level single-node preflight checks.
- [x] Add helper protocol DTOs for read-only and mutation command envelopes.
- [x] Add deterministic helper adapter stub for read-only and mutation commands.
- [x] Route kernel backend read-only + mutation methods via helper client/protocol.
- [x] Convert helper command failures into `KernelAwgBackendError`.
- [x] Keep runtime commands uncalled (no subprocess/system integration).

## Next: real helper transport boundary (still no runtime execution in app process)
- [ ] Define transport contract for `ProcessHelperClient` (process/IPC shape only).
- [ ] Implement real transport serialization/deserialization for helper envelopes.
- [ ] Document transport-level error mapping and retry/no-retry policy.

## Later: subscription flows
- [ ] Define subscription state transitions and renewal rules.
- [ ] Add minimal user-facing subscription status responses.

## Later: profile generation/export
- [ ] Implement profile rendering and export delivery flow.
- [ ] Add audit events for profile lifecycle actions.

## Later: second node support
- [ ] Add assignment policy for `ProfileNode` across two nodes.
- [ ] Add operational checks for node failover readiness.

## Later: anti-abuse
- [ ] Define anti-abuse strategy and data model additions.
- [ ] Add rate-limit or anomaly-control policy.

## Later: referrals
- [ ] Define referral domain model and reward rules.
- [ ] Add referral accounting and moderation hooks.
