#!/usr/bin/env python
# -*- coding: utf-8 -*-

# baseフォルダのファイルを加工して問題に変換する
"""
    重要：適当に問題を生成しています。
    
    元の文章
        改行を入れて選択肢を並べる
        


"""
import os
import random

# MASK_CHAR:マスクに使用する文字 

# 空白にするとマスクが空白になる
# MASK_CHAR=" "

# ""にするとマスクではなく削除になる
# MASK_CHAR=""

MASK_CHAR="_"
FLAG_ANSWER=False
FLAG_SYSTEM_RANDOM=False

def fake_symbol(w_anser,w_word):
    def fake_symbol_inner(w_tmp_word):
        for w_prefix_suffix in ["'",'"',"?",",","!",".",";",":"]:
            if(w_anser[0]==w_prefix_suffix ):
                w_tmp_word=w_prefix_suffix + w_tmp_word
            if(w_anser[-1]==w_prefix_suffix ):
                w_tmp_word=w_tmp_word+w_prefix_suffix  
        return w_tmp_word
    w_pre=w_word
    w_tmp=fake_symbol_inner(w_word)
    while(w_pre!=w_tmp):
        w_pre=w_tmp
        w_tmp=fake_symbol_inner(w_word)
    return w_tmp

def reg_eliminate_symbol(w_word):
    def reg_word_inner(w_tmp_word):
        for w_prefix_suffix in ["'",'"',"?",",","!",".",";",":"]:
            if len(w_tmp_word)==0:
                continue
            if(w_tmp_word[0]==w_prefix_suffix ):
                w_tmp_word=w_tmp_word[1:]
            if(w_tmp_word[-1]==w_prefix_suffix ):
                w_tmp_word=w_tmp_word[:-1]
        return w_tmp_word

    w_pre=w_word
    w_tmp=reg_word_inner(w_word)
    while(w_pre!=w_tmp):
        w_pre=w_tmp
        w_tmp=reg_word_inner(w_word)
    return w_tmp

def reg_word(w_word):
    return reg_eliminate_symbol(w_word.lower())    
    

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


di_word_dict=dict()

def prepare_word_dict(wlines):
    for line in wlines:
        line_info=line_to_number_body_pair(line)
        if is_memory_line(line_info):
            wwords=line_info[1].strip().split(" ")
            for word in wwords:
                if word[0]!="(":
                    di_word_dict[reg_word(word.strip())]=1

def my_shuffle(wlist,wrandbase=0):
    if FLAG_SYSTEM_RANDOM:
        #　動かすたびにlv02,lv03,lv04の結果がランダムになる
        # githubにアップする結果が毎回変わるので固定にするために擬似的なシャッフルを作成
        w_new_list=wlist[:]
        random.shuffle(w_new_list)
        return w_new_list
    else:
        #　lv02,lv03,lv04の結果が固定になる。ランダムではないシャッフル
        w_tmp_list=wlist[:]
        
        for i in range(0,len(w_tmp_list)):
            j=dum_rand(len(w_tmp_list)-1,i+wrandbase)
            if i!=j:
                tmp=w_tmp_list[i]
                w_tmp_list[i]=w_tmp_list[j]
                w_tmp_list[j]=tmp
        return w_tmp_list


def dum_rand(max_rnd,i):
    """乱数
    """
    if FLAG_SYSTEM_RANDOM:
        wret= random.randint(0,max_rnd)
    else:
        #固定の乱数にする
        random.seed(i)
        wret= random.randint(0,max_rnd)
        #wret= ((i * 3+5 ) *7+i) % max_rnd 
        
    #print ("wret:",wret)
    
    return wret

        
def change_candidate(w_answer,w_candidate):
    w_no_symbol_anser=reg_eliminate_symbol(w_answer)
    w_char_u=[chr(i) for i in range(65, 65+26)] # A,B
    if(w_no_symbol_anser[0] in w_char_u):
        ##大文字　小文字の調整
        w_candidate=w_candidate[0].upper()+w_candidate[1:]
    if w_answer[0]=="'":
        w_candidate="'"+w_candidate
    if w_answer[0]=='"':
        w_candidate='"'+w_candidate
    #print("change_candidate:w_answer:",w_answer)
    #print("change_candidate:w_candidate:",w_candidate)
    w_candidate=fake_symbol(w_answer,w_candidate)
    #print("change_candidate:new-w_candidate:",w_candidate)
    return w_candidate
        
        

