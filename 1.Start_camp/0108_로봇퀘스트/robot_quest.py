from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

# 1. 텔레비전 시청
hub = PrimeHub()
hub.light_matrix.write('T')
pair = MotorPair('E', 'F')
pair.move(68,'cm', 0, 40)
pair.move(10,'cm',0, -30)
pair.move_tank(360, 'degrees', 30, -30)
wait_for_seconds(1)
pair.move(60, 'cm', 0, 50)
pair.stop()

# 2. 스마트그리드
hub = PrimeHub()
color_sensor = ColorSensor('A')
dist_sensor = DistanceSensor('B')
motor = Motor('C')
pair = MotorPair('E','F')
dist = dist_sensor.get_distance_cm()

pair.start(speed = 50)

while True :
    color = color_sensor.get_color()
    if color == 'black' :
        pair.stop()
        pair.move(5, 'cm', 0, 20)
        wait_for_seconds(1)
        pair.move_tank(180, 'degrees', 30, -30)
        pair.move(57, 'cm', 0, 30)
        break

pair.stop()
motor.run_for_degrees(70)
wait_for_seconds(1)
pair.move(15,'cm',0, -30)
wait_for_seconds(1)
motor.run_for_degrees(-70)
pair.move_tank(360, 'degrees', 30, -30)
wait_for_seconds(1)
pair.move(70, 'cm', 0, 50)
pair.move_tank(-180, 'degrees', 30, -30)
pair.move(60, 'cm', 0, 50)
pair.stop()

# 3. 수소플랜트
hub = PrimeHub()
pair = MotorPair('E', 'F')
motor = Motor('C')

pair.move(71, 'cm', 0, 20)
motor.run_for_degrees(70, speed=5)
pair.move(1, 'cm', 0, 30)
motor.run_for_degrees(-100, speed=5)
pair.move_tank(360, 'degrees', 30, -30)
wait_for_seconds(1)
pair.move(70, 'cm', 0, 50)
pair.stop()

# 4. 장난감
hub = PrimeHub()
color_sensor = ColorSensor('A')
dist_sensor = DistanceSensor('B')
motor = Motor('C')
pair = MotorPair('E','F')
dist = dist_sensor.get_distance_cm()

pair.move(26, speed = 50)
motor.run_for_degrees(15, spee = 20)
pair.move(6,'cm',0, -30)
pair.move_tank(360, 'degrees', 30, -30)
wait_for_seconds(0.5)
pair.move(20, 'cm', 0, 50)
pair.stop()

# 5. 수력
hub = PrimeHub()
color_sensor = ColorSensor('A')
dist_sensor = DistanceSensor('B')
motor = Motor('C')
pair = MotorPair('E','F')
dist = dist_sensor.get_distance_cm()

pair.move(24, speed = 50)
motor.run_for_degrees(-15, speed = 20)
motor.run_for_degrees(15, speed = 20)
pair.move(6,'cm',0, -30)
pair.move_tank(360, 'degrees', 30, -30)
pair.move(18, speed = 50)

# 6. 풍력
hub = PrimeHub()
color_sensor = ColorSensor('A')
dist_sensor = DistanceSensor('B')
motor = Motor('C')
pair = MotorPair('E','F')
dist = dist_sensor.get_distance_cm()

pair.start(speed = 50)

while True :
    color = color_sensor.get_color()
    if color == 'black' :
        pair.stop()
        wait_for_seconds(1)
        pair.move_tank(90, 'degrees', 30, -30)
        for _ in range(3):
            pair.move(9, 'cm', 0, 30)
            pair.move(-9, 'cm', 0, 30)
        break

pair.stop()
pair.move_tank(360, 'degrees', 30, -30)
wait_for_seconds(0.5)
pair.move(8, 'cm', 0, 50)
pair.move_tank(90, 'degrees', 30, -30)
pair.move(74, 'cm', 0, 50)
pair.stop()