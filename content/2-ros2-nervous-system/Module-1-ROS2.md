---
module: ros2-nervous-system
module_id: ros2
module_number: 1
sections: 7
word_count: 5800
retrieval_ready: true
rag_chunking: section-level
---

# Module 1: The Robotic Nervous System (ROS 2)

## 1. ROS 2: The Robotic Nervous System

When you think about a humanoid robot navigating a room and picking up an object, you might imagine a single intelligent system. In reality, that robot is composed of many independent components: cameras streaming visual data, joint motors executing commands, force sensors detecting touch, and a planning system reasoning about goals and obstacles.

**These components must coordinate in real time.**

ROS 2 (Robot Operating System 2) is the **nervous system** of modern robots. Just as your biological nervous system carries signals from your senses to your brain and back out to your muscles, ROS 2 carries data streams from a robot's sensors to planning algorithms and back to its actuators. It is not a simulator, not a programming language, and not a specific robot control framework. **ROS 2 is middleware—the communication infrastructure that allows distributed robotic components to work as a coherent system.**

Without ROS 2 or something like it, building a complex robot would mean writing custom code to manage communication between every pair of components. The first robot would have a sensor driver talking directly to a perception module, which talks directly to a planner, which talks directly to a controller. Add a second sensor, and you rewire everything. Add a second robot, and you duplicate all the infrastructure.

ROS 2 solves this problem by establishing a standard, language-independent way for robot software components to communicate. It provides a marketplace of tools, libraries, and community expertise. And it enables the separation of concerns: hardware drivers publish sensor data without needing to know what algorithms will use that data. Planning algorithms consume perception and produce high-level commands without needing to know how motors will execute them.

For a humanoid robot, this architecture is essential. A humanoid has dozens of joints, hundreds of sensors, multiple perception systems, and a cognitive layer (perhaps an LLM-based planner) running simultaneously. ROS 2 is what ties all these components together into a single, responsive agent.

## 2. ROS 2 Architecture: Nodes, DDS, and Decoupling

ROS 2's architecture is built on a simple but powerful idea: **autonomous processes (nodes) that communicate via a publish-subscribe messaging system.**

### Nodes as Independent Processes

A **node** is an independent, executable process within a ROS 2 system. A humanoid robot might have dozens of nodes:

- A **sensor node** that reads from cameras and publishes image data
- A **perception node** that subscribes to images and publishes detected objects
- A **planner node** that subscribes to world state and publishes motion goals
- Multiple **controller nodes** that subscribe to goals and publish motor commands
- A **safety monitor node** that subscribes to all critical signals and enforces constraints

Each node has a specific responsibility. None of them needs to know the internal implementation of the others. The sensor node doesn't care whether perception is implemented in C++ or Python. The planner doesn't need to know if motors are real or simulated. This **decoupling** is the core strength of the architecture.

Nodes communicate through a publish-subscribe (pub/sub) model called the Distributed Data Service (DDS). Think of DDS as a global bulletin board. When a sensor node has new data, it publishes to a named topic on the bulletin board. Any node interested in that data subscribes to the topic and receives all published messages. The DDS infrastructure handles routing, buffering, and serialization—the node writers don't think about network details.

### The Message Contract

Communication between nodes happens via **messages**—structured data units with well-defined formats. For example, a camera publishes `sensor_msgs/Image` messages, a motion planner publishes `geometry_msgs/Twist` messages (linear and angular velocity commands), and a joint controller publishes `sensor_msgs/JointState` messages.

These message types are **contracts**. When a node publishes a message, it promises that the data conforms to the message schema. Subscribers rely on that contract and don't need to negotiate interfaces. This standardization, again, enables decoupling.

ROS 2 provides a large library of standard message types, and developers can define custom messages for domain-specific data. A humanoid's proprietary force-control message might have fields for desired force vectors and stiffness parameters. As long as nodes agree on the message schema, they can interoperate.

### Why This Architecture Matters for Physical AI

For our course, this architecture is crucial. Your humanoid robot will have an AI planning layer (Module 4: Vision-Language-Action) that reasons about goals and world state. That AI layer will be written in Python, possibly using large language models. It will **not** be a hand-coded controller that micromanages every motor.

