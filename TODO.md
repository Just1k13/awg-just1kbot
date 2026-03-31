# TODO

## Current: consistency cleanup around foundation/backend/protocol/adapter
- [x] Keep backend/helper boundary explicit and typed.
- [x] Add application-level single-node preflight checks.
- [x] Add read-only helper protocol DTO draft for request/result envelopes.
- [x] Add deterministic read-only helper adapter stub.
- [x] Add runtime inspection foundation on backend read-only methods.
- [ ] Keep kernel backend operations as stubs only.

## Next: helper-facing client/gateway boundary (still no runtime execution)
- [x] Add explicit client/gateway interface between backend services and helper adapter.
- [x] Keep runtime commands uncalled (no subprocess/system integration).

## Next: real helper transport boundary planning
- [ ] Define transport contract for `ProcessHelperClient` (process/IPC shape only).
- [ ] Keep runtime commands uncalled until transport safety constraints are documented.

## Later: mutation protocol expansion
- [ ] Expand transport DTOs for mutation commands when helper execution work starts.
- [ ] Document mutation safety constraints before implementation.

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
