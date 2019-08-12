xyz = [-1, 0.2, 3] #coordinate system x - forward / backward from the nose (chunk); y - height (meter); z - left / right of the nose (chunk)
speed = [1, 1] #groundspeed - main speed (meter per second); airspeed - don't lern/not use (meter per second)
chunk = 0.45 #meter of chunk

from dronekit import connect

print('X:', xyz[0])
print('Y:', xyz[1])
print('Z:', xyz[2])

#t=(chunk*xyz[0])/speed[0]

vehicle = connect('/dev/ttyAMA0', wait_ready=['parameters, attitude'], baud=57600) #connect Rasberry to PX

print "Arming motors"
# Copter should arm in GUIDED mode
vehicle.mode    = VehicleMode("GUIDED")
vehicle.armed   = True

while not vehicle.armed:
    print " Waiting for arming..."
    time.sleep(1)

print "Taking off!"
vehicle.simple_takeoff(xyz[1]) # Take off to target altitude



print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")