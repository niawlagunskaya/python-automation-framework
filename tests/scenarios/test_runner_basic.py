from harness.core.runner import run_scenario
from harness.core.scenario import Scenario
from harness.core.scenario import Step




def test_run_scenario_returns_true():
    name = "niatest"
    kind = "api"
    action = {}
    expect = {}

    my_steps = [Step(name, kind, action, expect)]
    my_scenario = Scenario("niascenario", my_steps, {"a", "b"})

    assert run_scenario(my_scenario) is True