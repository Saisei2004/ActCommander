#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

def publisher():
    rospy.init_node('random_publisher', anonymous=True)  # ノードの初期化
    pub = rospy.Publisher('/random_topic', Int32, queue_size=10)  # トピックを作成
    rate = rospy.Rate(1)  # 1Hz（1秒ごとに送信）

    while not rospy.is_shutdown():
        random_number = random.randint(1, 100)  # 1〜100のランダムな整数
        rospy.loginfo(f"Publishing: {random_number}")
        pub.publish(random_number)  # トピックを送信
        rate.sleep()  # 1秒待機

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