def get_word_candidate(w_word,wlinecount):
    w_reg_ans=reg_word(w_word)
    w_tmp_candidate_list=list()
    wlen=len(w_reg_ans)
    wtop=w_reg_ans[0]
    
    w_candidate_list=di_word_dict.keys()
    for w_candidate in w_candidate_list:
        if wlen==len(w_candidate) and wtop==w_candidate[0] and w_candidate!=w_reg_ans:
            w_tmp_candidate_list.append(w_candidate )
    
    
    wdiff=1
    while len(w_tmp_candidate_list)<3 and wdiff<100: 
        for w_candidate in w_candidate_list:
            if abs(wlen-len(w_candidate))<wdiff and w_candidate!=w_reg_ans:
                if w_candidate  not in  w_tmp_candidate_list:
                    w_tmp_candidate_list.append(w_candidate )
        wdiff=wdiff+1
        
    
    #print ("w_tmp_candidate_list:",w_tmp_candidate_list)
    w_ret_candidate_list=list()
    for w_tmp_candidate in w_tmp_candidate_list:
        w_ret_candidate_list.append(change_candidate(w_word,w_tmp_candidate ))
    #print ("w_ret_candidate_list:",w_ret_candidate_list)
        
    w_ret_candidate_list=my_shuffle(w_ret_candidate_list,wlinecount+len(w_ret_candidate_list)    )
    w_ret_candidate_list=w_ret_candidate_list[0:3]
        
    #回答を追加
    if FLAG_ANSWER:
        w_ret_candidate_list=[]#回答のみ場合は候補を使わない
    w_ret_candidate_list.append(w_word)

    w_ret_candidate_list=my_shuffle(w_ret_candidate_list,wlinecount+len(w_word)+len(w_candidate_list))    
    return w_ret_candidate_list
    
    
def proc_line_candidate(line,wlinecount):
    w_words=line.split(" ")
    w_new_words=list()
    wordcount=1
    
    #chk_char=get_lv_char(lv)
    w_hole_dict=dict()
    for w_word in w_words:
        if ((wordcount*3+wlinecount) % 7)==1 and w_word[0]!="(":
            w_hole_dict[wordcount]=1
            w_new_words.append(str(wordcount)+")"+MASK_CHAR*len(w_word))
        else:
            w_new_words.append(w_word)
        wordcount=wordcount+1
        
    w_new_words.append("\n")
    
    #回答候補を追加
    wordcount=1
    for w_word in w_words:
        if wordcount in w_hole_dict:
            w_candidate_list=get_word_candidate(w_word,wlinecount+wordcount)
            #print( "w_word :",w_word )
            #print( "w_candidate_list :",w_candidate_list )
            #一番最初に単語の位置
            w_new_words.append(" " +str(wordcount)+")\n")
            for w_candidate in w_candidate_list:
                w_new_words.append("    "+ w_candidate+"\n")
            w_new_words.append("\n")
        wordcount=wordcount+1
     
    return " ".join(w_new_words)                

    
def proc_txt_candidate(lines,lv):
    """
        元の文章から単語の候補を並べる
    """
    w_ret=list()
    
    wcount=0
    wlinecount=0
    for line in lines:
        line_info=line_to_number_body_pair(line)
        wlinecount=wlinecount+1
        if is_memory_line(line_info):
            if FLAG_ANSWER:
                w_ret.append(line.strip())
            w_new_line=line_info[0]+" "+proc_line_candidate(line_info[1],wlinecount)
            w_ret.append(w_new_line)
        else:
            w_ret.append(line.strip())
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
    
    if FLAG_ANSWER:
        fn_quiz="./quiz6-a"+w_quiz_dir_suffix+"/lv"+slv+"_"+f_suffix+"/"+w_chap_file_name
    else:
        fn_quiz="./quiz6/"+w_quiz_dir_suffix+"/lv"+slv+"_"+f_suffix+"/"+w_chap_file_name
    fn_quiz_dir=os.path.dirname(fn_quiz)
    makedirs(fn_quiz_dir)
    
    f=open(fn_quiz,"w")
    txt_write="\n".join(w_li_quiz_text)
    txt_write="Lv"+str(lv)+"-"+f_suffix+"\n"+txt_write +"\n"
    f.write(txt_write)
    f.close()
    
def make_quiz_line(lines,lv):
    #chk_char=get_lv_char(lv)
    
    return ("_candidate",proc_txt_candidate(lines,lv))

    
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

        prepare_word_dict(lines)

        #for lv in range(66,70):
        for lv in range(1,2):
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
    #FLAG_ANSWER=True
    #FLAG_SYSTEM_RANDOM=True
    make_quiz()
    
    # Holmes 
    #make_quiz_holmes()
