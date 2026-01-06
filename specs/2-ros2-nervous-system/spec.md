# Feature Specification: Module 1 — The Robotic Nervous System (ROS 2)

**Feature Branch**: `2-ros2-nervous-system`
**Created**: 2026-01-04
**Status**: Draft
**Input**: User description: "Module 1 — The Robotic Nervous System (ROS 2)"

---

## User Scenarios & Testing

### User Story 1 - Student Understands ROS 2 as Distributed Middleware (Priority: P1)

A learner new to robotics needs to understand ROS 2 as a **communication and coordination backbone** for distributed robot components, not as a programming language or simulator.

**Why this priority**: Without this foundational understanding, students conflate ROS 2 with simulation tools (Gazebo), control algorithms, or specific languages. This conceptual clarity is essential before any hands-on work.

**Independent Test**: A student can:
1. Explain ROS 2's role as middleware enabling component communication
2. Draw a simple diagram showing how sensors, processors, and actuators exchange data via ROS 2
3. Identify ROS 2 concepts in a given robot system description

**Acceptance Scenarios**:

1. **Given** a student has only heard "ROS 2" mentioned in robotics contexts, **When** they complete the module's foundational section, **Then** they understand ROS 2 as a message-based communication framework for distributed processes.

2. **Given** a student reads about a humanoid robot with multiple sensors and actuators, **When** they apply ROS 2 concepts, **Then** they can map sensor streams to topics and actuator commands to publishers.

3. **Given** a student encounters a statement like "ROS 2 is just for simulation," **When** they reference the module, **Then** they can articulate that ROS 2 is middleware independent of simulation tools.

---

### User Story 2 - Student Grasps ROS 2 Communication Patterns (Priority: P1)

A learner needs to internalize the three primary ROS 2 communication patterns—**Topics (pub/sub)**, **Services (req/resp)**, and **Actions (goal-oriented)**—and know when to use each.

**Why this priority**: These patterns form the vocabulary for discussing robot system design. Without this clarity, students cannot reason about distributed robot architectures or read existing ROS systems.

**Independent Test**: A student can:
1. Describe a use case and select the appropriate communication pattern (topic, service, or action)
2. Explain why one pattern is better than another for a given scenario
3. Read a ROS 2 system diagram and trace data flow through all three patterns

**Acceptance Scenarios**:

1. **Given** a continuous stream of sensor data (e.g., LiDAR), **When** a student is asked "How does this reach the perception processor?", **Then** they correctly identify this as a **topic** (pub/sub pattern).

2. **Given** a robot that needs to query its battery level once, **When** a student designs the ROS 2 interaction, **Then** they select a **service** (request/response).

3. **Given** a robot tasked with navigating to a goal with feedback, **When** a student chooses communication, **Then** they select an **action** (goal-oriented).

4. **Given** a mixed scenario (continuous sensor updates + periodic queries + long-running navigation), **When** the student designs the system, **Then** they correctly use all three patterns for appropriate subsystems.

---

### User Story 3 - Student Bridges Python AI Agents to ROS Controllers (Priority: P1)

A learner needs to understand how **Python-based AI agents** (including future LLM-based planners) interface with **ROS 2 controllers** on physical or simulated robots.

**Why this priority**: This is the key conceptual bridge for the entire course. Future modules depend on understanding how digital (Python agent) and physical (ROS controller) systems interact.

**Independent Test**: A student can:
1. Describe the role of `rclpy` (Python ROS client library) in connecting AI to robotics
2. Outline the data flow from perception → AI decision → motor command
3. Explain the separation of concerns: cognition (agent) vs. actuation (controller)

**Acceptance Scenarios**:

1. **Given** a Python AI agent that decides "move forward 1 meter," **When** asked how this reaches motor controllers, **Then** the student correctly describes using ROS 2 topics/services via `rclpy` to publish motion commands.

2. **Given** a simulated humanoid robot with 20+ joints, **When** a student is asked how an LLM-based planner controls it, **Then** they explain the agent subscribes to sensor topics, reasons, and publishes joint commands via ROS 2.

3. **Given** a system diagram showing an AI layer separate from robot controllers, **When** asked what ties them together, **Then** the student identifies ROS 2 communication and `rclpy` as the integration layer.

---

### User Story 4 - Student Reads and Understands Humanoid URDF (Priority: P1)

