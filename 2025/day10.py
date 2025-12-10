from sys import stdin
from collections import deque


def parse_input(input):
    """
    Parse machine configurations
    Each machine has:
    - target: target state for indicator lights (1 = on, 0 = off)
    - buttons: list of tuples, each containing indices of lights that button toggles
    """
    machines = []
    for line in input.splitlines():
        # Extract target state from [.##.]
        target_start = line.index("[") + 1
        target_end = line.index("]")
        target_str = line[target_start:target_end]
        target = [1 if c == "#" else 0 for c in target_str]

        # Extract buttons from (1,3) (2) etc
        buttons = []
        i = target_end + 1
        while i < len(line):
            if line[i] == "(":
                close = line.index(")", i)
                button_str = line[i + 1 : close]
                if button_str:
                    button = [int(x) for x in button_str.split(",")]
                    buttons.append(button)
                i = close + 1
            elif line[i] == "{":
                # Joltage requirements - ignore as per problem
                break
            else:
                i += 1

        machines.append((target, buttons))

    return machines


def solve_lights_bfs(target, buttons):
    """
    Solve for minimum button presses using BFS

    Since pressing a button twice returns to the original state,
    we only care about the parity (odd/even) of button presses.
    This means each button is either pressed (1) or not pressed (0).

    State: tuple representing current light configuration
    BFS explores all reachable states, tracking minimum presses to reach each
    """
    n_lights = len(target)
    target_tuple = tuple(target)

    # Start with all lights off
    start = tuple([0] * n_lights)

    # BFS: queue contains (state, presses_count)
    queue = deque([(start, 0)])
    visited = {start: 0}

    while queue:
        state, presses = queue.popleft()

        # Check if we reached the target
        if state == target_tuple:
            return presses

        # Try pressing each button
        for button in buttons:
            # Calculate new state after pressing this button
            new_state = list(state)
            for light_idx in button:
                new_state[light_idx] ^= 1  # Toggle light
            new_state_tuple = tuple(new_state)

            # Only visit if we haven't seen this state or found a shorter path
            if new_state_tuple not in visited or visited[new_state_tuple] > presses + 1:
                visited[new_state_tuple] = presses + 1
                queue.append((new_state_tuple, presses + 1))

    # No solution found
    return float("inf")


def solve_puzzle_1(machines):
    """
    Find the fewest total button presses to configure all machines using BFS
    """
    total = 0
    for target, buttons in machines:
        presses = solve_lights_bfs(target, buttons)
        if presses == float("inf"):
            return -1  # No solution
        total += presses
    return total


def solve_puzzle_2(machines):
    """
    Part 2 - to be determined after part 1 is solved
    """
    return 0


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)
