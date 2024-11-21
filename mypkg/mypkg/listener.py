import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

rclpy.init()
node = Node("listener")


def main():
    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "関口友雪"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                responce = future.result()
            except:
                node.get_logger().info('u r loser')
            else:
                node.get_logger().info("age: {}".format(response.age))

            break

    node.destory_node()
    rclpy.shutdown()
