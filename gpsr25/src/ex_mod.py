import rospy
import smach
import smach_ros
from utils import *
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
    input_text = input("::")
    input_text = input_text.lower()

    return input_text

def look_person():#
    print(f"目の前の人を見る")
    # print("完成")
    print("0🔵")
    # print("の場所を特定する")
    # print("できてない")

def find_person():#
    print(f"人を探す")
    print("1🔵")

def find_pose(person,room):#
    print(f"{room}で{person}ポーズの人を見つける")
    print("2🔵")

def count_pose(person):#見極めまではやらん
    print(f"{person}ポーズの人を数える")
    print("3🔵")
    return "３にん"

def find_color_cloth(color,clothe):#
    print(f"{color}色の{clothe}の服を着ている人を探す")
    print("4🔵")

def count_color_cloth(color,clothe):#見極めまではやらん
    print(f"{color}色の{clothe}の服を着ている人を数える")
    count = 3
    print("5🔵")
    return count

def find_info(person_info):#
    print(f"目の前の人の{person_info}の特徴を取得する")
    print("6🔵")
    return "いい感じの答え"

def count_object(obj):#見極めまではやらん
    print(f"{obj}の数を数える")
    print("7🔵?")
    return "There are 1 cup"

def find_object(obj, now_room):#
    if obj == None:
        obj = "aaaaaaaaaaaa"
    print(f"{now_room}で{obj}を探す")

    print("8⚪")

def find_feature(obj_comp,obj):#見極めまではやらん
    print(f"{obj_comp}の{obj}を探して特定する")
    print("9🔴")
    return f"{obj_comp}{obj} is at the far right"

# def identify_person(): #未使用
#     print(f"あるひとの身体的特徴を特定する")

# 対話・コミュニケーション
def answer_question():#
    print(f"質問に答える")
    print("10🔵")

# def ask_name():#未使用
#     print(f"名前を聞く")

def greet_selfintro():#完成
    print(f"挨拶と自己紹介をする")
    print("11🔵")

def give_info(talk):#完成
    print(f"{talk}を伝える")
    print("12🔵")

def give_saved_info(saved_info):#
    
    print(f"{saved_info}を伝える")
    print("13🔵")

# 行動・移動
def navigate(rooms):#既存
    print(f"{rooms}に移動")
    print("14🔵")

def approach_person():#
    print(f"人に近づく")
    print("15🔵")

def follow_person(rooms=None):#見極めまではやらん
    if rooms:
        print(f"{rooms} までついていく")
    else:
        print("目の前の人についていく")
    print("16🔵")

def guide(rooms):#
    print(f"{rooms}へ案内する")
    print("17🔵")

# 操作・物体の取り扱い
def pick_object(obj):#だにーる
    print(f"{obj}を持つ")
    print("18🔵")

def hand_object():#だにーる 完成
    print(f"持っているものを渡す")
    print("19🔵")

def put_object(pl):#見極めまではやらん
    print(f"{pl}に持っているものを置く")
    print("20🔵")

def find_name(name,):#見極めまではやらん
    print(f"角度調べて{name}の場所を特定する")
    print("21🔵")

