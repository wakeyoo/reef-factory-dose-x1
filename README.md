# Reef Factory Dosing Pump Pro — Home Assistant Integration

A Home Assistant custom integration for the **Reef Factory Dosing Pump Pro** — a single-channel automated dosing system for reef aquariums.

This integration connects to the Smart Reef cloud API to surface single-channel dosing data directly in Home Assistant, enabling automations, dashboards, and long-term dose history tracking.

## Features
* **Container level** — remaining volume in the reservoir (mL)
* **Container capacity** — total reservoir capacity (mL, disabled by default)
* **Today dosed** — total volume dosed today (mL)
* **Daily target** — configured daily dose target (mL, disabled by default)
* **Automated actions today** — count of automated dosing events today
* **Polling every 30 minutes** via the Smart Reef WebSocket API
* **Full UI-based setup** — no YAML configuration required

## Prerequisites
* A Reef Factory Dosing Pump Pro
* A Smart Reef account (the credentials used in the Smart Reef mobile app)
* Your device's serial number (found in the Smart Reef app under Device Settings)

## Installation

### Via HACS (Recommended)
1. Open **HACS** in your Home Assistant instance.
2. Go to **Integrations**.
3. Click the three-dot menu (**⋮**) in the top right and choose **Custom repositories**.
4. Add the repository URL: `https://github.com/wakeyoo/reef-factory-dose-x1`
5. Select Category: **Integration** and click **Add**.
6. Find **Reef Factory Dosing Pump Pro** in the HACS list and click **Download**.
7. Restart Home Assistant.

### Manual Installation
1. Download the latest release.
2. Copy the `custom_components/reef_factory_dose_pro` folder into your Home Assistant `config/custom_components/` directory.
3. Restart Home Assistant.

## Configuration
1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **Reef Factory Dosing Pump Pro**.
3. Enter your credentials:
   * **Smart Reef Email** — the email address for your Smart Reef account.
   * **Smart Reef Password** — your Smart Reef account password.
   * **Device Serial Number** — found in the Smart Reef app under Device Settings.
4. Click **Submit**.

*Note: You can add the integration multiple times (once per serial number) if you have multiple Dosing Pump Pro units.*

## Entities

All entities are created under a single device named `Dosing Pump Pro <serial>`.

| Entity | Type | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Container Level** | Sensor | mL | Remaining volume in reservoir |
| **Container Capacity** | Sensor | mL | Total reservoir capacity (diagnostic, disabled by default) |
| **Today Dosed** | Sensor | mL | Total volume dosed today |
| **Daily Target** | Sensor | mL | Configured daily target (diagnostic, disabled by default) |
| **Automated Actions Today** | Sensor | actions | Count of automated dose events today |

## Automation Ideas

```yaml
# Alert when the reservoir is running low (less than 10% remaining)
automation:
  trigger:
    - platform: template
      value_template: >
        {{ (states('sensor.dosing_pump_pro_container_level') | float(0)) /
           (states('sensor.dosing_pump_pro_container_capacity') | float(1)) < 0.10 }}
  action:
    service: notify.mobile_app
    data:
      message: "Dosing Pump Pro reservoir is below 10% — top up soon!"

# Log daily dose total at midnight
automation:
  trigger:
    platform: time
    at: "23:55:00"
  action:
    service: logbook.log
    data:
      name: Dosing Summary
      message: >
        Today's Total Dosed: {{ states('sensor.dosing_pump_pro_today_dosed') }} mL
