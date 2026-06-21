# Curriculum — Build the autograd engine

Goal: the student builds a `Value` class that supports `+`, `*`, and `tanh`, and can run
**backpropagation** to compute gradients automatically. By the end they understand exactly
how neural networks learn.

Reveal these milestones **one at a time**. Do not show the whole list to the student.

## Milestone 1 — The `Value` object
A class that wraps a single number and remembers its `data`, its `grad` (starts at 0),
and which other `Value`s produced it (its "children"). No math yet — just the container.
*Concept:* we need to track how values are built so we can later trace gradients back.

## Milestone 2 — Addition and multiplication
Implement `__add__` and `__mul__` so two `Value`s combine into a new `Value` that records
its parents and the operation. Forward pass only.
*Concept:* every operation builds a node in a computation graph.

## Milestone 3 — The local derivative of each op
For each operation, store *how* the output's gradient flows back to each input (the local
derivative). Addition passes gradient through unchanged; multiplication scales by the other
input.
*Concept:* the chain rule, one node at a time.

## Milestone 4 — `backward()`
Walk the graph from the output backward (topological order) and accumulate gradients into
every `Value.grad`.
*Concept:* backpropagation = chain rule applied across the whole graph.

## Milestone 5 — `tanh` and a tiny neuron
Add a `tanh` activation, then build a single neuron (`w*x + b` → `tanh`) and confirm its
gradients are correct. This is a real, trainable neuron built from scratch.
*Concept:* this is literally how deep learning works.

Each milestone has tests in `tests/`. A milestone is **done when its tests pass**.

When all tests pass, the engine is complete — and you're ready for **Project 2: Build & train
a neural net**, where this engine powers a real training loop.
