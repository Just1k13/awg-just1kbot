# Domain model

## Entities in current schema
- `User`: Telegram identity with optional `ref_code` field (no referral logic yet).
- `Node`: future AWG node/server descriptor.
- `Subscription`: minimal subscription state with time window.
- `DeviceSlot`: logical device slot per user.
- `Profile`: logical access profile linked to a slot.
- `ProfileNode`: mapping profile to node for future multi-node support.
- `AuditLog`: minimal action journal.

## Explicitly missing by design
- Payment tables.
- Referral/reward tables.
- Session lease or abuse-control tables.

These are intentionally deferred to roadmap phases.
