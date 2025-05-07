def when_started1():
    drivetrain.drive_for(FORWARD, 36, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    while True:
        drivetrain.drive_for(FORWARD, 35, INCHES)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 72, INCHES)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 72, INCHES)

vr_thread(when_started1)