Instead, the AI planner will publish high-level commands via ROS 2 (e.g., "grasp the cup"). Specialized ROS 2 nodes will translate those commands into joint trajectories, enforce safety constraints, and drive the motors. The beauty of this design is that the AI planner can be swapped out, upgraded, or even run remotely, and the low-level robot operation continues uninterrupted. The decoupling enables flexibility and resilience.

## 3. Communication Pattern 1: Topics (Pub/Sub)

**Topics** are the primary communication pattern in ROS 2. They implement a publish-subscribe model: a node publishes a message to a named topic, and any number of nodes can subscribe and receive a copy.

### When to Use Topics

Topics are ideal for **continuous data streams**:

- Sensor data (camera images, LiDAR scans, IMU readings)
- Periodic state updates (current position, velocity, forces)
- Asynchronous commands (desired motion direction, reference frames)

Topics are **one-way broadcasting**. The publisher doesn't know or care who is listening. Subscribers receive messages as they arrive but don't send responses back to the publisher. This decoupling means publishers and subscribers can be started and stopped independently.

### Topic Flow in a Humanoid System

Imagine your humanoid is preparing to pick up a cup:

1. **Camera Node** publishes `sensor_msgs/Image` to topic `/camera/rgb_image` at 30 Hz
2. **Perception Node** subscribes to `/camera/rgb_image`, detects the cup's location, and publishes a `geometry_msgs/PointStamped` message (3D position) to topic `/perception/object_detected`
3. **Planner Node** subscribes to `/perception/object_detected`, reasons about reaching the cup's location, and publishes a `geometry_msgs/PoseStamped` goal to topic `/planner/goal`
4. **Motion Controller Node** subscribes to `/planner/goal`, translates it into joint velocities, and publishes to topic `/command/joint_velocity`
5. **Joint Driver Node** subscribes to `/command/joint_velocity` and sends commands to the actual motors

At any moment, the camera publishes at 30 Hz whether or not anyone is listening. The perception node might lag slightly behind the camera due to processing time. The planner waits for new perception updates before replanning. The controller executes as fast as it can. **All components are loosely coupled through topics.** If perception fails temporarily, the planner still has the last known position. If the motion controller lags, the planner doesn't stall—it continues reasoning based on predicted state.

