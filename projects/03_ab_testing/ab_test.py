"""
🔵 Project 03 — A/B Testing (the most common Data Scientist task in industry)
=============================================================================

The scenario (this is REAL work at every tech company):
    The product team changed the "Buy" button from blue to green. They show
    the OLD page to half of visitors (group A, "control") and the NEW page to
    the other half (group B, "treatment"). Question: did green actually get
    MORE people to buy — or is the difference just random luck?

Answering "is this difference real or just noise?" is the heart of data science.
The tool is a HYPOTHESIS TEST. Here we use a two-proportion z-test.

Run:
    python3 projects/03_ab_testing/ab_test.py
"""

import numpy as np
from scipy import stats

rng = np.random.default_rng(7)  # fixed seed -> reproducible

# --- 1. Simulate an experiment ---------------------------------------------
# In real life this data comes from your logs. Here we simulate it so we can
# learn the method. The TRUE conversion rates (which we'd never know in reality):
n_A, n_B = 5000, 5000          # visitors in each group
true_rate_A, true_rate_B = 0.10, 0.118   # green really IS a bit better

conversions_A = rng.binomial(1, true_rate_A, n_A).sum()
conversions_B = rng.binomial(1, true_rate_B, n_B).sum()

rate_A = conversions_A / n_A
rate_B = conversions_B / n_B

print("===== 🧪 EXPERIMENT RESULTS =====")
print(f"Group A (control, blue):   {conversions_A}/{n_A} bought = {rate_A:.2%}")
print(f"Group B (treatment, green):{conversions_B}/{n_B} bought = {rate_B:.2%}")
print(f"Observed lift: {(rate_B - rate_A):.2%}")


def two_proportion_z_test(conv_a, n_a, conv_b, n_b):
    """Return (z statistic, two-sided p-value) for difference in proportions."""
    p_a, p_b = conv_a / n_a, conv_b / n_b
    # Pooled proportion under the null hypothesis "the rates are equal".
    p_pool = (conv_a + conv_b) / (n_a + n_b)
    se = np.sqrt(p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b))
    z = (p_b - p_a) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))  # two-sided
    return z, p_value


z, p_value = two_proportion_z_test(conversions_A, n_A, conversions_B, n_B)

print("\n===== 📐 THE STATISTICAL TEST =====")
print(f"Null hypothesis (H0): green is NO different from blue.")
print(f"z-statistic: {z:.3f}")
print(f"p-value:     {p_value:.4f}")

# --- The decision rule -------------------------------------------------------
ALPHA = 0.05  # our risk tolerance: a 5% chance of a false alarm
print("\n===== ⚖️  THE DECISION =====")
if p_value < ALPHA:
    print(f"p ({p_value:.4f}) < {ALPHA}  ->  REJECT H0.")
    print("✅ The improvement is STATISTICALLY SIGNIFICANT. Ship the green button.")
else:
    print(f"p ({p_value:.4f}) >= {ALPHA}  ->  fail to reject H0.")
    print("🤷 We cannot conclude green is better. The difference may be luck.")

print("\n🧠 What the p-value MEANS (interview gold):")
print("   'If green were truly no different, there'd be only a", f"{p_value:.1%}",
      "chance\n    of seeing a gap this big by random luck alone.' Small p -> unlikely luck.")
print("\n⚠️  A p-value is NOT 'the probability green is better'. Never say that in")
print("    an interview. It is the probability of THIS DATA, assuming no difference.")
