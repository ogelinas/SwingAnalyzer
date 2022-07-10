from enum import Enum


class Metric(Enum):
    ATTACK_ANGLE = ('attackAngle', 'Attack Angle', 'Attack Angle (in deg)', True)
    BACK_SPIN = ('backSpin', 'Back Spin', 'Back Spin (in RPM)', True)
    CARRY_DISTANCE = ('carryDistance', 'Carry Distance', 'Carry Distance (in yd)', True)
    CARRY_DEVIATION_DISTANCE = ('carryDeviationDistance', 'Carry Deviation Distance', 'Carry Deviation Distance (in yd)', False)
    CLUB_HEAD_SPEED = ('clubHeadSpeed', 'Club Head Speed', 'Club Head Speed (in mph)', True)
    CLUB_PATH_ANGLE = ('clubPathAngle', 'Club Path Angle', 'Club Path Angle (in deg)', False)
    HORIZONTAL_LAUNCH_ANGLE = ('horizontalLaunchAngle', 'Horizontal Launch Angle', 'Horizontal Launch Angle (in deg)', False)
    SMASH_FACTOR = ('smashFactor', 'Smash Factor', 'Smash Factor', True)
    SIDE_SPIN = ('sideSpin', 'Side Spin', 'Side Spin (in RPM)', False)
    SPIN_AXIS = ('spinAxis', 'Spin Axis', 'Spin Axis (in rad)', False)
    SPIN_RATE = ('spinRate', 'Spin Rate', 'Spin Rate (in RPM)', True)
    TEMPO = ('tempo', 'Tempo', 'Tempo', True)
    VERTICAL_LAUNCH_ANGLE = ('verticalLaunchAngle', 'Vertical Launch Angle', 'Vertical Launch Angle (in deg)', True)
    
    def __init__(self, data, short_description, long_description, vert) -> None:
        self.data = data
        self.short_description = short_description
        self.long_description = long_description
        self.vert = vert