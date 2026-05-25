import rclpy
from .robot_arm_controller_base import BaseArmController

class RightArmController(BaseArmController):
    def __init__(self):
        super().__init__(
            arm_name='right',  # We assume the name for the bi-manual robot is left and right
            robot_name = "kinova",#Your own robot type
            mirror=False, # # If True, maps the RIGHT controller input to the LEFT arm (and vice versa).
            base_frame_id = "base_link", # The root reference frame for all robot movements (World Frame).
            filter_window_size = 1,# Size of the moving average filter;
            end_effector_link_name = "end_effector_link",# The name of the specific link we want to control/move.
            ctrl_prefix = "",# Name for the robot's inverse kinematics controller, includes the namespace
            gripper_action_topic = "/robotiq_gripper_controller/gripper_cmd"# The Action Server topic for opening/closing the gripper, includes the namespace.
        )

def main(args=None):
    rclpy.init(args=args)
    node = RightArmController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()