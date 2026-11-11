
from thermostat_control import target_temperature, hvac_action, energy_alert


# Target temperature tests

def test_away():
    assert target_temperature("away", False, 12) == 16

def test_sleep_before_six():
    assert target_temperature("sleep", True, 5) == 18

def test_sleep_at_six():
    assert target_temperature("sleep", True, 6) == 20

def test_sleep_before_ten_pm():
    assert target_temperature("sleep", True, 21) == 20

def test_sleep_at_ten_pm():
    assert target_temperature("sleep", True, 22) == 18

def test_unoccupied():
    assert target_temperature("home", False, 12) == 18

def test_morning_start():
    assert target_temperature("home", True, 6) == 22

def test_morning_end():
    assert target_temperature("home", True, 9) == 20

def test_evening_start():
    assert target_temperature("home", True, 17) == 21

def test_evening_end():
    assert target_temperature("home", True, 22) == 20


# HVAC action tests

def test_idle():
    assert hvac_action(20, 20.5, 10) == "idle"

def test_heat_boost():
    assert hvac_action(15, 20, 4) == "heat_boost"

def test_heat_normal():
    assert hvac_action(15, 20, 5) == "heat"

def test_cool_boost():
    assert hvac_action(25, 20, 31) == "cool_boost"

def test_cool_normal():
    assert hvac_action(25, 20, 30) == "cool"


# Energy alert tests

def test_empty_readings():
    assert energy_alert([], 10) == "ok"

def test_none_over_limit():
    assert energy_alert([5, 10, 7], 10) == "ok"

def test_warning_exactly_half():
    assert energy_alert([11, 12, 5, 6], 10) == "warning"

def test_critical_more_than_half():
    assert energy_alert([11, 12, 13, 5], 10) == "critical"

def test_single_high_reading():
    assert energy_alert([11], 10) == "critical"