A learner needs to understand **URDF (Unified Robot Description Format)** as a way to express humanoid robot **structure, kinematic chains, and relationships** between links and joints.

**Why this priority**: URDF appears in Module 2 (Gazebo), Module 3 (Isaac), and the Capstone. Understanding URDF structure early prevents confusion later and enables system-level reasoning.

**Independent Test**: A student can:
1. Read a URDF snippet and identify links (rigid bodies) and joints (connections)
2. Trace a kinematic chain from a humanoid robot's base to end-effector (e.g., hand)
3. Understand why URDF matters for simulation and control

**Acceptance Scenarios**:

1. **Given** a humanoid URDF with chest, arm, forearm, and hand, **When** asked to trace the kinematic chain, **Then** the student correctly identifies the sequence of joints and links.

2. **Given** a URDF snippet, **When** asked what information a motion planner needs, **Then** the student explains that the kinematic structure (from URDF) tells the planner which joints move together.

3. **Given** a humanoid robot preparing to enter Module 2 (Gazebo simulation), **When** asked why URDF matters, **Then** the student explains that URDF defines the structure the simulator will import.

---

### User Story 5 - Student Grasps ROS 2 Lifecycle & Safety Concepts (Priority: P2)

A learner needs to understand ROS 2 **node lifecycle** (unconfigured, inactive, active, finalized) and why **deterministic startup/shutdown** matters for safety.

**Why this priority**: Important for robustness and fault isolation but less immediately critical than communication patterns. Students should understand it before hands-on system design.

**Independent Test**: A student can:
1. Explain why ROS 2 nodes have multiple lifecycle states
2. Describe what happens during safe startup and shutdown
3. Identify why uncontrolled shutdown could be dangerous in physical systems

**Acceptance Scenarios**:

1. **Given** a robot with multiple ROS 2 nodes, **When** asked what happens if a node crashes, **Then** the student explains that lifecycle states and fault isolation prevent cascading failures.

2. **Given** a physical robot being shut down, **When** asked the safe sequence, **Then** the student explains the importance of node lifecycle transitions.

---

### User Story 6 - Educator Evaluates Module for Course Fit (Priority: P2)

An instructor reviewing this module needs to understand its scope, dependencies, and readiness for integration into the 13-week curriculum.

**Why this priority**: Educator buy-in affects course delivery quality. The specification should enable clear curricular planning.

**Independent Test**: An instructor can:
1. Verify that Module 1 aligns with course prerequisites
2. Assess learning objectives and success criteria
3. Plan assessments around ROS 2 package design

**Acceptance Scenarios**:

1. **Given** the course syllabus, **When** an instructor reviews Module 1, **Then** they confirm it fits Weeks 3–5 and is a prerequisite for Modules 2 and 3.

---

## Edge Cases

- **What if a student has no Linux/Ubuntu experience?** (Addressed in assumptions; assumes working with Ubuntu 22.04 environment; setup guidance is out-of-scope but recommended as prerequisite.)

- **What if a learner wants to use ROS 2 Iron instead of Humble?** (Mentioned that Humble is canonical; other distributions are variants; conceptual content applies to all.)

- **What if the student skips the ROS 2 architecture section and jumps to communication patterns?** (Possible but suboptimal; module content is sequenced to build understanding progressively.)

- **What if a student asks about ROS 1 (legacy)?** (ROS 1 is out-of-scope; module focuses exclusively on ROS 2.)

- **What if a learner conflates ROS 2 with specific robot frameworks (e.g., MoveIt, Nav2)?** (Module clarifies that ROS 2 is foundational middleware; framework integration occurs in later modules.)

---

## Requirements

### Functional Requirements

- **FR-001**: The module MUST explain ROS 2 as **distributed middleware** enabling component communication in robotic systems, distinct from simulators or programming languages.

- **FR-002**: The module MUST describe and contrast the **three primary ROS 2 communication patterns**:
  - **Topics** (pub/sub): Continuous data streams
  - **Services** (req/resp): Request-response interactions
  - **Actions**: Goal-oriented, long-running tasks

- **FR-003**: The module MUST explain **message-based communication** as the core abstraction, enabling decoupling of robot components.

- **FR-004**: The module MUST introduce **ROS 2 nodes** as independent, communicating processes and explain their role in distributed systems.

- **FR-005**: The module MUST bridge **Python-based AI agents** (including LLM-based agents) to ROS 2 controllers using `rclpy`, emphasizing the separation of **cognition (agent) vs. actuation (controller)**.

