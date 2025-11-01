# ROS2 Proximity Monitor 🚨

**Tárgy-alapú közelségfigyelés szimulált szenzorral • Python • rclpy**

## 🎯 Projekt célja
Ez a ROS2 csomag egy egyszerű proximity (közelség) figyelő rendszert valósít meg két node-dal:
egy szenzor véletlenszerű távolságot generál, egy feldolgozó node pedig az érték alapján állapotot határoz meg:

| Távolság | Állapot |
|---------:|:-------|
| < 25 cm | 🔴 DANGER |
| < 60 cm | 🟠 WARNING |
| >= 60 cm | 🟢 CLEAR |

## 🧩 Felépítés
| Node | Topic I/O | Üzenettípus | Leírás |
|------|-----------|-------------|--------|
| proximity_sensor | /proximity/distance → publish | std_msgs/Float32 | véletlenszerű távolság cm-ben |
| proximity_processor | /proximity/distance → subscribe<br>/proximity/state → publish | Float32 → String | állapotkategorizálás |

## 📦 Telepítés & futtatás

```bash
# Munkaterület létrehozás
mkdir -p ~/ros2_proximity_monitor/src
cd ~/ros2_proximity_monitor/src

# Csomag bemásolása / klónozása
# -> helyezd ide a ros2_proximity_monitor mappát

# Build és setup
cd ~/ros2_proximity_monitor
colcon build
source install/setup.bash

# Indítás
ros2 launch ros2_proximity_monitor proximity_launch.py
```

## Ellenőrzés
```bash
ros2 topic echo /proximity/distance
ros2 topic echo /proximity/state
```

## ⚙️ Paraméterezés

| Node | Paraméter | Default |
|------|-----------|---------|
| proximity_sensor | rate_hz | 5.0 |
| proximity_sensor | min_cm, max_cm | 5.0 – 200.0 |
| proximity_processor | warn_threshold_cm | 60.0 |
| proximity_processor | danger_threshold_cm | 25.0 |

Paraméterezett indítás:
```bash
ros2 run ros2_proximity_monitor proximity_sensor --ros-args -p rate_hz:=10
```

## Hibakezelés
Ha ezt kapod:
> Package 'ros2_proximity_monitor' not found

Ellenőrizd:
- helyes mappanév: ros2_proximity_monitor
- a csomag a `src/` alatt van build előtt
- build után futtasd: `source install/setup.bash`

## 📂 Projekt felépítés
```
ros2_proximity_monitor/
 ├── ros2_proximity_monitor/
 │   ├── proximity_sensor.py
 │   ├── proximity_processor.py
 │   └── __init__.py
 ├── launch/
 │   └── proximity_launch.py
 ├── resource/
 ├── package.xml
 ├── setup.py
 └── README.md
```

## 📜 Licenc
MIT
