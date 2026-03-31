# TODO

## Phase 0: scaffold cleanup
- [x] Define repository structure for bot/app/docs/deploy/tests.
- [x] Set up typed settings, DB foundation, Alembic, and basic bot wiring.

## Phase 1: single-node kernel backend integration
- [ ] Implement real health check and peer operations in `KernelAwgBackend`.
- [ ] Add node status synchronization flow.

## Phase 2: subscription flows
- [ ] Define subscription state transitions and renewal rules.
- [ ] Add minimal user-facing subscription status responses.

## Phase 3: profile generation/export
- [ ] Implement profile rendering and export delivery flow.
- [ ] Add audit events for profile lifecycle actions.

## Phase 4: second node support
- [ ] Add assignment policy for `ProfileNode` across two nodes.
- [ ] Add operational checks for node failover readiness.

## Phase 5: anti-abuse
- [ ] Define anti-abuse strategy and data model additions.
- [ ] Add rate-limit or anomaly-control policy.

## Phase 6: referrals
- [ ] Define referral domain model and reward rules.
- [ ] Add referral accounting and moderation hooks.

## Phase 7: hardening
- [ ] Strengthen observability and error handling.
- [ ] Add runbooks and production operation checklists.
