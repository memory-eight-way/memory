#!/usr/bin/env python
# -*- coding: utf-8 -*-

# baseフォルダのファイルを加工して問題に変換する
"""
    重要：適当に問題を生成しています。
        
    quiz,quiz2,..,quiz5を一括で生成します。

"""
import os
import random
import make_quiz as q1
import make_quiz2_swap as q2
import make_quiz3_mask_letter_contain as q3
import make_quiz4_mask_letter_start as q4
import make_quiz5_mask_letter_end as q5



def make_quiz_file(w_dir_root,w_file_suffix):
    q1.make_quiz_file(w_dir_root,w_file_suffix)
    q2.make_quiz_file(w_dir_root,w_file_suffix)
    q3.make_quiz_file(w_dir_root,w_file_suffix)
    q4.make_quiz_file(w_dir_root,w_file_suffix)
    q5.make_quiz_file(w_dir_root,w_file_suffix)


def make_quiz_holmes():
    
    make_quiz_file("../holmes/base/SH_01_A_Study_in_Scarlet","SH_01")

    make_quiz_file("../holmes/base/SH_02_The_Sign_of_the_Four","SH_02")

    make_quiz_file("../holmes/base/SH_03_The_Hound_of_the_Baskervilles","SH_03")

    make_quiz_file("../holmes/base/SH_04_The_Valley_of_Fear","SH_04")

    make_quiz_file("../holmes/base/SH_05_The_Adventures_of_Sherlock_Holmes","SH_05")

    make_quiz_file("../holmes/base/SH_06_The_Memoirs_of_Sherlock_Holmes","SH_06")

    make_quiz_file("../holmes/base/SH_07_The_Return_of_Sherlock_Holmes","SH_07")

    make_quiz_file("../holmes/base/SH_08_His_Last_Bow","SH_08")


    
def make_quiz():
    #make_quiz_file("../TheArtOfWar/base","TheArtOfWar")
    make_quiz_file("../TheArtOfWar/base","")
    
    
def set_flag_answer(wFlag):
    q1.FLAG_ANSWER=wFlag    
    q2.FLAG_ANSWER=wFlag    
    q3.FLAG_ANSWER=wFlag    
    q4.FLAG_ANSWER=wFlag    
    q5.FLAG_ANSWER=wFlag    

if __name__=="__main__":
    # set_flag_answer(True)　を実行するとQuizファイルの中身に回答を含めて作る（練習用）
    #set_flag_answer(True)


    # The Art Of War
    make_quiz()
    
    # Holmes 
    #make_quiz_holmes()
