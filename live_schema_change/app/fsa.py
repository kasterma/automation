import logging
import random
import numpy as np

log = logging.getLogger('fsa')


def compile_transitions_actions(transitions, actions):
    def f(s):
        r = random.uniform(0, 1)
        tr = transitions[s]
        l = list(zip(*tr.items()))
        ns = l[0][np.min(np.where(np.cumsum(l[1]) > r))]
        res = actions[ns]()
        return {'next_state': ns, 'result': res}
    return f


class FSA:
    def __init__(self, fsa_id: int, send_fn, fsa_type: int, transactions):
        self.fsa_id = fsa_id
        self.send_fn = send_fn
        self.fsa_type = fsa_type
        self.state = 'init'
        self.transitions = transactions
        self.actions = {'init': lambda: None,
                        'view': lambda: (self.fsa_id, self.fsa_type, 'view'),
                        'click': lambda: (self.fsa_id, self.fsa_type, 'click'),
                        'click2': lambda: (self.fsa_id, self.fsa_type, 'click2'),
                        'done': lambda: None}
        self.step_fn = compile_transitions_actions(self.transitions, self.actions)

    def step(self):
        s = self.step_fn(self.state)
        log.debug(f"FSA_{self.fsa_type}({self.fsa_id}): {self.state} --> {s['next_state']}")
        self.state = s['next_state']
        self.send_fn(s['result'])

    def done(self):
        return self.state == 'done'
