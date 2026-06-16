from policies import register

from solution.feature_demo import TimeOfDayPolicy
from solution.policy import MyPolicy

register("my_policy", MyPolicy)

# Worked example of using a FeaturePipeline inside a policy (see solution/feature_demo.py).
register("feature_demo", TimeOfDayPolicy)

# Register every policy you want us to see — keep the variants you tried across the
# challenge, each under its own name (add a module per policy as you go), e.g.:
#   from solution.my_policy_v2 import MyPolicyV2
#   register("my_policy_v2", MyPolicyV2)
