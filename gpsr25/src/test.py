#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
# ノードを初期化
rospy.init_node('minimal_node', anonymous=True)
rospy.loginfo("ノードが起動しましたaaaaaaa")

import sys
import warnings

# NumPyの二重インポート警告を無効化
warnings.filterwarnings("ignore", category=UserWarning, message="The NumPy module was reloaded")


# ノードが終了するまで待機
for i in range(3):
    from gpsr_ai import *
    for module in list(sys.modules.keys()):
        if module not in sys.builtin_module_names:
            del sys.modules[module]
    
# rospy.Subscriber('/random_topic', Int32, callback)


print("↑これ")
# rospy.spin()
# rospy.signal_shutdown()
