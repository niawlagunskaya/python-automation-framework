from harness.core.scenario import Scenario
from harness.engines import api_engine
def run_scenario(sc: Scenario):
    for step in sc.steps:
        print(f"Step Name: {step.name} \n Step Kind: {step.kind}")
        if step.kind == "api":
            api_engine.func_name(step, "randomurl")
        else:
            print("unsupported step")
    return True
