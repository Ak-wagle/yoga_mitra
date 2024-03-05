import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import pyttsx3

class TalkingNode(Node):
    def __init__(self):
        super().__init__('talking_node')
        self.engine = pyttsx3.init()
        self.trigger_ = "yes"
        self.speech_output = "Hello user, good morning. Your today's yoga routine list is: 1. Surya Namaskara, 2. Vrikshasana. Shall we start with the first one?"
        self.publisher_ = self.create_publisher(String, 'speech_output', 10)
        self.publish_speech()

    def publish_speech(self):
        msg = String()
        msg.data = self.trigger_
        self.engine.say(self.speech_output)
        self.engine.runAndWait()
        self.publisher_.publish(msg)
        self.get_logger().info('Published speech output.')

def main(args=None):
    rclpy.init(args=args)
    node = TalkingNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()