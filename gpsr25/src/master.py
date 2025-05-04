import rospy
import smach
import smach_ros

# ① 基本的なStateクラスの定義
class MyState(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success', 'failure'])

    def execute(self, userdata):
        rospy.loginfo("実行中: MyState")
        # 何らかの処理（成功なら'success'を返す）
        return 'success'

# ② StateMachineの構築
def main():
    rospy.init_node('smach_example')

    # StateMachineを作成（outcomesには終了時の状態を設定）
    sm = smach.StateMachine(outcomes=['finished'])

    with sm:
        # 状態を追加
        smach.StateMachine.add('STATE1', MyState(),
                               transitions={'success': 'finished',
                                            'failure': 'STATE1'})  # ループ処理

    # ③ StateMachineの実行
    outcome = sm.execute()

if __name__ == '__main__':
    main()