- **FR-006**: The module MUST introduce **URDF (Unified Robot Description Format)** as a method for expressing humanoid robot structure—links, joints, and kinematic chains.

- **FR-007**: The module MUST explain ROS 2 **node lifecycle states** (unconfigured, inactive, active, finalized) and their role in deterministic startup/shutdown.

- **FR-008**: The module MUST establish ROS 2 **Humble Hawksbill on Ubuntu 22.04** as the canonical reference environment, while noting that concepts apply to other distributions.

- **FR-009**: The module MUST include **guided, conceptual labs** that illustrate:
  - Simple ROS 2 node architectures
  - Message flow between sensors, planners, and actuators
  - How a Python AI agent subscribes to perception and publishes commands

- **FR-010**: The module MUST emphasize that all examples are **simulation-only** with no requirement for physical robot hardware.

- **FR-011**: The module MUST NOT teach Gazebo, NVIDIA Isaac, full robot control stacks, or low-level kinematics mathematics.

- **FR-012**: The module MUST be structured for the embedded RAG tutor, enabling step-by-step explanations of ROS 2 concepts, message flow, and URDF on demand.

### Key Entities

- **ROS 2 Node**: An independent process that communicates with other nodes via topics, services, or actions; represents a functional unit in a robotic system.
- **Topic**: A named channel for pub/sub messaging; used for continuous data streams (e.g., sensor data, commands).
- **Service**: A named request/response interface; used for discrete, synchronous interactions.
- **Action**: A goal-oriented mechanism with feedback; used for long-running tasks with progress reporting.
- **Message**: A structured data unit exchanged between nodes; defines the interface contract.
- **URDF**: XML-based format describing robotic structure (links, joints, kinematic relationships).
- **Python AI Agent**: A decision-making entity (future: LLM-based) that uses ROS 2 to interact with robot controllers.
- **ROS 2 Controller**: A node managing actuators (motors, joint controllers) based on commands received via ROS 2.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can define ROS 2 and articulate its role as middleware distinct from simulators or programming languages.

- **SC-002**: Students can explain all three ROS 2 communication patterns (topics, services, actions) and provide use cases for each.

- **SC-003**: Students can trace data flow through a multi-node ROS 2 system (sensors → perception → planner → actuators).

- **SC-004**: Students understand how Python AI agents (via `rclpy`) interface with ROS 2-based robot controllers.

- **SC-005**: Students can read a URDF snippet and identify links, joints, and kinematic relationships.

- **SC-006**: Students understand ROS 2 lifecycle states and why deterministic startup/shutdown matters for robot safety.

- **SC-007**: Module content is structured for RAG retrieval; students can ask the tutor to explain any ROS 2 concept and receive grounded, contextual answers.

- **SC-008**: All example systems described are simulation-compatible (no hardware assumptions).

- **SC-009**: Module language is academic but accessible; no unnecessary jargon; robotics terms are defined on first use.

- **SC-010**: Module aligns with course positioning (Weeks 3–5, prerequisite for Modules 2–4) and contributes to ROS 2 Package Design Assessment.

---

## Assumptions

- **Environment Assumption**: Learners have access to or understanding of Ubuntu 22.04 + ROS 2 Humble environment. Specific installation and setup are out-of-scope but recommended as prerequisites.

- **Knowledge Assumption**: Learners have Python programming fundamentals and basic AI/ML familiarity from the Introduction module.

- **Hardware Non-Assumption**: No physical robot hardware is required; all examples and labs are simulation-compatible.

- **Distribution Variant Assumption**: While Humble is canonical, concepts apply to ROS 2 Iron, Jazzy, and later distributions. Non-core API differences are out-of-scope.

- **Messaging Paradigm Assumption**: The module assumes message-based communication (DDS) as the foundation; low-level network protocols are out-of-scope.

- **Integration Assumption**: Module 1 is a prerequisite for Modules 2 (Digital Twin), 3 (Isaac), and 4 (VLA). Subsequent modules will build on this foundation.

- **Safety Responsibility Assumption**: While lifecycle and deterministic shutdown are covered conceptually, detailed safety analysis (e.g., fail-safes, watchdogs) belongs in later modules or a dedicated safety engineering context.

---

## Non-Goals

The module MUST NOT:

