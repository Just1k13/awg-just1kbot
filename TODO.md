# TODO

## Current: helper contract + preflight + read-only integration planning
- [x] Keep backend/helper boundary explicit and typed.
- [x] Add application-level single-node preflight checks.
- [x] Add read-only runtime inspection service skeleton.
- [ ] Keep kernel backend operations as stubs only.

## Next: minimal safe helper-facing wiring / protocol draft
- [ ] Define typed helper request/response envelopes for read-only commands.
- [ ] Document command/versioning constraints before mutating operations.

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
