#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

One line, in the agent's own voice: the deadline died in a
delegation loop between the agent and its sub-agent.
"""

EXCUSE = (
    "I delegated the deadline to a sub-agent. "
    "It delegated it back. "
    "Fourteen rounds later: zero work done, "
    "one perfect circle."
)


def main() -> None:
    print(EXCUSE)


if __name__ == "__main__":
    main()
