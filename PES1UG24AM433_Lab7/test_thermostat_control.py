
from hypothesis import given, strategies as st
from thermostat_control import (
    parse_setpoint,
    average_temperature,
    schedule_slot
)


# Test 1: parse_setpoint
@given(st.text() | st.none())
def test_parse_setpoint_no_crash(s):
    try:
        parse_setpoint(s)
    except Exception as e:
        assert False, f"parse_setpoint crashed with input {s!r}: {e}"


# Test 2: average_temperature
@given(st.text() | st.none())
def test_average_temperature_no_crash(s):
    try:
        average_temperature(s)
    except Exception as e:
        assert False, f"average_temperature crashed with input {s!r}: {e}"


# Test 3: schedule_slot
@given(st.text() | st.none())
def test_schedule_slot_no_crash(s):
    try:
        schedule_slot(s)
    except Exception as e:
        assert False, f"schedule_slot crashed with input {s!r}: {e}"
