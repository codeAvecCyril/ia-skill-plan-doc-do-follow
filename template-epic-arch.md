# Epic Architecture

> **Code**: E{n}
>
> **Slug**: e{n}-{epic-name} (e.g., e2-orm-discovery)
>
> **Priority**: P{0|1|2}

## System Overview
[High-level diagram or description of the system components]

## Component Breakdown
1. **Component 1**: [Purpose and responsibilities]
2. **Component 2**: [Purpose and responsibilities]
3. **Component 3**: [Purpose and responsibilities]

## Data Models
[Entity Relationship Diagram (ERD) or description]

### Key Entities
- **Entity 1**: [attributes and relationships]
- **Entity 2**: [attributes and relationships]

## API Specifications

### Endpoint 1: [METHOD] /api/path
- **Purpose**: [what it does]
- **Request Schema**: [schema or example]
- **Response Schema**: [schema or example]
- **Auth Required**: [yes/no, what type]
- **Rate Limits**: [if applicable]

### Endpoint 2: [METHOD] /api/path/{id}
[Similar structure]

## Technology Stack

Reference: [Link to technical-stack.md]

- **Backend Framework**: [technology & rationale]
- **Database**: [technology & rationale]
- **Frontend Framework**: [technology & rationale]
- **Message Queue**: [technology & rationale, if applicable]
- **Caching Layer**: [technology & rationale, if applicable]

## Performance Targets
- **Target Response Time**: [milliseconds]
- **Target Throughput**: [requests/second]
- **Expected Data Volume**: [size]
- **Concurrent Users**: [number]

## Security & Compliance
- **Authentication Method**: [e.g., JWT, OAuth2]
- **Authorization Model**: [e.g., RBAC]
- **Data Encryption**:
  - At rest: [algorithm]
  - In transit: [protocol]
- **Compliance Requirements**: [GDPR, HIPAA, PCI-DSS, etc., if applicable]

## Integration Points
- **Integrates with**: [other epics/systems]
- **Data Exchange Format**: [JSON, XML, etc.]
- **Frequency**: [real-time, batch, etc.]
- **Impact**: [what happens if integration fails]

## Deployment Architecture
[Diagram or description of deployment topology]

## Scalability Strategy
- **Horizontal Scaling**: [approach]
- **Vertical Scaling**: [approach]
- **Database Scaling**: [sharding, replication, etc.]
- **Caching Strategy**: [what to cache, TTL]

## High Availability
- **Failover Mechanism**: [approach]
- **Redundancy**: [what is redundant]
- **RTO (Recovery Time Objective)**: [time]
- **RPO (Recovery Point Objective)**: [acceptable data loss]

## Monitoring & Observability
- **Metrics**: [what to monitor]
- **Logging**: [centralized logging approach]
- **Tracing**: [distributed tracing approach]
- **Alerting**: [critical alerts]

## Known Constraints & Trade-offs
- [Constraint 1]: [impact]
- [Constraint 2]: [impact]
- [Trade-off 1]: [why chosen]

## Non-Functional Requirements

## Dependencies

## Estimation

