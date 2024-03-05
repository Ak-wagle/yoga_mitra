import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import speech_recognition as sr

class ListeningNode(Node):
    def __init__(self):
        super().__init__('listening_node')
        self.subscription = self.create_subscription(String, 'speech_output', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(String, 'topic2', 10)
        self.listening = False
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listener_callback(self, msg):
        if msg.data == "yes":
            self.get_logger().info('Received "yes", starting listening for "go" command.')
            self.listening = True
            self.listen_for_go_command()

    def listen_for_go_command(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.get_logger().info('Listening for "go" command...')
            audio = self.recognizer.listen(source)
        try:
            recognized_text = self.recognizer.recognize_google(audio)
            self.get_logger().info('Recognized: {}'.format(recognized_text))
            if "go" in recognized_text:
                self.publish_openthecv()
        except sr.UnknownValueError:
            self.get_logger().info('Could not understand audio.')
        except sr.RequestError as e:
            self.get_logger().info('Speech recognition service error: {}'.format(e))

    def publish_openthecv(self):
        msg = String()
        msg.data = "openthecv"
        self.publisher_.publish(msg)
        self.get_logger().info('Published "openthecv".')

def main(args=None):
    rclpy.init(args=args)
    node = ListeningNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
