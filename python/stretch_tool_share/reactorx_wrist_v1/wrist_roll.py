from stretch_body.dynamixel_hello_XL430 import DynamixelHelloXL430
import stretch_body.hello_utils as hu


class WristRoll(DynamixelHelloXL430):
    """
    API to the Stretch RE1 wrist roll joint
    """
    def __init__(self, chain=None):
        DynamixelHelloXL430.__init__(self,'wrist_roll',chain)
        self.poses = {'cw_90': hu.deg_to_rad(90.0), 'forward': hu.deg_to_rad(0.0), 'ccw_90': hu.deg_to_rad(-90.0)}

    def home(self):
        """
        Home to hardstops
        """
        pass

    def pose(self,p,v_r=None,a_r=None):
        """
        p: Dictionary key to named pose (eg 'forward')
        v_r: velocityfor trapezoidal motion profile (rad/s).
        a_r: acceleration for trapezoidal motion profile (rad/s^2)
        """
        self.move_to(self.poses[p],v_r,a_r)