This robustness is why topics are used for high-frequency, continuous data. The cost is latency variability and the challenge of synchronizing asynchronous streams (an advanced topic we won't explore here).

### Topic Messages and Timestamps

Each message published to a topic carries metadata: a timestamp (when was this data collected?) and a frame reference (in what coordinate system is this data expressed?). These fields enable the perception, planning, and control layers to reason correctly about time and space.

For example, a force sensor publishes forces "at time T, in the robot's wrist frame." A planner reads these forces and knows exactly when they were measured and which robot part they refer to. This temporal and spatial grounding is essential for safe, coordinated robot operation.

## 4. Communication Pattern 2: Services (Request/Response)

**Services** implement a request-response pattern: a client node sends a request to a service, and the service node sends back a response. Unlike topics, services are **synchronous**—the client waits for a response before proceeding.

### When to Use Services

Services are ideal for **discrete, transactional interactions**:

- Querying the robot's current battery level
- Requesting a one-time computation (e.g., "plan a path from A to B")
- Triggering an action with immediate feedback (e.g., "record a sensor snapshot")

Services are useful when the client needs a result and is willing to wait. The request-response pattern provides a clear API contract: you send this request structure, and you'll receive this response structure.

### Service Example: Path Planning

Imagine your humanoid needs to navigate around an obstacle. Rather than continuously streaming goal positions (topics), the navigation system uses a service:

1. **Planner Node** calls the service `/move_base/plan_path` with request `{start: [0,0], goal: [5,5]}`
2. **Path Planning Service** computes the path, avoiding obstacles
3. **Path Planning Service** responds with `{path: [...], feasible: true}`
4. **Planner Node** receives the response and can now execute the path

The synchronous nature means the planner waits for the path before deciding next steps. The service provider can take seconds (or longer) to compute without flooding the network with intermediate updates.

### Hybrid Patterns

In practice, you often combine patterns. A navigation system might:

- Publish the current path to a topic (for visualization and feedback)
- Publish current position to a topic (continuous state)
- Offer a service to request a new path goal
- Publish collision alerts to a topic (asynchronous safety warnings)

Each pattern serves its purpose in the overall system architecture.

## 5. Communication Pattern 3: Actions (Goal-Oriented)

**Actions** are ROS 2's way of handling long-running, goal-oriented tasks with feedback. An action client sends a goal to an action server; the server executes, provides periodic feedback, and eventually returns a final result.

### When to Use Actions

Actions are ideal for **long-running tasks with progress feedback**:

- Navigate to a goal location (takes seconds to minutes)
- Execute a grasping sequence (takes seconds, needs real-time feedback)
- Run a vision-based search (takes variable time, provides periodic updates)

Actions are more complex than topics or services, but they enable elegant handling of long tasks. The client can cancel mid-execution ("stop navigating"), and the server can provide feedback ("I'm 50% of the way there").

### Action Anatomy: Humanoid Navigation

A humanoid robot receives a voice command: "Go to the kitchen." Here's how an action handles it:

1. **Voice Command Node** sends an action goal `/navigate_to_goal` with request `{target_location: "kitchen"}`
2. **Navigation Action Server** starts working toward that goal
   - It subscribes to the humanoid's current position (topic-based feedback)
   - It publishes periodic feedback to the action client: "5 meters traveled, 10 meters remaining"
   - It detects obstacles and replans
3. After navigating for 30 seconds, the humanoid reaches the kitchen
4. **Navigation Action Server** sends final result: `{success: true, distance_traveled: 15.0}`
5. **Voice Command Node** knows the task completed and can now issue the next command

Meanwhile, if the voice command node changes its mind ("cancel, go back"), it can preempt the action. The navigation server gracefully stops, returns `{success: false, reason: "preempted"}`, and the humanoid halts.

### Why Actions Matter for Humanoid Robots

Humanoid robots perform inherently long-running tasks. A single command—"pick up the cup"—might take 30 seconds and involve dozens of intermediate steps: navigate, approach, reach, grasp, lift, return, place. Actions provide a clean abstraction for these complex behaviors.

## 6. Bridging AI Agents to ROS 2: Python and `rclpy`

This section is the conceptual bridge of the entire course. **How does a high-level AI planning layer (Module 4: VLA) interact with the low-level ROS 2 robot control system?**

### The Separation of Concerns

Modern robotics separates two concerns:

1. **Cognition**: Reasoning about goals, world state, and plans. This layer is high-level, possibly LLM-based, written in Python. It operates at semantics—"pick up the cup" or "move to the kitchen."

2. **Actuation**: Executing motor commands, enforcing constraints, and handling real-time control. This layer is low-level, deterministic, and written in specialized control languages (often C++ for speed). It operates at kinematics—joint angles, velocities, and forces.

These two layers must communicate, and ROS 2 is the bridge.

### Python and `rclpy`

`rclpy` is the Python client library for ROS 2. It allows Python programs to:

- **Subscribe to topics**: Read sensor data, perception results, or state estimates
- **Publish to topics**: Broadcast decisions, commands, or state information
- **Call services**: Request computations or trigger actions
- **Use actions**: Send goal-oriented requests and receive feedback

Here's a conceptual example (pseudocode) of a Python AI planner using `rclpy`:

```
# Python AI Planner using rclpy

node = ROS2_Node("ai_planner")

# Subscribe to perception
node.subscribe("/perception/world_state", WorldState, on_perception_update)

# Publish commands
motion_publisher = node.create_publisher("planner/command", Command)

def on_perception_update(world_state):
    # AI reasoning: what should we do?
    if "cup" in world_state.objects:
        cup_pose = world_state.objects["cup"].pose
        # Decide to pick up the cup
        command = Command(action="grasp", target=cup_pose)
        motion_publisher.publish(command)
```

The AI planner subscribes to `/perception/world_state`, which is published by a perception node. When new perception arrives, the planner reasons ("I see a cup; I should grasp it") and publishes a command to `/planner/command`. Downstream motion controllers subscribe to that command and execute it.

The key insight: **The AI planner doesn't need to know how the motion controller works.** It publishes commands; downstream nodes handle execution. The planner can be run in Python, updated without touching C++ code, and even migrated to a cloud service without breaking the robot.

### Latency and Real-Time Constraints

An important caveat: AI reasoning might be slow. An LLM-based planner could take 100 milliseconds to reason about the next action. Meanwhile, low-level motor controllers need updates every 10 milliseconds to maintain stability.

This is why the architecture separates cognition and actuation:

- **The AI planner** runs at 10 Hz (reasoning once per 100 ms)
- **The motion controller** runs at 100 Hz (updating motors 10 times per second)
- **The AI planner publishes a high-level goal** ("move arm to this pose")
- **The motion controller subscribes and executes** low-level joint commands

The motion controller can independently ensure that joint commands stay within safe limits, respond to unexpected disturbances, and maintain balance. The AI planner focuses on high-level reasoning. Both benefit from the separation.

## 7. Describing Robots with URDF: Structure and Kinematics

The final core concept is **URDF (Unified Robot Description Format)**, an XML-based language for describing robotic structure. URDF defines the morphology of a robot: its links (rigid bodies), joints (connections), and kinematic relationships.

### Links and Joints

A humanoid robot is a kinematic chain: the base connects to the torso via a fixed joint, the torso connects to the left shoulder via a revolute joint, the left shoulder connects to the left elbow via another joint, and so on.

In URDF:

- A **link** is a rigid body (the torso, upper arm, forearm, hand)
- A **joint** is a connection between two links (shoulder joint, elbow joint)
- Each joint has a **type**: revolute (rotational), prismatic (linear), fixed, or continuous

A simplified humanoid URDF might look like:

```xml
<robot name="humanoid">
  <link name="base" />
  <link name="torso" />
  <link name="left_upper_arm" />
  <link name="left_forearm" />
  <link name="left_hand" />

  <joint name="base_to_torso" type="fixed">
    <parent link="base" />
    <child link="torso" />
  </joint>

  <joint name="left_shoulder" type="revolute">
    <parent link="torso" />
    <child link="left_upper_arm" />
    <limit lower="-1.57" upper="1.57" /> <!-- ±90 degrees -->
  </joint>

  <joint name="left_elbow" type="revolute">
    <parent link="left_upper_arm" />
    <child link="left_forearm" />
  </joint>

  <!-- ... more joints ... -->
</robot>
```

### Why URDF Matters

URDF serves several critical purposes:

1. **Simulation**: When you load a humanoid into Gazebo (Module 2), you import its URDF. Gazebo uses the kinematic structure to compute dynamics, collisions, and sensor placements.

2. **Motion Planning**: Path and motion planners need to know the robot's structure. To answer "Can the arm reach this point?" a planner needs the joint limits and kinematic chain. URDF provides this.

3. **Control**: Real-time controllers need to know which joints to command. The control system reads URDF to understand the robot's morphology.

4. **Visualization**: Tools display the robot as a visual model. URDF includes mesh files (3D models) for each link, enabling realistic visualization.

5. **Safety**: URDF can specify joint limits (how far each joint can move), maximum velocities, and forces. Safety controllers use this information to prevent damage.

### Kinematic Chains and End-Effectors

A humanoid's arm is a kinematic chain: base → shoulder → elbow → wrist → hand. The hand is the **end-effector**—the point we ultimately want to control.

When a planner says "move the hand to position X, Y, Z," it's not specifying joint angles directly. Instead, it's giving a desired pose for the end-effector, and the inverse kinematics system (not covered here) computes what joint angles achieve that pose.

URDF provides the structure the inverse kinematics system needs. It knows that the hand is 6 joints away from the base, with specific limits and ranges at each joint.

### URDF and the Physical AI Curriculum

You'll encounter URDF in:

- **Module 2 (Digital Twin)**: You'll import a humanoid URDF into Gazebo and simulate it
- **Module 3 (Isaac)**: You'll use URDF with Isaac Sim for advanced perception
- **Module 4 (VLA)**: Your AI planner will reason about the humanoid's morphology (encoded in URDF) when planning manipulation tasks
- **Capstone**: Your system design will include a URDF representation of your humanoid

Understanding URDF's role now—as the structural blueprint of a robot—will make these future modules clearer.

---

## Summary: The Robotic Nervous System

ROS 2 is the communication infrastructure. Nodes are independent processes. Messages are structured data contracts. Topics broadcast continuous data. Services handle transactional request-response interactions. Actions manage long-running goal-oriented tasks. Python agents use `rclpy` to reason and command. URDF describes robot structure.

Together, these concepts enable a humanoid robot to coordinate dozens of sensors, actuators, and planning algorithms in real time. As you progress through this course, you'll see how this nervous system scales to support perception (Module 2), advanced vision systems (Module 3), AI-based planning (Module 4), and finally a fully autonomous humanoid system (Capstone).

The humanoid robot is more than the sum of its parts. ROS 2 is what makes those parts work as one.
