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

# Csomag klónozása
git clone https://github.com/Pecsrik2243/nem_dox_ajr.git

# Build és setup
cd ~/ros2_proximity_monitor
colcon build

# Sourceolás
source install/setup.bash

# Indítás
ros2 launch ros2_proximity_monitor proximity_launch.py
```

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
