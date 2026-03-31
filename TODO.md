# TODO

## Current: single-node preflight + helper protocol draft
- [x] Keep backend/helper boundary explicit and typed.
- [x] Add application-level single-node preflight checks.
- [x] Add read-only helper protocol DTO draft for request/result envelopes.
- [ ] Keep kernel backend operations as stubs only.

## Next: helper-facing adapter stub (no runtime execution)
- [ ] Add adapter stub that accepts protocol DTOs and returns deterministic stub results.
- [ ] Keep runtime commands uncalled (no subprocess/system integration).

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
