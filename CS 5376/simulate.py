import random

class State:
    all_states = []  # For keeping track of states as they're initialized.

    def __init__(self, name, payoff, choices=None):
        self.name = name
        self.payoff = payoff
        self.choices = choices
        self.value = 0
        self.all_states.append(self)

    def is_terminal_state(self):
        return self.choices == None


class Choice:
    def __init__(self, out_state, weight=1):
        self.out_state = out_state
        self.weight = weight


def run_episode(start_state, cost_per_step):

    payoff_total = 0
    steps_taken = 0
    curr_state = start_state
    states_visited = {curr_state}

    while not curr_state.is_terminal_state():

        # Make a decision.
        choices = curr_state.choices
        weights = [final_choice.weight for final_choice in choices]
        final_choice = random.choices(choices, weights)[0]
        next_state = final_choice.out_state

        payoff = next_state.payoff
        payoff_total += payoff
        states_visited.add(next_state)
        steps_taken += 1
        curr_state = next_state

    cost_for_steps = cost_per_step * steps_taken
    payoff_total += cost_for_steps

    return payoff_total, states_visited


if __name__ == "__main__":

    weight_attack = 20
    weight_not_attack = 5
    weight_negotiate = 30
    weight_expose = 40
    weight_ask_50 = 40
    weight_ask_75 = 60
    weight_lost_control = 3

    revenue = 1000
    ransom = 100

    # Costs will usually be negative.
    cost_distress = -3
    cost_hardware = -10
    cost_investigation = -10
    cost_expose = -revenue * 0.75
    cost_full = -ransom
    cost_seventy_five = -ransom * 0.75
    cost_fifty = -ransom * 0.5
    cost_twenty_five = -ransom * 0.25
    cost_kill = -revenue * 0.90
    cost_lost_control = 0
    cost_prepare = 0
    cost_not_prepare = 0
    cost_negotiate = -1
    cost_disagree = 0
    cost_wait = 0

    d39 = State("d39: pay 75%", cost_seventy_five)
    d38 = State("d38: pay 50%", cost_fifty)
    d37 = State("d37: ask 75%", 0, [Choice(d39)])
    d36 = State("d36: ask 50%", 0, [Choice(d38)])
    d35 = State("d35: negotiate", cost_negotiate, [Choice(d36, weight_ask_50), Choice(d37, weight_ask_75)])
    d34 = State("d34: pay full amount", cost_full)
    d33 = State("d33: kill service", cost_kill)
    d32 = State("d32: pay 75%", cost_seventy_five)
    d31 = State("d31: pay 50%", cost_fifty)
    d30 = State("d30: pay 50%", cost_fifty)
    d29 = State("d29: pay 25%", cost_twenty_five)
    d28 = State("d28: pay 75%", cost_seventy_five)
    d27 = State("d27: pay 50%", cost_fifty)
    d26 = State("d26: expose sensitive data", cost_expose, [Choice(d33), Choice(d34), Choice(d35)])
    d25 = State("d25: negotiate", 0, [Choice(d31), Choice(d32)])
    d24 = State("d24: negotiate", 0, [Choice(d29), Choice(d30)])
    d23 = State("d23: lost control", cost_lost_control)
    d22 = State("d22: ask 75%", 0, [Choice(d28)])
    d21 = State("d21: ask 50%", 0, [Choice(d27)])
    d20 = State("d20: prepare", cost_prepare)
    d19 = State("d19: not prepare", cost_not_prepare)
    d18 = State("d18: disagree", cost_disagree, [Choice(d25, weight_negotiate), Choice(d26, weight_expose)])
    d17 = State("d17: pay full amount", cost_full)
    d16 = State("d16: wait", cost_wait, [Choice(d23, weight_lost_control), Choice(d24, weight_negotiate)])
    d15 = State("d15: negotiate", cost_negotiate, [Choice(d21, weight_ask_50), Choice(d22, weight_ask_75)])
    d14 = State("d14: pay full amount", cost_full)
    d13 = State("d13: kill service", cost_kill)
    d12 = State("d12: pay 75%", cost_seventy_five)
    d11 = State("d11: pay 50%", cost_fifty)
    d10 = State("d10: not attacked", 0, [Choice(d19), Choice(d20)])
    d9 = State("d9: attacked", cost_distress, [Choice(d16), Choice(d17), Choice(d18)])
    d8 = State("d8: expose sensitive data", cost_expose, [Choice(d13), Choice(d14), Choice(d15)])
    d7 = State("d7: negotiate", 0, [Choice(d11), Choice(d12)])
    d6 = State("d6: launch investigation", cost_investigation, [Choice(d9, weight_attack), Choice(d10, weight_not_attack)])
    d5 = State("d5: replace hardware", cost_hardware)
    d4 = State("d4: pay full amount", cost_full)
    d3 = State("d3: not pay", 0, [Choice(d7, weight_negotiate), Choice(d8, weight_expose)])
    d2 = State("d2: attack did not happen", 0, [Choice(d5), Choice(d6)])
    d1 = State("d1: attack happened", cost_distress, [Choice(d3), Choice(d4)])
    d0 = State("d0: vulnerability found", 0, [Choice(d1, weight_attack), Choice(d2, weight_not_attack)])

    N_EPISODES = 1000
    LEARNING_RATE = 0.1
    START_STATE = d0
    STEP_COST = -1

    for i in range(N_EPISODES):
        episode_payoff, states_visited = run_episode(START_STATE, STEP_COST)
        for state in states_visited:
            state.value = state.value + LEARNING_RATE * (episode_payoff - state.value)

    print(f"N_EPISODES={N_EPISODES}, LEARNING_RATE={LEARNING_RATE}, START_STATE=\"{START_STATE.name}\", STEP_COST={STEP_COST}")
    print("[state_id: state_name] = value")
    for state in State.all_states:
        print(f"[{state.name}] = {float(state.value):.5}")
