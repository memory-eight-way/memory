#!/usr/bin/env python
# -*- coding: utf-8 -*-

# baseフォルダのファイルを加工して問題に変換する
"""
    重要：適当に問題を生成しています。
        
    ※lv=レベル
    ※加工ファイル名はプログラムに埋め込んでいる（make_quiz関数）
    ※自分にできるところから始める
    
    入れ替え特化の問題作成
        入れ替え単語の先頭に*をつけます。        

"""
import os
import random

MARK_CHAR="*"
FLAG_ANSWER=False

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

def mark_word(word):
    if word[0]==MARK_CHAR:
        return word
    return MARK_CHAR+word

def dum_rand(max_rnd,i):
    """乱数っぽいなにか"""
    return ((max_rnd * 3+5 ) *7+i*2) % max_rnd 

def my_shuffle(wlist,lv):
    w_tmp_list=wlist[:]
    
    for i in range(0,len(w_tmp_list)):
        #先頭の単語を並び替える
        if i <=lv:
            j=dum_rand(len(w_tmp_list),i)
            if (i!=j):
                tmp=w_tmp_list[i]
                w_tmp_list[i]=mark_word(w_tmp_list[j])
                w_tmp_list[j]=mark_word(tmp)
    return w_tmp_list

def line_to_number_body_pair(wline):
    w_word=wline.strip().split(".")
    w_line_number=w_word[0]+"."
    w_line_body=".".join(w_word[1:]).strip()
    return (w_line_number ,w_line_body)

    
def proc_txt_swap(lines,lv):
    """
        単語の入れ替え
            単語のスペルの能力は不要
    """
    w_ret=list()
    
    for line in lines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            wele=line_info[1].split(" ")
            if len(wele)>=4:
                w_new_ele=list()
                w_new_ele.append(wele[0])
                w_shuffle_ele=wele[1:-1]
                w_shuffle_ele=my_shuffle(w_shuffle_ele,lv ) #入れ替え
                w_new_ele.extend(w_shuffle_ele)
                w_new_ele.append(wele[-1])
                wele=w_new_ele        
            w_new_line=line_info[0]+" "+" ".join(wele)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
    return w_ret
    


def write_quiz_file(li_quiz,lv,w_chap_file_name,w_quiz_dir_suffix=""):    
    """
    """
    
    slv=str(lv)
    if len(slv)==1:
        slv="0"+slv
    f_suffix,w_li_quiz_text=li_quiz
    
    if FLAG_ANSWER:
        fn_quiz="./quiz2-a"+w_quiz_dir_suffix+"/lv"+slv+"_"+f_suffix+"/"+w_chap_file_name
    else:
        fn_quiz="./quiz2"+w_quiz_dir_suffix+"/lv"+slv+"_"+f_suffix+"/"+w_chap_file_name
    fn_quiz_dir=os.path.dirname(fn_quiz)
    makedirs(fn_quiz_dir)
    
    f=open(fn_quiz,"w")
    txt_write="\n".join(w_li_quiz_text)
    txt_write="Lv"+str(lv)+"-"+f_suffix+"\n"+txt_write +"\n"
    f.write(txt_write)
    f.close()
    
def make_quiz_line(lines,lv):
    return ("swap",proc_txt_swap(lines,lv))

    
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
        
        #60単語まで入れ替え
        for lv in range(1,60):
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
