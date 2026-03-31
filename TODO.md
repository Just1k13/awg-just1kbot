# TODO

## Current: single-node preflight + helper contract
- [x] Keep backend/helper boundary explicit and typed.
- [x] Add application-level single-node preflight checks.
- [ ] Keep kernel backend operations as stubs only.

## Next: safe read-only kernel integration planning
- [ ] Define read-only helper-facing wiring for health/runtime inspection.
- [ ] Document safe integration constraints before any mutating operations.

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
