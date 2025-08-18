from dispatch.fourmi_bot import run_fourmi_bot
from dispatch.berserk_bot import run_berserk_bot
from dispatch.shadow_bot import run_shadow_bot
from config import CAPITAL_INITIAL, ALLOCATION

def run_all_bots():
    run_fourmi_bot(CAPITAL_INITIAL * ALLOCATION['fourmi'])
    run_berserk_bot(CAPITAL_INITIAL * ALLOCATION['berserk'])
    run_shadow_bot(CAPITAL_INITIAL * ALLOCATION['shadow'])