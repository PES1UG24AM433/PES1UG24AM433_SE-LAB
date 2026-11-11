
from thermostat_control import target_temperature, hvac_action, energy_alert


# Target temperature tests

def test_away_mode():
    assert target_temperature("away", True, 12) == 16

def test_sleep_night():
    assert target_temperature("sleep", True, 23) == 18

def test_sleep_day():
    assert target_temperature("sleep", True, 12) == 20

def test_unoccupied():
    assert target_temperature("home", False, 12) == 18

def test_morning():
    assert target_temperature("home", True, 7) == 22

def test_evening():
    assert target_temperature("home", True, 19) == 21

def test_normal_day():
    assert target_temperature("home", True, 12) == 20


# HVAC action tests

def test_idle():
    assert hvac_action(22, 22, 15) == "idle"

def test_heat_boost():
    assert hvac_action(15, 22, 2) == "heat_boost"

def test_heat():
    assert hvac_action(18, 22, 10) == "heat"

def test_cool_boost():
    assert hvac_action(30, 22, 35) == "cool_boost"

def test_cool():
    assert hvac_action(28, 22, 20) == "cool"


# Energy alert tests

def test_no_readings():
    assert energy_alert([], 10) == "ok"

def test_all_below_limit():
    assert energy_alert([5, 6, 7], 10) == "ok"

def test_warning():
    assert energy_alert([12, 5, 6], 10) == "warning"

def test_critical():
    assert energy_alert([12, 13, 5], 10) == "critical"