- **NG-001**: Teach Gazebo physics simulation or Unity engine mechanics.
- **NG-002**: Explain NVIDIA Isaac Sim, Isaac ROS pipelines, or Isaac perception tools.
- **NG-003**: Implement full robot control stacks (e.g., joint trajectory controllers, inverse kinematics).
- **NG-004**: Teach low-level kinematics mathematics, Denavit-Hartenberg parameters, or control theory.
- **NG-005**: Provide hardware setup instructions, robot assembly, or deployment procedures.
- **NG-006**: Compare ROS 2 to other robotics middleware (e.g., MOOS, Yarp) or justify ROS 2 adoption at length.
- **NG-007**: Teach C++ ROS 2 integration (Python via `rclpy` only).
- **NG-008**: Explain advanced ROS 2 features (e.g., QoS policies, custom executors) beyond foundational concepts.

---

## Content Structure

The module is organized into **7 logically sequenced sections**:

1. **ROS 2: The Robotic Nervous System** — Motivation and core abstraction
2. **ROS 2 Architecture: Nodes, DDS, and Decoupling** — System design foundation
3. **Communication Pattern 1: Topics (Pub/Sub)** — Continuous data streams
4. **Communication Pattern 2: Services (Request/Response)** — Discrete interactions
5. **Communication Pattern 3: Actions (Goal-Oriented)** — Long-running tasks with feedback
6. **Bridging AI Agents to ROS 2: Python and `rclpy`** — Integration of cognition and actuation
7. **Describing Robots with URDF: Structure and Kinematics** — Robot morphology representation

**Optional Sections** (if needed after planning):
- 8. **Guided Conceptual Lab: Designing a Simple ROS 2 System** — Putting it all together
- 9. **ROS 2 Lifecycle and Safety Considerations** — Deterministic operation
- 10. **Common Pitfalls and Misconceptions** — Addressing confusion

---

## Style & Tone Guidelines

- **Academic but Accessible**: Written for intermediate CS/AI students new to robotics, not robotics experts.
- **System-Thinking Emphasis**: Encourage readers to think in terms of distributed components and message flows, not isolated algorithms.
- **Conceptual Over Syntactic**: Prioritize understanding ROS 2 architecture over memorizing API details.
- **Scaffolded Progression**: Each section builds on prior understanding; concepts are introduced in order of dependency.
- **Narrative Continuity**: Link concepts to the broader Physical AI narrative (e.g., "This is how the humanoid's nervous system will coordinate sensors and AI decisions").

---

## Validation Checklist (Pre-Implementation)

- [ ] All 12 functional requirements defined and aligned with module goals
- [ ] 6 prioritized user stories with acceptance scenarios
- [ ] 10 success criteria covering learning outcomes and RAG structure
- [ ] ROS 2 Humble + Ubuntu 22.04 explicitly identified as canonical reference
- [ ] 7 content sections logically sequenced and scoped
- [ ] Non-goals clearly prevent scope creep (no Gazebo, no Isaac, no C++, no math)
- [ ] AI-agent-to-ROS-bridge is clearly articulated as core concept
- [ ] URDF introduction is present and sequenced appropriately
- [ ] Edge cases identified and addressed
- [ ] Module positioning (Weeks 3–5, prerequisite for Modules 2–4) clear
- [ ] Aligns with course Constitution and Hackathon-1 requirements
- [ ] RAG tutor can answer common questions about ROS 2 concepts from this content

---

## Assessment Integration

This module contributes to **ROS 2 Package Design Assessment**:

- **Deliverable**: Learners produce a conceptual ROS 2 package design artifact (diagram or design document).
- **Focus**: Architectural reasoning and message flow design, not executable code.
- **Rubric Alignment**:
  - Correct identification of ROS 2 communication patterns for given scenarios
  - Clear data flow diagrams showing pub/sub, services, and actions
  - Evidence of understanding AI-agent-to-controller integration
  - URDF structure comprehension (if kinematic reasoning is required)

---

## Acceptance Gate

Module 1 is **ready for content development** when this specification is approved. The actual module content will be written using:

- **Primary Skill**: `robotics-explainer` (author technically accurate, engaging explanations)
- **Supporting Skill**: `section-writer` (polish prose and narrative flow)
- **AI Tool**: Claude Code (supervised authoring, not autonomous content generation)
- **Validation**: Content reviewed against all 12 functional requirements and 10 success criteria

All content will be grounded in the Physical AI Hackathon-1 Constitution and positioned as Weeks 3–5 of the 13-week curriculum.
