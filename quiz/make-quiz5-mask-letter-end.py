#!/usr/bin/env python
# -*- coding: utf-8 -*-

# baseフォルダのファイルを加工して問題に変換する
"""
    重要：適当に問題を生成しています。
    
    lv=1 aで終わる単語をマスクします。
    lv=2 bで終わる単語をマスクします。
    lv=26 zで終わる単語をマスクします。
    レベルは難度ではないです。
    lv=26のzで終わる単語はほとんど無いのでマスクされません。


"""
import os
import random

# MASK_CHAR:マスクに使用する文字 

# 空白にするとマスクが空白になる
# MASK_CHAR=" "

# ""にするとマスクではなく削除になる
# MASK_CHAR=""

MASK_CHAR="_"



def empty_line(w_line):
    """
    """
        
    return "empty_line"


def makedirs(dir_make):
    up_dir_make = os.path.abspath(dir_make).upper()
    if os.path.isdir(dir_make):
        return
    return os.makedirs(dir_make)

def is_memory_line(line_info):
    """
    記憶対象の行かを確認する
    行番号. 文章 の構成になっているか
    """
    if len(line_info)!=2:
        # 行番号＋文章の構成でない
        return False

    if line_info[1].strip()=="":
        # 行番号＋文章の構成だけど 文章が空
        return False
    return True
    
    
def proc_line_mask(line,w_mask_char):
    wret=list()
    for wletter in line:
        if wletter!=" " and wletter in w_mask_char:
            wret.append(MASK_CHAR)
        else:
            wret.append(wletter)
    return "".join(wret)

def get_lv_char(lv):    
    chk_char="abcdefghijklmnopqrstuvwxyz"[lv-1]
    return chk_char
    
def proc_line_word_mask(line,lv):
    w_words=line.split(" ")
    w_new_words=list()
    wordcount=1
    
    chk_char=get_lv_char(lv)
    for w_word in w_words:
        if chk_char not in w_word.lower()[-1]:
            w_new_words.append(w_word)
        else:
            w_new_words.append(MASK_CHAR*len(w_word))
        wordcount=wordcount+1
    return " ".join(w_new_words)                

    
def proc_txt_mask_word(lines,lv):
    """
        指定した文字が入っている単語をマスクする    
    """

    w_ret=list()
    
    wcount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            w_new_line=line_info[0]+" "+proc_line_word_mask(line_info[1],lv)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line)
    return w_ret
    
    
    
    
def line_to_number_body_pair(wline):
    w_word=wline.strip().split(".")
    w_line_number=w_word[0]+"."
    w_line_body=".".join(w_word[1:]).strip()
    return (w_line_number ,w_line_body)


def write_quiz_file(li_quiz,lv,w_chap_file_name,w_quiz_dir_suffix=""):    
    """
    """
    
    slv=str(lv)
    if len(slv)==1:
        slv="0"+slv
    f_suffix,w_li_quiz_text=li_quiz
    
    fn_quiz="./quiz5/"+w_quiz_dir_suffix+"/lv"+slv+"_"+f_suffix+"/"+w_chap_file_name
    fn_quiz_dir=os.path.dirname(fn_quiz)
    makedirs(fn_quiz_dir)
    
    f=open(fn_quiz,"w")
    txt_write="\n".join(w_li_quiz_text)
    txt_write="Lv"+str(lv)+"-"+f_suffix+"\n"+txt_write +"\n"
    f.write(txt_write)
    f.close()
    
def make_quiz_line(lines,lv):
    chk_char=get_lv_char(lv)
    
    return ("mask_word_"+chk_char+"_end",proc_txt_mask_word(lines,lv))

    
def make_quiz_file(w_dir_root,w_file_suffix):
    """
    フォルダの単語リストを作成
    """
    print("make_quiz_file:",w_dir_root)
    wfiles=os.listdir(w_dir_root)
    for w_chap_file_name in wfiles:
        print("parse file:",w_chap_file_name )
        f=open(os.path.join(w_dir_root,w_chap_file_name),"r")
        lines=f.readlines()
        f.close()

        #for lv in range(66,70):
        for lv in range(1,27):
                w_chap_quiz=make_quiz_line(lines,lv)
                write_quiz_file(w_chap_quiz,lv,w_chap_file_name,w_file_suffix)

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
    


    


if __name__=="__main__":
    # The Art Of War
    make_quiz()
    
    # Holmes 
    #make_quiz_holmes()
