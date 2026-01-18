# define the data model for how tests will be described in the framework
# represent test scenario as a name + tags + ordered steps, where each step has an action and an expectation
import dataclasses
@dataclasses.dataclass
class Step:
    name: str
    kind: str
    action: dict
    expect: dict

@dataclasses.dataclass
class Scenario:
    name: str
    steps: list[Step]
    tags: set[str]

