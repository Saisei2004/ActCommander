import rospy
import smach
import smach_ros
# from utils import *
import rospy
from std_msgs.msg import Int32

#########################################
person_names = ["Yoshimura", "Angel", "Basil", "Chikako", "Andrew", "Sophia", "Jack", "Mike", "Leo", "Tom"]
location_names = ["dining room", "living room", "bedroom", "study room"]
placement_location_names = ["counter","low table","tall table","shelf","dining table",]
room_names = ["dining room", "living room", "bedroom", "study room"]
object_names = ["cookies","noodles","potato chips","caramel corn","detergent","sponge","lunch box","dice","glue gun","light bulb","phone stand"]
object_categories_singular = ["cookie", "noodle", "potato chip", "caramel corn", "detergent", "sponge", "lunch box", "dice", "glue gun", "light bulb", "phone stand"]
object_categories_plural = ["cookies", "noodles", "potato chips", "caramel corn", "detergents", "sponges", "lunch boxes", "dice", "glue guns", "light bulbs", "phone stands"]


import random
#########################################

rospy.loginfo("ノードが起動しました")
from cmd_gen import *
from config import *
def input_com():
    cmd_gen = CommandGenerator(
        person_names,
        location_names,
        placement_location_names,
        room_names,
        object_names,
        object_categories_plural,
        object_categories_singular
    )
    input_text = cmd_gen.generate_command_start()
    # input_text = "meet Tom at the bedroom then locate them in the living room"
    # input_text = input("::")
    input_text = input_text.lower()

    return input_text

def look_person():#LookPerson
    print(f"目の前の人を見る")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def find_person():#FindPerson
    print(f"人を探す")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def find_pose(person,room):#FindPose
    print(f"{room}で{person}ポーズの人を見つける")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value
    
def count_pose(person):#CountPose
    print(f"{person}ポーズの人を数える")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def find_color_cloth(color,clothe):#FindColorCloth
    print(f"{color}色の{clothe}の服を着ている人を探す")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def count_color_cloth(color,clothe):#CountColorCloth
    print(f"{color}色の{clothe}の服を着ている人を数える")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def find_info(person_info):#FindInfo
    print(f"目の前の人の{person_info}の特徴を取得する")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def count_object(obj):#CountObject
    print(f"{obj}の数を数える")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def find_object(obj, now_room):#FindObject
    print(f"{now_room}で{obj}を探す")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def find_feature(obj_comp,obj):#FindFeature
    print(f"{obj_comp}の{obj}を探して特定する")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def answer_question():#AnswerQuestion
    print(f"質問に答える")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def greet_selfintro():#GreetSelfintro
    print(f"挨拶と自己紹介をする")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def give_info(talk):#GiveInfo
    print(f"{talk}を伝える")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def give_saved_info(saved_info):#GiveSavedInfo    
    print(f"{saved_info}を伝える")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def navigate(rooms):#Navigate
    print(f"{rooms}に移動")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def navi_front(room):
    print(f"{room}の目の前に移動")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def approach_person():#ApproachPerson
    print(f"人に近づく")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def follow_person(rooms=None):#FollowPerson
    print("目の前の人についていく")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def guide(rooms):#Guide
    print(f"{rooms}へ案内する")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def pick_object(obj):#PickObject
    print(f"{obj}を持つ")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def hand_object():#HandObject
    print(f"持っているものを渡す")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def put_object(pl):#PutObject
    print(f"{pl}に持っているものを置く")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def find_name(name):#FindName
    print(f"角度調べて{name}の場所を特定する")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def guest_intro(name,add_info = None):
    if add_info != None:
        print(f"{name}を紹介し,追加情報：{add_info}を伝える。")
    else:
        print(f"{name}を紹介する")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def enter_room():
    print("ドアが空いたら入場する")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def free_talk(talk):
    print(f"{talk}としゃべる")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def image_info(prompt):
    print(f"{prompt}の情報をもとに画像認識を行う")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def free_ask(talk):
    print(f"{talk}と言って、自由な回答を求める")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def ask_yesno(talk):
    print(f"{talk}と言って、yes/noの回答を求める")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def get_comfig(config):
    print(f"{config}の情報を取得する")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def open_door():
    print("ドアを開ける")
    value = random.choices([True, False], weights=[7, 3])[0]
    return value

def 