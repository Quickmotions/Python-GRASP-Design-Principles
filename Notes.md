# GRASP DESIGN PRINCIPLES
#### General Responsibility Assignment Software Patterns

## 1. Creator Principle
 states that you should assign the creator role to the class that has or aggregates the object, contains or composes it, records or closely uses it, has the initializing data for it, or is a factory or builder for it.
- Object A is responsible for creating Object B inside of itself instead of creating Object B and then adding them into Object A

## 2. Information Expert
used to determine where to delegate responsibilities such as methods, computed fields, and so on

